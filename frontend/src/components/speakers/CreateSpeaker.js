import React, { Component } from 'react';
import { connect } from 'react-redux';
import SpeakerForm from './SpeakerForm';
import { createSpeaker } from '../../actions/speakerAction';

class CreateSpeaker extends Component {
  onSubmitHandler = (formValues) => {
    this.props.createSpeaker(formValues);
  };

  render() {
    const text =
      this.props.app.language === 'EN' ? 'Add Speaker' : 'Diiwaan Gali Speaker';
    return (
      <div>
        <h2>{text}</h2>
        <SpeakerForm onSubmit={this.onSubmitHandler} />
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return { app: state.language };
};

export default connect(mapStateToProps, { createSpeaker })(CreateSpeaker);
