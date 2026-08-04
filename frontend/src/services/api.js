import axios from "axios";

const api = axios.create({
  baseURL: "https://the-contrarian-api.onrender.com",
});

export default api;