import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from models import setup_db, Comments, Numbers, Product

app = Flask(__name__)
setup_db(app)
CORS(app)


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, true'
    header['Access-Control-Allow-Methods'] = 'POST,GET,PUT,DELETE,PATCH,OPTIONS'
    return response

@app.route('/')
def test():
   return("hello world ")

@app.route('/products')
def get_products(): 
    products = Product.query.all()
    if len(products) == 0:
        abort(420)
    return jsonify({
        "success": True, 
        "products": [product.format_short() for product in products]
    })

@app.route('/products/<id>')
def get_product_detail(id): 
    #get product
    product = Product.query.filter_by(id=id).one()
    
    #if product is none abort with 404
    if product is None: 
        abort(404)
    
    #get details for jsonify 
    product_details = product.format_long()

    return jsonify({
        "success":True, 
        "product":product_details
    })

#add product 
@app.route('/products/<id>', methods=[POST])
def get_product_detail(id): 
    #get product
    product = Product.query.filter_by(id=id).one()
    
    #if product is none abort with 404
    if product is None: 
        abort(404)
    
    #get details for jsonify 
    product_details = product.format_long()
    
    return jsonify({
        "success":True, 
        "product":product_details
    })



