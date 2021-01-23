/* eslint-disable no-template-curly-in-string */
import React from 'react';
import { connect } from 'react-redux';
import { Form, Input, Button } from 'antd';
import { signIn } from '../../actions/auth';

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};

const LoginForm = ({ initialValues, app, signIn }) => {
  const validateMessages = {
    required:
      app.language === 'EN'
        ? '${label} is required!'
        : '${label} Waa loo baahanyahay!',
    types: {
      email: '${label} is not valid email!',
      number: '${label} is not a valid number!',
    },
  };

  //   const submitValues = (formValues) => {
  //     onSubmit(formValues);
  //   };
  const onSubmitHandler = (formValues) => {
    signIn(formValues);
    console.log(formValues);
  };

  // Form Fields Translation
  const email = app.language === 'EN' ? 'Email' : 'Gali Emailkaaga';
  const password =
    localStorage.getItem('language') === 'EN'
      ? 'Password'
      : 'Gali Lamber sireedkaaga';

  const submit = app.language === 'EN' ? 'Submit' : 'Dir';

  return (
    <Form
      {...layout}
      name="nest-messages"
      onFinish={onSubmitHandler}
      validateMessages={validateMessages}
      initialValues={initialValues}
    >
      <Form.Item
        name={'email'}
        label={email}
        rules={[
          {
            type: 'email',
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>
      <Form.Item
        name={'password'}
        label={password}
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        wrapperCol={{
          ...layout.wrapperCol,
          offset: 8,
        }}
      >
        <Button type="primary" htmlType="submit">
          {submit}
        </Button>
      </Form.Item>
    </Form>
  );
};

const mapStateToProps = (state) => {
  return { app: state.language };
};

export default connect(mapStateToProps, { signIn })(LoginForm);
