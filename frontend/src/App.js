import React from "react";

class App extends React.Component {
  state = { speakerList: {}, isLoading: true };
  componentDidMount() {
    fetch("/v1/speaker")
      .then((response) => response.json())
      .then((result) => {
        this.setState({ speakerList: result, isLoading: false });
      });
  }
  speakerList = () => {
    const { speakerList, isLoading } = this.state;
    if (isLoading) {
      return;
    }
    return speakerList.map((speaker, index) => {
      return (
        <div>
          <ul>
            <li key={speaker._id}>FirstName: {speaker.firstName}</li>
            <li>LastName: {speaker.lastName}</li>
            <li>Email: {speaker.email}</li>
            <li>Company: {speaker.companyName}</li>
            <li>Job Title: {speaker.jobTitle}</li>
          </ul>
        </div>
      );
    });
  };
  render() {
    return (
      <div>
        {/* <SpeakerList speaker={this.state.speakerList} /> */}

        <p>Speakers List</p>
        <div>{this.speakerList()}</div>
      </div>
    );
  }
}

export default App;
