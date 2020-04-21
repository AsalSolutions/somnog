import React from "react";
import { Router, Route } from "react-router-dom";
import history from "./history";
import SpeakerList from "./components/SpeakerList";
import Home from "./pages/Home";
import Header from "./layout/header";

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
