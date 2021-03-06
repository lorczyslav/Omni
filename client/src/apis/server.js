import axios from "axios";

const Server = axios.create({
  baseURL: `http://${process.env.REACT_APP_CURRENT_IP}:8000/api`
});

export default Server;
