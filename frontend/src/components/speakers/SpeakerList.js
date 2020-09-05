import React from "react";
import _uniqueId from "lodash/uniqueId";
import { Table, Space, Modal,Button } from 'antd';
import { ExclamationCircleOutlined } from '@ant-design/icons';
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { getSpeakers } from "../../actions/speakerAction";

const { confirm } = Modal;


const columns = [
  {
    title: 'First Name',
    dataIndex: 'firstName',
    key: 'firstName',
    render: text => <Link to={`speaker/${text}`}>{text}</Link>,
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
    render: record => (
      
      <Space size="middle">
        <Link to={`speaker/view/${record.key}`}>View</Link>
        <Link to={`speaker/edit/${record.key}`}>Update </Link>
        <Link to={`speaker/delete/${record.key}`}>  <Button onClick={showDeleteConfirm}>Delete</Button></Link>
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
    
      const speakerList = 
        {
          key: speaker._id,
          firstName: speaker.firstName,
          lastName: speaker.lastName,
          email:speaker.email,
          phone:speaker.phone,
          companyName: speaker.companyName,
          jobTitle:speaker.jobTitle,
        };
        
      return  speakerList 
    });
  };
  render() {
  
    return (
      <React.Fragment>
        <h3>Speakers List</h3>
        <Table columns={columns} dataSource={this.speakerList()} rowKey={_uniqueId()}/>
        {/* <React.Table columns={columns} data={this.speakerList}></React.Table> */}
      </React.Fragment>
    );
  }
}

// Map state to props
const mapStateToProps = (state) => {
  return {
    getAllSpeakers: Object.values(state.speakers)
  };
};

// Delete Speaker 

function showDeleteConfirm() {
  confirm({
    title: 'Are you sure delete this task?',
    icon: <ExclamationCircleOutlined />,
    content: 'Some descriptions',
    okText: 'Yes',
    okType: 'danger',
    cancelText: 'No',
    onOk() {
      console.log('OK');
    },
    onCancel() {
     return <Link to="/speaker"> </Link>
    },
  });
}


export default connect(mapStateToProps, { getSpeakers })(SpeakerList);

