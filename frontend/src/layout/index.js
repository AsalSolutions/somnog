import React,{Component} from 'react';
import { Link ,Route } from "react-router-dom";
import { Layout, Menu ,Avatar,Row} from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
} from '@ant-design/icons';
import SpeakerList from "../components/speaker/SpeakerList";
import CreateSpeaker from "../components/speaker/CreateSpeaker";
import Home from "./pages/Home";

const { Header, Sider, Content } = Layout;

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
        <Sider trigger={null} collapsible collapsed={this.state.collapsed}>
          <div className="logo" />
          <Link to="/"> <h1 style={{color:'white',paddingTop:"20px",paddingLeft:"20px"}}>SOMNOG APP</h1></Link>
          <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
            <Menu.Item key="1" icon={<UserOutlined />}>
               Events
            </Menu.Item>
            <Menu.Item key="2" icon={<VideoCameraOutlined />}>
                <Link to="/speaker"> Speakers</Link>
            </Menu.Item>
            <Menu.Item key="3" icon={<UploadOutlined />}>
                <Link to="/speaker/create"> Add Speaker</Link>
            </Menu.Item>
          </Menu>
        </Sider>
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
          <Content
            className="site-layout-background"
            style={{
              margin: '24px 16px',
              padding: 24,
              minHeight: 610,
            }}
          >
        {/* Content Should be displayed */}
            <Route path="/" exact component={Home} />
            <Route path="/speaker" exact component={SpeakerList} />
            <Route path="/speaker/create" exact component={CreateSpeaker} />
          </Content>
        </Layout>
      </Layout>
    );
  }
}

// ReactDOM.render(<SiderDemo />, mountNode);
export default Dashboard;




