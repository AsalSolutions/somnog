import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Dashboard from './dashboard';
import Admin from './admin/AdminDashboard';
import AuthRoutes from '../components/auth/authRoutes';
import Register from '../components/auth/Register';
import ForgetPassword from '../components/auth/ForgetPassword';
import LoginForm from '../components/auth/Login';
export default function Routes() {
  return (
    <Switch>
      <Route path="/" exact component={LoginForm} />
      <Route path="/auth/register" component={Register} />
      <Route path="/auth/forgetpassword" component={ForgetPassword} />
      <Route path="/dashboard" exact component={Dashboard} />
      <Route path="/admin" exact component={Admin} />
    </Switch>
  );
}
