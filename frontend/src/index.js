import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
