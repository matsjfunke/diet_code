/*
api.js creates an Axios instance named api with a base URL specified in the docker-compose file
-> which can be imported / used throughout the frontend app to send HTTP requests to the specified server.
*/
import axios from "axios";

// Create an Axios instance
const api = axios.create({
    baseURL: process.env.REACT_APP_BACKEND_BASE_URL,
    headers: {
        "Content-Type": "application/json",
    },
});

export default api;
