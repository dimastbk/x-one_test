import api from '@/api';

const user_path = '/user/';
const delete_all_pages_path = '/delete_all_pages/';

export default {
  getAllUser(callback, callbackError) {
    api
    .get(user_path)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  },
  blockUser(id, callback, callbackError) {
    api
    .patch(`${user_path}${id}/`, {is_active: false})
    .then(response => callback(response))
    .catch(error => callbackError(error));
  },
  deleteUserPages(id, callback, callbackError) {
    api
    .delete(`${user_path}${id}${delete_all_pages_path}`)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  }

}