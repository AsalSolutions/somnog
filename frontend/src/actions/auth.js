// import { Redirect } from 'react-router-dom';
import { SIGN_IN, SIGN_OUT, USER_PROFILE } from '../constants/types';
import { api, authApi } from '../api';
import history from '../helpers/history';
// import { sucessAlert, errorAlert } from './alerts';

export const signIn = (formValues) => {
  return async (dispatch) => {
    try {
      // T0 Signin/login we need to send request to auth/login
      //?Email and Password is required to login
      const response = await api.post('/auth/login', {
        ...formValues,
      });

      if (response.data.success) {
        dispatch({ type: SIGN_IN, payload: response.data });
        // Store user token
        sessionStorage.setItem('token', response.data.access_token);
        if (response.data.role === 'User') {
          console.log('redirecting User Dashboard....');
          return history.push('/dashboard');
        }
        if (response.data.role === 'Admin') {
          return history.push('/admin');
        }
        console.log(response.data);
      } else {
        console.log(response.data.message);
        history.push('/');
      }
    } catch (e) {
      console.log(`Something Went Wrong ${e}`);
    }
  };
};

// Stackoverfollow

export const signOut = () => {
  return async (dispatch) => {
    try {
      //TODO 1: Check if user is signed in first
      if (sessionStorage.getItem('token')) {
        const response = await authApi.post('auth/logout/access');
        if (response.data.success) {
          dispatch({ type: SIGN_OUT, payload: response.data });
          sessionStorage.removeItem('token');
          history.push('/');
        }

        //TODO 2: Redirect User to Login Page
      } else {
        console.log('You need to sign in first to logout');
      }
    } catch (e) {
      console.log(`Something Went Wrong ${e}`);
    }
  };
};

export const getUserProfile = (userId) => {
  return async (dispatch) => {
    try {
      const response = await authApi.get(`users/${userId}`);
      if (response.data.success) {
        console.log(response.data);
        dispatch({ type: USER_PROFILE, payload: response.data });
      } else {
        console.log(response.data);
      }
    } catch (e) {
      console.log('Something went wrong' + e);
    }
  };
};
