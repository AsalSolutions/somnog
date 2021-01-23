import React from 'react';
import { Router, Route } from 'react-router-dom';
import history from './helpers/history';

import LoginForm from './components/auth/Login';
import Admin from './layout/admin';
import Dashboard from './layout/dashboard';
import {
  ProtectedUserRoute,
  ProtectedAdminRoute,
} from './helpers/ProtectedRoute';

// import Header from "./components/layout/header";

function App({ user }) {
  /* TODO 1: Check if the user is authenticated  */
  /* TODO 2: Check If the User is Admin or Normal User */
  /* TODO 3: Only Admin Users are allowed to visit Admin Dashboard */
  return (
    <Router history={history}>
      <Route path="/" exact component={LoginForm} />
      {/* <Route path="/dashboard" exact component={Dashboard} /> */}
      <ProtectedAdminRoute path="/admin" exact component={Admin} />
      {/* <Route path="/dashboard" exact component={Dashboard} /> */}
      <ProtectedUserRoute path="/dashboard" component={Dashboard} />
    </Router>
  );
}

export default App;
