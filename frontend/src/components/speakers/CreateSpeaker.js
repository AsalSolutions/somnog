import React, { Component } from "react";
import { connect } from "react-redux";
import SpeakerForm from './SpeakerForm'
import { createSpeaker } from "../../actions/speakerAction";

class CreateSpeaker extends Component {
  onSubmit = (formValues) => {
    // this.props.createSpeaker(formValues);
     this.props.createSpeaker(formValues);
  };
  render() {
    return (
      <div>
        <h3>Add Speaker</h3>
        <SpeakerForm onSubmit={this.onSubmit}/>
      </div>
    );
  }
}

export default connect(null, { createSpeaker })(CreateSpeaker);
