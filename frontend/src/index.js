import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import './App.css';
import App from './App';
import reducers from './reducers';

// Redux dev tools setup
const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(reducers, composeEnhancer(applyMiddleware(thunk)));

ReactDOM.render(
  <Provider store={store}>
    {/* TODO1. Login Here if and if passed then we can redirect to either
    user or admin dashboard */}
    <App />
  </Provider>,
  document.getElementById('root')
);
