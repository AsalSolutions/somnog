import mapKeys from 'lodash/mapKeys';
import omit from 'lodash/omit';

import {
  CREATE_SPEAKER,
  DELETE_SPEAKER,
  UPDATE_SPEAKER,
  GET_SPEAKER,
  GET_SPEAKERS,
} from '../actions/types';

export const speakerReducer = (state = {}, action) => {
  switch (action.type) {
    case CREATE_SPEAKER:
      return { ...state, [action.payload.id]: [action.payload] };
    case GET_SPEAKERS:
      return { ...state, ...mapKeys(action.payload, 'id') };
    case GET_SPEAKER:
      return { ...state, [action.payload.id]: action.payload };
    case DELETE_SPEAKER:
      return omit(state, action.payload);
    case UPDATE_SPEAKER:
      return { ...state, [action.payload.id]: action.payload };
    // case SPEAKER_COUNT:
    //   return {...state, [action.payload.speakerCount]:action.payload}

    default:
      return state;
  }
};
