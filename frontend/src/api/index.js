import axios from 'axios';

const baseURL = 'http://localhost:5000/api/v1.0/';
export const api = axios.create({
  baseURL,
});

export const authApi = axios.create({
  baseURL,
  headers: {
    Authorization: 'Bearer ' + sessionStorage.getItem('token'),
  },
});
