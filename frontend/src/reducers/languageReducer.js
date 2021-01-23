import { SET_LANGUAGE } from '../constants/types';

export const languageReducer = (
  state = { language: localStorage.getItem('language') || 'SO' },
  action
) => {
  switch (action.type) {
    case SET_LANGUAGE:
      return { ...state, language: action.payload };
    default:
      return state;
  }
};
