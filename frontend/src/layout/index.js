import React,{Component} from 'react';

import { Layout ,Avatar,Space} from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined 

} from '@ant-design/icons';

import Sidebar from './Sidebar';
import ContentSection from './ContentSection'
import  LanguageDropDown from './LanguageDropDown.js'

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
            <Space style={{  float:'right', display:'flex',
                     justifyContent:"space-around",
                     alignItems:'center', width:"280px" }} >
                        <span> Account</span>
                        <span><Avatar icon={<UserOutlined />} /> Hassan</span>
                        <LanguageDropDown/>
                        

          </Space>
          </Header>
          <ContentSection/>
        </Layout>
      </Layout>
    );
  }
}


export default Dashboard;




