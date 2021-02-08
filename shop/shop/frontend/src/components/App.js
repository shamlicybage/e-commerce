import React from "react";
import { render } from "react-dom";

function App() {
  return <h1>Shamli</h1>;
}

export default App;
const container = document.getElementById("app");
render(<App />, container || document.createElement("div"));
