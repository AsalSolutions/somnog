import { USER_PROFILE } from '../constants/types';

const INITIAL_STATE = {
  id: null,
  email: null,
  role: null,
  username: null,
  errors: null,
};

export const userProfileReducer = (state = INITIAL_STATE, actions) => {
  switch (actions.type) {
    case USER_PROFILE:
      return {
        ...state,
        id: actions.payload.id,
        email: actions.payload.email,
        username: actions.payload.username,
        role: actions.payload.role,
      };

    default:
      return state;
  }
};
