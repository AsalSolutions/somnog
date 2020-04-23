import React from "react";
import { Router, Route } from "react-router-dom";
import history from "./history";
import SpeakerList from "./components/speaker/SpeakerList";
import CreateSpeaker from "./components/speaker/CreateSpeaker";
import Home from "./components/pages/Home";
import Header from "./components/layout/header";

function App() {
  return (
    <Router history={history}>
      <Header />
      <div>
        <Route path="/" exact component={Home} />
        <Route path="/speaker" exact component={SpeakerList} />
        <Route path="/speaker/create" exact component={CreateSpeaker} />
      </div>
    </Router>
  );
}

export default App;
