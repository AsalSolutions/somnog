import axios from "axios";
// import api from "../api";
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
    // const response = await fetch("/v1/speaker");
    dispatch({ type: GET_SPEAKERS, payload: response.data });
  };
};

// Create Speaker
export const createSpeaker = (formValues) => {
  const formInput = { ...formValues };
  console.log(formInput);
  return async (dispatch) => {
    try {
      const options = {
        "Content-Type": "application/json",
      };
      const response = await axios.post(
        "http://localhost:5000/v1/speaker",
        {
          ...formValues,
        },
        { headers: options }
      );
      dispatch({ type: CREATE_SPEAKER, payload: response.data });
      // history.push("/speaker");
    } catch (e) {
      console.error(`Something went wrong: ${e}`);
    }
  };
};
