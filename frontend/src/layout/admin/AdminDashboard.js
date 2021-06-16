import React, { Component } from 'react';
import { Layout, Avatar, Space } from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
} from '@ant-design/icons';

import { connect } from 'react-redux';
import { getUserProfile, signOut } from '../../actions/auth';

import Sidebar from './Sidebar';
import ContentSection from './ContentSection';
import LanguageDropDown from '../LanguageDropDown.js';
import tokenDecoder from '../../helpers/tokenDecoder';
import SpeakerList from '../../components/speakers/SpeakerList';

// get user id and role
const { userId } = tokenDecoder();
const { Header } = Layout;

class Admin extends Component {
  state = {
    collapsed: false,
  };
  // Get Current User Information
  componentDidMount = () => {
    this.props.getUserProfile(userId);
  };

  toggle = () => {
    this.setState({
      collapsed: !this.state.collapsed,
    });
  };

  render() {
    if (!this.props.user) {
      return 'Loading...';
    }
    // Load User Information
    const { username } = this.props.user;
    return (
      <Layout>
        {/* Sidebar */}
        <Sidebar collapsed={this.state.collapsed} />
        <Layout className="site-layout">
          <Header className="site-layout-background">
            {React.createElement(
              this.state.collapsed ? MenuUnfoldOutlined : MenuFoldOutlined,
              {
                className: 'trigger',
                onClick: this.toggle,
              }
            )}
            <Space
              style={{
                float: 'right',
                display: 'flex',
                justifyContent: 'space-around',
                alignItems: 'center',
                width: '280px',
              }}
            >
              <span>
                <Avatar icon={<UserOutlined />} /> Welcome,
                {username}
              </span>
              <span>
                <a onClick={this.props.signOut}>Log Out</a>
              </span>

              <LanguageDropDown />
            </Space>
          </Header>
          <ContentSection />
        </Layout>
      </Layout>
    );
  }
}

const mapStateToProps = (state) => {
  return { user: state.userProfile };
};

export default connect(mapStateToProps, { getUserProfile, signOut })(Admin);
