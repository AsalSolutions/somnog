import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import tokenDecoder from './tokenDecoder';

const token = tokenDecoder();
console.log(token);
console.log(token.userRole);

//  Creating private routes for User
export const ProtectedUserRoute = ({ component: Component, ...rest }) => (
  <Route
    {...rest}
    render={(props) => {
      // if we have a token useTokenDecoder returns userid and userRole
      // otherwise it will return false
      if (token && token.userRole === 'User') {
        return <Component {...props} />;
      } else {
        return <Redirect to="/" />;
      }
    }}
  />
);

//  Creating private routes for User
export const ProtectedAdminRoute = ({ component: Component, ...rest }) => (
  <Route
    {...rest}
    render={(props) => {
      // if we have a token useTokenDecoder returns userid and userRole
      // otherwise it will return false
      if (token && token.userRole === 'Admin') {
        return <Component {...props} />;
      } else {
        return <Redirect to="/" />;
      }
    }}
  />
);
