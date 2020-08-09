import { combineReducers } from "redux";
import { speakerReducer } from "./speakerReducer";
import {languageReducer} from './languageReducer'
export default combineReducers({
  language: languageReducer,
  speakers: speakerReducer,
});
