import { SIGN_IN, SIGN_OUT } from '../constants/types';

const INITIAL_STATE = {
  isSignedIn: false,
  role: null,
  accessToken: null,
  refreshToken: null,
  errors: null,
};

export const authReducer = (state = INITIAL_STATE, actions) => {
  switch (actions.type) {
    case SIGN_IN:
      return {
        ...state,
        isSignedIn: true,
        role: actions.payload.role,
        accessToken: actions.payload.access_token,
        refreshToken: actions.payload.refresh_token,
      };
    case SIGN_OUT:
      // We're clearing information if user information if signedOut
      return {
        ...state,
        isSignedIn: false,
        role: null,
        accessToken: '',
        refreshToken: '',
      };
    default:
      return state;
  }
};
