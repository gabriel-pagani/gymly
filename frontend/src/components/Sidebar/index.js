import React from "react";
import "../../styles/sidebar.css";

function Sidebar() {
  return (
    <div id="sidebar">
      <div id="top"></div>
      <div className="divider" />
      <nav id="menu"></nav>
      <div className="divider" />
      <div id="bottom"></div>
    </div>
  );
}

export default Sidebar;
