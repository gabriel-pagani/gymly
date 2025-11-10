import React from "react";
import "../../styles/sidebar.css";

const sectorsData = [
  { id: "sector-1", dashboards: ["dash-1-1", "dash-1-2"] },
  { id: "sector-2", dashboards: ["dash-2-1", "dash-2-2"] },
  { id: "sector-3", dashboards: ["dash-3-1", "dash-3-2"] },
];

const menuItemsData = ["item-1", "item-2"];

function Sidebar() {
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
          {sectorsData.map((sector) => (
            <li key={sector.id} className="sector">
              {sector.id}
              <ul className="dashboards-list">
                {sector.dashboards.map((dashboard) => (
                  <li key={dashboard} className="dashboard">
                    {dashboard}
                  </li>
                ))}
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
