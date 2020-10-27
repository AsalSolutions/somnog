import React from 'react';
import { Table, Space, Popconfirm } from 'antd';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { getSpeakers, deleteSpeaker } from '../../actions/speakerAction';
// import DeleteSpeaker from './DeleteSpeaker';

class SpeakerList extends React.Component {
  componentDidMount() {
    this.props.getSpeakers();
  }

  columns = [
    {
      title: 'First Name',
      dataIndex: 'firstName',
      key: 'firstName',
      render: (text) => <Link to={`speaker/${text}`}> {text} </Link>,
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
      render: (record) => (
        <Space size="middle">
          <Link to={`speaker/edit/${record.id}`}> Update </Link>
          <Popconfirm
            title="Sure to delete?"
            onConfirm={() => this.renderDeleteSpeaker(record.id)}
          >
            <a>Delete</a>
          </Popconfirm>
        </Space>
      ),
    },
  ];
  // Delete Speaker
  renderDeleteSpeaker = (id) => {
    this.props.deleteSpeaker(id);
  };

  speakerList = () => {
    const { getAllSpeakers } = this.props;
    if (!getAllSpeakers) {
      return 'loading';
    }
    return getAllSpeakers.map((speaker) => {
      const speakerList = {
        id: speaker._id,
        firstName: speaker.firstName,
        lastName: speaker.lastName,
        email: speaker.email,
        phone: speaker.phone,
        companyName: speaker.companyName,
        jobTitle: speaker.jobTitle,
      };
      return speakerList;
    });
  };

  render() {
    return (
      <React.Fragment>
        <h3> Speakers List </h3>
        <Table
          columns={this.columns}
          dataSource={this.speakerList()}
          rowKey="id"
        />
      </React.Fragment>
    );
  }
}

// Map state to props
const mapStateToProps = (state) => {
  return {
    // We convert  object to an array so that we can map through
    getAllSpeakers: Object.values(state.speakers),
  };
};

export default connect(mapStateToProps, {
  getSpeakers,
  deleteSpeaker,
})(SpeakerList);
