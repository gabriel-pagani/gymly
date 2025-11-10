import React, { useState, useEffect } from "react";
import "../../styles/sidebar.css";

function Sidebar() {
  const [sectors, setSectors] = useState([]);
  const menuItemsData = ["Portal de Administração", "Sair"];

  useEffect(() => {
    fetch("/api/dashboards/sectors/")
      .then((response) => response.json())
      .then((data) => {
        const sectorsArray = Object.keys(data).map((sector) => ({
          id: sector,
          dashboards: data[sector],
        }));
        setSectors(sectorsArray);
      });
  }, []);

  return (
    <aside id="sidebar">
      <header id="top">
        <div id="logo">
          <a href="/">
            <img alt="Logo Grupo SMI" src="/path/to/logo.png" />
          </a>
        </div>
      </header>

      <div className="divider" />

      <nav id="menu">
        <div id="search-bar"></div>
        <ul id="sectors-list">
          {sectors.map((sector) => (
            <li key={sector.id} className="sector">
              {sector.id}
              <ul className="dashboards-list">
                {Array.isArray(sector.dashboards) ? (
                  sector.dashboards.map((dashboard) => (
                    <li key={dashboard.id} className="dashboard">
                      {dashboard.title}
                    </li>
                  ))
                ) : null}
              </ul>
            </li>
          ))}
        </ul>
      </nav>

      <div className="divider" />

      <footer id="bottom">
        <div id="user-menu">
          user.name
          <ul id="user-menu-list">
            {menuItemsData.map((item) => (
              <li key={item} className="user-menu-item">
                {item}
              </li>
            ))}
          </ul>
        </div>
        <div id="toggle-button">=</div>
      </footer>
    </aside>
  );
}

export default Sidebar;
