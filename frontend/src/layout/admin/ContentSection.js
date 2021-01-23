import React from 'react';
import { Layout } from 'antd';
import { Route, Router } from 'react-router-dom';
import SpeakerList from '../../components/speakers/SpeakerList';
import CreateSpeaker from '../../components/speakers/CreateSpeaker';
import UpdateSpeaker from '../../components/speakers/UpdateSpeaker';
import AdminDashboard from './Home';
import history from '../../helpers/history';

const { Content } = Layout;

function ContentSection() {
  return (
    <Content
      className="site-layout-background"
      style={{
        margin: '24px 16px',
        padding: 24,
        minHeight: 610,
      }}
    >
      <Router history={history}>
        {/* <Route path="/AdminDashboard" exact component={AdminDashboard} /> */}
        {/* Speaker Routes */}
        <Route path="AdminDashboard/speaker" exact component={SpeakerList} />
        <Route
          path="AdminDashboard/speaker/create"
          exact
          component={CreateSpeaker}
        />
        <Route
          path="AdminDashboard/speaker/edit/:id"
          exact
          component={UpdateSpeaker}
        />
      </Router>
    </Content>
  );
}

export default ContentSection;
