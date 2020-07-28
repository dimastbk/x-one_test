import axios from 'axios';
import router from '@/router'

const api = axios.create({
  'baseURL': '/api/v1',
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: localStorage.getItem('token') ? `Token ${localStorage.getItem('token')}` : '',
  }
});

api.interceptors.response.use((response) => {
    return response;
  }, error => {
    if ((error.response.status === 500 && error.response.data.code === 'auth') || error.response.status === 400) {
      return Promise.reject(error);
    }
    let path = '/500';
    switch (error.response.status) {
      case 403: path = '/403'; break;
      case 404: path = '/404'; break;
    }
    router.push(path);
    return Promise.reject(error);
  });

export default api;
