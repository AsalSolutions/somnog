import React,{Component} from 'react';

import { Layout ,Avatar,Menu} from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  NotificationOutlined,
  MessageOutlined
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
          <Header className="site-layout-background" >
            {React.createElement(this.state.collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
              className: 'trigger',
              onClick: this.toggle,
            })}
            <span style={{  float:'right', display:'flex',
                     justifyContent:"space-around",
                     alignItems:'center', width:"180px", paddingTop:"5px" }} >
                        <p> Account</p>
                        
                        <p><Avatar icon={<UserOutlined />} /> Hassan</p>
          </span>
          </Header>
          <ContentSection/>
        </Layout>
      </Layout>
    );
  }
}


export default Dashboard;




