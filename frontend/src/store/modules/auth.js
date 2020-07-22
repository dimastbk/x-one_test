import auth from '@/api/auth';

const state = () => ({
  authToken: localStorage.getItem('token') || '',
  userInfo: {},
  signInError: null,
  signUpError: null,
})

const getters = {
  isAuthenticated: state => !!state.authToken,
  isAdmin: state => state.userInfo.is_staff,
}

const actions = {
  signIn ({ commit, dispatch }, { credentials, callbackError }) {
    commit('removeAuthToken');
    commit('removeError');
    auth.signIn(
      credentials,
      response => {
        commit('setAuthToken', response.data.token);
        dispatch('updateUserInfo');
      },
      error => {
        commit('setSignInError', error.response.data.detail);
        callbackError(error);
      }
    )
  },
  signUp ({ commit, dispatch }, { credentials, callbackError }) {
    commit('removeAuthToken');
    commit('removeError');
    auth.signUp(
      credentials,
      response => {
        commit('setAuthToken', response.data.token);
        dispatch('updateUserInfo');
      },
      error => {
        commit('setSignUpError', error.response.data.detail);
        callbackError(error);
      }
    )
  },
  signOut ({ commit }) {
    commit('removeAuthToken');
    commit('setUserInfo', {});
    // TODO logout на сервере?
  },
  updateUserInfo({ commit, state }) {
    if (!state.authToken) {
      return;
    }
    auth.getUserInfo(
      response => commit('setUserInfo', response.data),
      error => {
        commit('setUserInfo', {});
        console.log(error);
      }
    )
  }
}
const mutations = {
  removeAuthToken (state) {
    localStorage.removeItem('token');
    state.authToken = null;
  },
  setAuthToken (state, token) {
    localStorage.setItem('token', token);
    state.authToken = token;
  },
  removeError (state) {
    state.signInError = null;
    state.signUpError = null;
  },
  setSignInError (state, error) {
    state.signInError = error;
  },
  setSignUpError (state, error) {
    state.signUpError = error;
  },
  setUserInfo(state, userinfo) {
    state.userInfo = userinfo;
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}