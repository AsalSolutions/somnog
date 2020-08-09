import {
    SET_LANGUAGE
    
  } from "./types";

// Set Language Action
export const setLanguage = dispatch => ({
    setLanguage: language => dispatch({ type: SET_LANGUAGE, payload: language })
 });
