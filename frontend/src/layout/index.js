import React,{Component} from 'react';

import { Layout ,Avatar,Row} from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined
} from '@ant-design/icons';

import Sidebar from './Sidebar';
import ContentSection from './ContentSection'

const { Header } = Layout;

class Dashboard extends Component {
  state = {
    collapsed: false,
  };

  toggle = () => {
    this.setState({
      collapsed: !this.state.collapsed,
    });
  };

  render() {
    return (
      <Layout>
        {/* Sidebar */}
        <Sidebar collapsed={this.state.collapsed} />
        <Layout className="site-layout">
          <Header className="site-layout-background" style={{ paddingLeft: 20 }}>
            {React.createElement(this.state.collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
              className: 'trigger',
              onClick: this.toggle,
            })}
            <Row>
                <Avatar size={32} icon={<UserOutlined />} />
            </Row>
          </Header>
          <ContentSection/>
        </Layout>
      </Layout>
    );
  }
}


export default Dashboard;




