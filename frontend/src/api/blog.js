import api from '@/api';

const blog_path = '/blog/';

export default {
  getAllPages(callback, callbackError) {
    api
    .get(blog_path)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  },
  getAllPagesInfo(callback, callbackError) {
    api
    .get(blog_path)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  },
  getPage(id, callback, callbackError) {
    api
    .get(`${blog_path}${id}/`)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  },
  postPage(payload, callback, callbackError) {
    if (payload.id) {    
      api
      .patch(`${blog_path}${payload.id}/`, payload)
      .then(response => callback(response))
      .catch(error => callbackError(error));
    } else {
      api
      .post(blog_path, payload)
      .then(response => callback(response))
      .catch(error => callbackError(error));
    }
  },
  deletePage(payload, callback, callbackError) {
    api
    .delete(blog_path, payload)
    .then(response => callback(response))
    .catch(error => callbackError(error));
  }
}