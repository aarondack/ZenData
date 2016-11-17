import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';

const initialState = {
  profile: [],
  fetching: false
};

export const dashboardReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'REQUEST_PROFILE_BLOB':
      return {
        ...state,
        fetching: true
      }
    case 'RECEIVE_PROFILE_BLOB':
      return {
        ...state,
        profile: action.profile,
        fetching: false
      }
    default:
      return state;
  }
}

const rootReducer = combineReducers({
  dashboardReducer,
  routing: routerReducer
});

export default rootReducer;
