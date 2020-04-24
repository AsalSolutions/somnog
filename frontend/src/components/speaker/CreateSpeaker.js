import React, { Component } from "react";
import { connect } from "react-redux";
import SpeakerForm from "./SpeakerForm";
import { createSpeaker } from "../../actions/speaker";

class CreateSpeaker extends Component {
  onSubmit = (formValues) => {
    console.log(formValues);
    this.props.createSpeaker(formValues);
  };
  render() {
    return (
      <div>
        <h3>Add Speaker</h3>
        <SpeakerForm onSubmit={this.onSubmit} />
      </div>
    );
  }
}

export default connect(null, { createSpeaker })(CreateSpeaker);
