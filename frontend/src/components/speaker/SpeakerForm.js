import React, { Component } from "react";
import { Field, reduxForm } from "redux-form";

class SpeakerForm extends Component {
  //
  inputRender = (formProps) => {
    return (
      <div>
        <label>{formProps.label}</label>
        <input {...formProps.label} />
        {this.renderError(formProps.meta)}
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
  onSubmit = () => {
    this.props.onSubmit(formValues);
  };
  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit(this.onSubmit)}>
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
          />
          <Field
            name="socialAccount"
            component={this.inputRender}
            label="Social Account"
          />
        </form>
      </div>
    );
  }
}
