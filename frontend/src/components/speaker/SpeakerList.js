import React from "react";
import { connect } from "react-redux";
import { getSpeakers } from "../../actions/speakerAction";

class SpeakerList extends React.Component {
  componentDidMount() {
    this.props.getSpeakers();
  }

  speakerList = () => {
    const { getAllSpeakers } = this.props;
    if (!getAllSpeakers) {
      return "loading";
    }
    return getAllSpeakers.map((speaker) => {
      return (
        <ul key={speaker._id}>
          <li>FirstName: {speaker.firstName}</li>
          <li>LastName: {speaker.lastName}</li>
          <li>Email: {speaker.email}</li>
          <li>Company: {speaker.companyName}</li>
          <li>Job Title: {speaker.jobTitle}</li>
        </ul>
      );
    });
  };
  render() {
    return (
      <div>
        <p>Speakers List</p>
        <div>{this.speakerList()}</div>
      </div>
    );
  }
}

// Map state to props
const mapStateToProps = (state) => {
  return {
    getAllSpeakers: Object.values(state.speakers),
  };
};

export default connect(mapStateToProps, { getSpeakers })(SpeakerList);
