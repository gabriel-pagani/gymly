import React from "react";
import "../../styles/home.css";
import Sidebar from "../../components/Sidebar";

function Home() {
  return (
    <>
      <Sidebar />
      <iframe id="dashboard"/>
    </>
  );
}

export default Home;
