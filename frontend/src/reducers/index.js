import { combineReducers } from "redux";
import { reducer as formReducer } from "redux-form";
import { speakerReducer } from "./speakerReducer";
export default combineReducers({
  form: formReducer,
  speakers: speakerReducer,
});
