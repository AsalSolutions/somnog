/* eslint-disable no-template-curly-in-string */
import React from 'react';
import { connect } from 'react-redux';
import { Form, Input, Button } from 'antd';
import { signIn } from '../../actions/auth';
// import tokenDecoder from '../../helpers/tokenDecoder';
// import { Redirect } from 'react-router-dom';

// const { token, userRole } = tokenDecoder();

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};

const RegisterForm = ({ initialValues, app, signIn }) => {
  return <h1>Register Page</h1>;
};

const mapStateToProps = (state) => {
  return { app: state.language, user: state.auth };
};

export default connect(mapStateToProps, { signIn })(RegisterForm);
