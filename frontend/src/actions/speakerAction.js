// import axios from "axios";
import api from "../api";
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
    const response = await api.get("/speakers");
    dispatch({ type: GET_SPEAKERS, payload: response.data });
  };
};

// Create Speaker
export const createSpeaker = (formValues) => {
  return async (dispatch) => {
    try {
<<<<<<< HEAD:frontend/src/actions/speakerAction.js
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
=======
      const response = await api.post("/speakers", {
        ...formValues,
      });
>>>>>>> frontend:frontend/src/actions/speaker.js
      dispatch({ type: CREATE_SPEAKER, payload: response.data });
      history.push("/speaker");
    } catch (e) {
      console.error(`Something went wrong: ${e}`);
    }
  };
};
