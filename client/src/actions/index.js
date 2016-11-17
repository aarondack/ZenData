export const REQUEST_PROFILE_BLOB = 'REQUEST_PROFILE_BLOB';
export const RECEIVE_PROFILE_BLOB = 'RECEIVE_PROFILE_BLOB';

export function requestProfileBlob(profileName) {
  return {
    type: REQUEST_PROFILE_BLOB,
    profileName
  }
};

export function receiveProfileBlob(profile) {
  return {
    type: RECEIVE_PROFILE_BLOB,
    profile
  }
};
