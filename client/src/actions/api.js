const API = '/api/';

export const apiRequestMap = {
  apiFetchProfileBlob({ profileName }) {
    return {
      url: `${API}${profileName}/en-us`
    }
  },
  apiFetchTopHeroe({ profile }) {
    return {
      url: `${API}${profile}/topheroes`
    }
  },
  apiFetchAchievements({ profile }) {
    return {
      url: `${API}${profile}/achievements`
    }
  }
}
