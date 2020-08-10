import React from 'react';
import {connect} from 'react-redux';
import {setLanguage} from '../actions/setLanguageAction'
import { Menu } from 'antd';
import {
    TranslationOutlined
  } from '@ant-design/icons';
const { SubMenu } = Menu;

 function LanguageDropDown({setLanguage,language}) {
    const handleClick = (e)=> { 
        // Save current language to local storage
        localStorage.setItem("language",e.key)
        // Updating Language State from Local Storage
        setLanguage(localStorage.getItem("language"))
    }
    return (
        
            <Menu mode="horizontal" onClick={handleClick}>
                <SubMenu icon={<TranslationOutlined />}>
                    <Menu.Item key="EN">English</Menu.Item>
                    <Menu.Item key="SO">Somali</Menu.Item>
                </SubMenu>
            </Menu>
       
    )
}





//  Languages
 const mapStateToProps = state => {
    return { language: state.language };
 };

 export default connect(mapStateToProps, setLanguage)(LanguageDropDown);

