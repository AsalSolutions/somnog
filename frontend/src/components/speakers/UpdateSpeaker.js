import React, { Component } from "react";
import { connect } from "react-redux";
import SpeakerForm from './SpeakerForm'
import { updateSpeaker,getSpeaker } from "../../actions/speakerAction";
import _ from 'lodash';

class UpdateSpeaker extends Component {

 componentDidMount = () => {
        const { id } = this.props.match.params;
        console.log(id)
        console.log(this.props.getSpeaker(id));
      };
  onSubmit = (formValues) => {
    // this.props.createSpeaker(formValues);
    const {id} = this.props.match.params
     this.props.updateSpeaker(id,formValues);
  };
  render() {
    console.log(this.props.speaker)
    console.log(this.props.getSpeaker)

    if (!this.props.speaker) {
        
        return "loading..";
      }
    return (
      <div>
        <h3>Update Speaker</h3>
        <SpeakerForm initialValues={_.pick(this.props.speaker, "firstName", "lastName","email","phone","companyName","jobTitle","description","photo","socialAccount")} onSubmit={this.onSubmit}/>
      </div>
    );
  }
}


const mapStateToProps = (state, ownprops) => {
    return {
      speaker: state.speakers[ownprops.match.params.id]
     
    };
  };

export default connect(mapStateToProps, { updateSpeaker,getSpeaker })(UpdateSpeaker);
