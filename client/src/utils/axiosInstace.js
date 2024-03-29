import axios from "axios";

const axiosInstance = axios.create({
  baseURL: import.meta.env["VITE_REACT_APP_API_URL"] + "/api",
});
axiosInstance.interceptors.request.use(
  function (config) {
    // Do something before request is sent
    return config;
  },
  function (error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // do something with response error
    return Promise.reject(error);
  }
);

export default axiosInstance;
