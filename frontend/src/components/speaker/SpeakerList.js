import React from "react";
import { Table, Space } from 'antd';
import { connect } from "react-redux";
import { getSpeakers } from "../../actions/speakerAction";
import { Link } from "react-router-dom";


const columns = [
  {
    title: 'First Name',
    dataIndex: 'firstName',
    key: 'firstName',
    render: text => <Link to={`speaker/${text}`} href="#">{text}</Link>,
  },
  {
    title: 'Last Name',
    dataIndex: 'lastName',
    key: 'lastName',
  },
  {
    title: 'Email',
    dataIndex: 'email',
    key: 'email',
  },
  {
    title: 'Phone',
    dataIndex: 'phone',
    key: 'phone',
  },
  {
    title: 'Company',
    dataIndex: 'companyName',
    key: 'companyName',
  },
  {
    title: 'Job Title',
    dataIndex: 'jobTitle',
    key: 'jobTitle',
  },
 
  {
    title: 'Action',
    key: 'action',
    render: (text, record) => (
      
      <Space size="middle">
        <Link to={`speaker/edit/${record.key}`}>Update {record.name}</Link>
        <Link to={`speaker/delete/${text.firstName}`}>Delete</Link>
      </Space>
    ),
  },
];



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
      const data = 
        {
          key: speaker._id,
          firstName: speaker.firstName,
          lastName: speaker.lastName,
          email:speaker.email,
          phone:speaker.phone,
          companyName: speaker.companyName,
          jobTitle:speaker.jobTitle,

      
        };
        
      return  data 
    });
  };
  render() {
    return (
      <div>
        <h3>Speakers List</h3>
        <Table columns={columns} dataSource={this.speakerList()}  />
        {/* <div>{this.speakerList()}</div> */}
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

