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
      const response = await api.post("/speakers", {
        ...formValues,
      });
      dispatch({ type: CREATE_SPEAKER, payload: response.data });
      history.push("/speaker");
    } catch (e) {
      console.error(`Something went wrong: ${e}`);
    }
  };
};

// Delete Speaker
export const deleteSpeaker = (id) => {
  return async (dispatch) => {
    try {
      await api.delete(`/speakers/${id}`);
      dispatch({ type: DELETE_SPEAKER, payload: id });
      history.push("/speaker");
    } catch (e) {
      console.error(`Something Went wrong: ${e}`);
    }
  };
};

// Update speaker
export const updateSpeaker = (id, formValues) => async dispatch => {
  const response = await api.put(`/speakers/${id}`, formValues);
  dispatch({ type: UPDATE_SPEAKER, payload: response.data });
  history.push("/speaker");
};

// Get a single speaker
// Get a sigle stream
export const getSpeaker = id => async dispatch => {
  const response = await api.get(`/speakers/${id}`);
  dispatch({ type: GET_SPEAKER, payload: response.data });
};
