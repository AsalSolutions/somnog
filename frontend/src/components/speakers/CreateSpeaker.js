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
    // const text = localStorage.getItem("language") === 'EN' ? 'Add Speaker' : 'Ku dar Soo Jeediye';
    const text = this.props.app.language === 'EN' ? 'Add Speaker' : 'Diiwaan Gali Speaker'
    return (
      <div>
        <h2>{text}</h2>
        <SpeakerForm onSubmit={this.onSubmit}/>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return { app: state.language };
};

export default connect(mapStateToProps, { createSpeaker })(CreateSpeaker);
