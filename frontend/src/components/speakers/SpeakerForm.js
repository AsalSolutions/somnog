import React from "react"; 
import {connect} from 'react-redux';
import { Form, Input, Button } from 'antd';

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};

// we need this fields 
// LastName
// Email
// Phone
// Company
// Job Title
// Description
// Photo Url
// Social Account


const  SpeakerForm = ({onSubmit,initialValues,app}) => {

  const validateMessages = {
    required: app.language === 'English' ?  '${label} is required!' : '${label} Waa loo baahanyahay!',
    types: {
      email: '${label} is not valid email!',
      number: '${label} is not a valid number!',
    },
    phone: {
      range: '${label} must be between ${min} and ${max}',
    },
  };

  const submitValues = (formValues) => {
    onSubmit(formValues);
    console.log(formValues)
    
  };
  
  // Form Fields Translation
  const firstName  = app.language === 'EN' ? "First Name" : "Magaca Koobaad";
  const lastName = app.language === "EN" ? "Last Name" : "Magaca Labaad";
  const companyName  = app.language === 'EN' ? "Company Name" : "Magaca Shirkadda";
  const jobTitle  = app.language === 'EN' ? "Job Title" : "Xilka Shaqo";
  const photo = app.language === "EN" ? "Photo " : "Gali Sawir";
  const description  = app.language === 'EN' ? "Description" : "Faah Faahin";
  const submit = app.language === 'EN' ? "Submit" : "Dir";
 

  return (
   
    <Form {...layout} name="nest-messages" onFinish={submitValues} validateMessages={validateMessages} initialValues={initialValues}>
      <Form.Item
        name={'firstName'}
        label={firstName}
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>
      <Form.Item
        name={'lastName'}
        label={lastName}
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>
      <Form.Item
        name={'email'}
        label="Email"
        rules={[
          {
            type: 'email',
          },
        ]}
      >
        <Input />
      </Form.Item>
      <Form.Item
        name={'phone'}
        label="Phone"
       
      >
        <Input />
      </Form.Item>
      <Form.Item
        name={'companyName'}
        label={companyName}
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>
      <Form.Item
        name={'jobTitle'}
        label={jobTitle}
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>
      
      <Form.Item name={'description'} label={description}>
        <Input.TextArea />
      </Form.Item>
      <Form.Item name={'photo'} label={photo}>
        <Input />
      </Form.Item>
      <Form.Item name={'socialAccount'} label="Website">
        <Input />
      </Form.Item>
      <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
        <Button type="primary" htmlType="submit">
          {submit}
        </Button>
      </Form.Item>
    </Form>
  );
};

const mapStateToProps = state => {
  return { app: state.language };
};



export default connect(mapStateToProps)(SpeakerForm);
  