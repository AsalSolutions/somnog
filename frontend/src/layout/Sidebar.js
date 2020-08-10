import React from 'react';
import {connect} from 'react-redux';
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
        const dashboard = this.props.app.language === "EN" ? "Dashboard" : "Bogga Hore";
        const AddSpeaker = this.props.app.language === "EN" ? "Add Speakers" : "Diiwangali Speaker";
        const Speakers = this.props.app.language === "EN" ? "Speakers" : "Liiska SpeakersKa";
        const Speaker = this.props.app.language === "EN" ? "Speaker" : "Khudbo-jeediye"
        
        return (
        <Sider width="230" trigger={null} collapsible collapsed={this.props.collapsed}>
            <div className="logo" />
            <Link to="/"> <h1 style={{color:'white',paddingTop:"20px",paddingLeft:"20px",paddingBottom:"25px"}}>SOMNOG APP</h1></Link>
            <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
            <Menu.Item key="1" icon={<BarChartOutlined />}>
        <Link to="/">{dashboard}</Link>
            </Menu.Item>
            <SubMenu key="sub1" icon={<UserOutlined />} title={Speaker}>
                <Menu.Item key="2" icon={<UserOutlined />}>
                    <Link to="/speaker"> {Speakers}</Link>
                </Menu.Item>
                <Menu.Item key="3" icon={<UserAddOutlined />}>
        <Link to="/speaker/create"> {AddSpeaker}</Link>
                </Menu.Item>
                
            </SubMenu>
            </Menu>
        </Sider>
        );
        
      
    }
}




const mapStateToProps = state => {
    return { app: state.language };
  };
  
  
  
  export default connect(mapStateToProps)(Sidebar);
