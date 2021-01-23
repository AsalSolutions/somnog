import React from 'react';
import { Layout } from 'antd';
import { Route, Router } from 'react-router-dom';
import Dashboard from './index';
import history from '../../helpers/history';

const { Content } = Layout;

function Routes() {
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
        {/* <Route path="/landing" exact component={Dashboard} /> */}
        {/* Speaker Routes */}
        {/* <Route path="/speaker" exact component={SpeakerList} />
        <Route path="/speaker/create" exact component={CreateSpeaker} />
        <Route path="/speaker/edit/:id" exact component={UpdateSpeaker} /> */}
      </Router>
    </Content>
  );
}

export default Routes;
