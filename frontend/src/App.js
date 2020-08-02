import React from "react";
import { Router } from "react-router-dom";
import history from "./history";



// import Header from "./components/layout/header";
import Dashboard from './layout'

function App() {
  return (
    <Router history={history}>
      <Dashboard />
    </Router>
  );
}

export default App;
