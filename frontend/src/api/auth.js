import api from '@/api';

const signin_path = '/user/signin/';
const signup_path = '/user/signup/';
const userinfo_path = '/user/userinfo/';

export default {
  signIn(credentials, callback, callbackError) {
    api
    .post(signin_path, credentials)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  },
  signUp(credentials, callback, callbackError) {
    api
    .post(signup_path, credentials)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  },
  getUserInfo(callback, callbackError) {
    api
    .get(userinfo_path)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  }
}