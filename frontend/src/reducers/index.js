import { combineReducers } from 'redux';
import { speakerReducer } from './speakerReducer';
import { languageReducer } from './languageReducer';
import { authReducer } from './authReducer';
import { userProfileReducer } from './userProfileReducer';
export default combineReducers({
  language: languageReducer,
  speakers: speakerReducer,
  auth: authReducer,
  userProfile: userProfileReducer,
});
