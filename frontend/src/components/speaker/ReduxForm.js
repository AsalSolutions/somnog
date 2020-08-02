import React, { Component } from "react";
import { Field, reduxForm } from "redux-form";
import { Form, Input, InputNumber, Button } from 'antd';


class SpeakerForm extends Component {
  //
  inputRender = (formProps) => {
    return (
      <div>
        <label>{formProps.label}</label>
        <input {...formProps.input} />
        <span>{this.renderError(formProps.meta)}</span>
      </div>
    );
  };
  // Render Errors only when touched
  renderError = ({ touched, error }) => {
    if (touched & error) {
      return error;
    }
  };

  // Handle form when submit btn is pressed
  submitValues = (formValues) => {
    this.props.onSubmit(formValues);
    console.log(formValues)
  };

  render() {
    return (
      <div>
        <form onSubmit={this.props.handleSubmit(this.submitValues)}>
          <Field
            name="firstName"
            component={this.inputRender}
            label="FirstName"
          />
          <Field
            name="lastName"
            component={this.inputRender}
            label="LastName"
          />
          <Field name="email" component={this.inputRender} label="Email" />
          <Field name="phone" component={this.inputRender} label="Phone" />
          <Field
            name="companyName"
            component={this.inputRender}
            label="Company"
          />
          <Field
            name="jobTitle"
            component={this.inputRender}
            label="Job Title"
          />
          <Field
            name="description"
            component={this.inputRender}
            label="Description"
          />{" "}
          <Field name="photo" component={this.inputRender} label="Photo Url" />
          <Field
            name="socialAccount"
            component={this.inputRender}
            label="Social Account"
          />
          <button>Add Speaker</button>
        </form>
      </div>
    );
  }
}

const validateForm = (formValues) => {
  const errors = {};
  if (!formValues.firstName) {
    errors.firstName = "FirstName is required";
  }
  if (!formValues.lastName) {
    errors.lastName = "LastName is required";
  }
  if (!formValues.email) {
    errors.email = "Email is required";
  }
  if (!formValues.phone) {
    errors.phone = "Phone is required";
  }
  return errors;
};

export default reduxForm({
  form: "speakerForm",
  validate: validateForm,
})(SpeakerForm);




