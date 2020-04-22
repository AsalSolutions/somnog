import React from "react";
import { Router, Route } from "react-router-dom";
import history from "./history";
import SpeakerList from "./components/speaker/SpeakerList";
import Home from "./components/pages/Home";
import Header from "./components/layout/header";

function App() {
  return (
    <Router history={history}>
      <Header />
      <div>
        <Route path="/" exact component={Home} />
        <Route path="/speaker" exact component={SpeakerList} />
      </div>
    </Router>
  );
}

export default App;
