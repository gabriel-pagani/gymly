import React from "react";
import "../../styles/home.css";
import Sidebar from "../../components/Sidebar";

function Home() {
  return (
    <>
      <Sidebar />
      {/* <iframe id="dashboard" title="" src=""></iframe> */}
      <div id="dashboard-placeholder">
        <h1>Bem Vindo ao Portal de Dashboards!</h1>
        <p>Selecione os dashboards no painel lateral ao lado</p>
      </div> 
    </>
  );
}

export default Home;
