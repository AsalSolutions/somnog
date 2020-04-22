import axios from "axios";
import history from "../history";

import {
  CREATE_SPEAKER,
  DELETE_SPEAKER,
  UPDATE_SPEAKER,
  GET_SPEAKER,
  GET_SPEAKERS,
} from "./types";

// Get all speakers
export const getSpeakers = () => {
  return async (dispatch) => {
    const response = await axios.get("/v1/speaker");
    dispatch({ type: GET_SPEAKERS, payload: response.data });
  };
};
