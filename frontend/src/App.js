import React from "react";
import { Router } from "react-router-dom";
import history from "./history";



// import Header from "./components/layout/header";
import Dashboard from './layout'

function App() {
  return (
    <Router history={history}>
      <Dashboard />
      {/* <div>
        <Route path="/" exact component={Home} />
        <Route path="/speaker" exact component={SpeakerList} />
        <Route path="/speaker/create" exact component={CreateSpeaker} />
      </div> */}
    </Router>
  );
}

export default App;
