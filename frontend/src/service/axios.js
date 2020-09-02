import axios from "axios";
import LocalStorageService from "./LocalStorageService";
const localStorageService = LocalStorageService.getService();

// Set config defaults when creating the instance
const instance = axios.create({
    baseURL: 'http://localhost:8000/api/v1'
});
  
// Alter defaults after instance has been created
instance.defaults.headers.post['Content-Type'] = 'application/json';

instance.interceptors.request.use(request => {
    console.log(request);
    const token = localStorageService.getAccessToken();
    if (token) {
        request.headers['Authorization'] = 'Bearer ' + token;
    }
    return request;
}, error => {
    console.log(error);
    return Promise.reject(error);
});

instance.interceptors.response.use(response => {
    console.log(response);
    // Edit response config
    return response;
}, error => {
    console.log(error);
    return Promise.reject(error);
});

export default instance;