const API = '/api/';

export const apiRequestMap = {
  apiFetchProfileBlob({ profile }) {
    return {
      url: `${API}${profile}`
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
