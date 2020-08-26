import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
import json
import datetime

database_path = "postgresql://postgres:password@localhost:5432/storefront"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Numbers(db.Model):  

  id = Column(Integer, primary_key=True)
  phone = Column(String)

  def __init__(self, id, phone):
      self.id = id
      self.phone = phone 

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'phone': self.question,
    }


class Product(db.Model):  

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    image = Column(String)

    def __init__(self,id, name, price, description,image):
        self.id = id
        self.name = name
        self.price = price 
        self.description = description
        self.image = image

    def format_short(self):
        return {
            'id': self.id,
            'name': self.name, 
            'price':self.price, 
            'image':self.image,
        }
    def format_long(self):
        return {
        'id': self.id,
        'name': self.name, 
        'price':self.price, 
        'image':self.image,
        'description': self.description
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Comments(db.Model):  

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    content = Column(String(300))
    product = Column(Integer ,db.ForeignKey('product.id'), nullable=False )

    def __init__(self,id, date, content, product):
        self.id = id
        self.date =date 
        self.content = content
        self.product = product

    def format(self):
        return {
            'id': self.id,
            'date': self.date, 
            'content':self.content, 
            'product':self.product,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()