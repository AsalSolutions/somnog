import React from 'react';
import { Link  } from "react-router-dom";
import { Layout, Menu } from 'antd';
import {
    
    UserOutlined,
    UserAddOutlined,
    BarChartOutlined
  } from '@ant-design/icons';

const {  Sider  } = Layout;
const { SubMenu} = Menu;
class Sidebar extends React.Component {
    render(){
        return (
        <Sider trigger={null} collapsible collapsed={this.props.collapsed}>
            <div className="logo" />
            <Link to="/"> <h1 style={{color:'white',paddingTop:"20px",paddingLeft:"20px",paddingBottom:"25px"}}>SOMNOG APP</h1></Link>
            <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
            <Menu.Item key="1" icon={<BarChartOutlined />}>
            <Link to="/">Dashboard</Link>
            </Menu.Item>
            <SubMenu key="sub1" icon={<UserOutlined />} title="Speaker">
                <Menu.Item key="2" icon={<UserOutlined />}>
                    <Link to="/speaker"> Speakers</Link>
                </Menu.Item>
                <Menu.Item key="3" icon={<UserAddOutlined />}>
                    <Link to="/speaker/create"> Add Speaker</Link>
                </Menu.Item>
                
            </SubMenu>
            </Menu>
        </Sider>
        );
        
      
    }
}

export default Sidebar;