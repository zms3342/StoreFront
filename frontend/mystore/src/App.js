import React from 'react';
import './App.css';
import Header from './components/Header.js'
import Product from './components/Product.js'

function App() {
  return (
    <div className="app">
      <Header />
      <div className="app__products">
        <Product name="My Product" image='https://image.shutterstock.com/image-photo/bright-spring-view-cameo-island-260nw-1048185397.jpg' price="10" />
        <Product name="My Product" image='https://image.shutterstock.com/image-photo/bright-spring-view-cameo-island-260nw-1048185397.jpg' price="10" />
        <Product name="My Product" image='https://image.shutterstock.com/image-photo/bright-spring-view-cameo-island-260nw-1048185397.jpg' price="10" />
      </div>
    </div>
  );
}

export default App;
