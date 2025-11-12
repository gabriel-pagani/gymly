import React, { useState } from "react";
import "../../styles/home.css";
import Sidebar from "../../components/Sidebar";

function Home() {
  const [selectedUrl, setSelectedUrl] = useState(null);

  return (
    <>
      <Sidebar onSelectDashboard={setSelectedUrl} />
      {selectedUrl ? (
        <iframe id="dashboard" title="Dashboard" src={selectedUrl}></iframe>
      ) : (
        <div id="dashboard-placeholder">
          <h1>Bem Vindo ao Portal de Dashboards!</h1>
          <p>Selecione os dashboards no painel lateral ao lado</p>
        </div>
      )}
    </>
  );
}

export default Home;
