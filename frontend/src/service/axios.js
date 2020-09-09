import axios from "axios";
import LocalStorageService from "./LocalStorageService";
import { BASE_URL } from "../utils/constant"; 

const localStorageService = LocalStorageService.getService();

// Set config defaults when creating the instance
const instance = axios.create({
    baseURL: BASE_URL
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
    if(error?.response?.status === 401) {
        localStorageService.clearToken(); 
        window.history.go();  
    }
    return Promise.reject(error);
});

export default instance;