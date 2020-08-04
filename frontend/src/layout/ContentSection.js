import React from 'react';
import { Layout } from 'antd';
import { Route } from "react-router-dom";
import SpeakerList from "../components/speaker/SpeakerList";
import CreateSpeaker from "../components/speaker/CreateSpeaker";
import UpdateSpeaker from "../components/speaker/UpdateSpeaker";
import DeleteSpeaker from "../components/speaker/DeleteSpeaker";
import Home from "./pages/Home";


const { Content } = Layout;

function ContentSection(){
  return (
    <Content
            className="site-layout-background"
            
            style={{
              margin: '24px 16px',
              padding: 24,
              minHeight: 610,
              
            }}>
    
            <Route path="/" exact component={Home} />
            {/* Speaker Routes */}
            <Route path="/speaker" exact component={SpeakerList} />
            <Route path="/speaker/create" exact component={CreateSpeaker} />
            <Route path="/speaker/edit/:id" exact component={UpdateSpeaker} />
            <Route path="/speaker/delete/:id" exact component={DeleteSpeaker} />
    </Content>
  )
    
}

export default ContentSection;