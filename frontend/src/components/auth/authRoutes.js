import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import ForgetPassword from './ForgetPassword';
import Login from './Login';
import Register from './Register';

function AuthRoutes() {
  return (
    <>
      <h1>Auth Routes</h1>

      <Route path="/auth/login" exact component={Login} />
      <Route path="/auth/register" exact component={Register} />
      <Route path="/auth/forgetpassword" exact component={ForgetPassword} />
      <Redirect to="/" path="/auth/login" />
    </>
  );
}

export default AuthRoutes;
