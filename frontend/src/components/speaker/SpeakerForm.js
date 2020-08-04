import React from "react"; 
import { Form, Input, InputNumber, Button } from 'antd';

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
const validateMessages = {
  required: '${label} is required!',
  types: {
    email: '${label} is not valid email!',
    number: '${label} is not a valid number!',
  },
  phone: {
    range: '${label} must be between ${min} and ${max}',
  },
};

const  SpeakerForm = ({onSubmit,initialValues}) => {
  const submitValues = (formValues) => {
    onSubmit(formValues);
    console.log(formValues)
  };

  return (
    <Form {...layout} name="nest-messages" onFinish={submitValues} validateMessages={validateMessages} initialValues={initialValues}>
      <Form.Item
        name={'firstName'}
        label="First Name"
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
        label="Last Name"
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
        label="Company"
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
        label="Title"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>
      
      <Form.Item name={'description'} label="Description">
        <Input.TextArea />
      </Form.Item>
      <Form.Item name={'photo'} label="Photo URL">
        <Input />
      </Form.Item>
      <Form.Item name={'socialAccount'} label="Website">
        <Input />
      </Form.Item>
      <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};


export default SpeakerForm;
  