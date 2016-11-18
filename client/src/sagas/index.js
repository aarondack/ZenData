import { take, put, call, fork } from 'redux-saga/effects';
import fetch from 'isomorphic-fetch';
import * as actions from '../actions';
import {apiRequestMap} from '../actions/api';

export function fetchOverwatcher(type, data) {
    const apiRequestConfiguration = apiRequestMap[type](data);
    return fetch(apiRequestConfiguration.url).then(res => {
        if (res.status >= 400) {
            return res.json().then(err => {
                throw err;
            });
        }
        return res.json();
    })
}

export function* watchFetchProfile() {
  while(true) {
    const { profileName } = yield take(actions.REQUEST_PROFILE_BLOB);
    yield call(fetchProfile, profileName);
  }
}

export function* fetchProfile(profileName) {
  const profileData = yield call(fetchOverwatcher, 'apiFetchProfileBlob', { profileName });
  yield put(actions.receiveProfileBlob(profileData));
}

export default function* rootSaga() {
  yield [
    fork(watchFetchProfile)
  ]
};
