import mapKeys from "lodash/mapKeys";
import {
  CREATE_SPEAKER,
  DELETE_SPEAKER,
  UPDATE_SPEAKER,
  GET_SPEAKER,
  GET_SPEAKERS,
} from "../actions/types";

export const speakerReducer = (state = {}, action) => {
  switch (action.type) {
    case CREATE_SPEAKER:
      return { ...state, [action.payload.id]: [action.payload] };
    case GET_SPEAKERS:
      return { ...state, ...mapKeys(action.payload, "_id") };

    default:
      return state;
  }
};
