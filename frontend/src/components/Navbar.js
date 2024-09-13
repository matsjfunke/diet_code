import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css"; // Import CSS for styling
import logo from "../assets/red-soda-can.png";

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/home" className="logo">
        <img src={logo} alt="Logo" className="logo-image" />
      </Link>
      <Link to="/home" className="diet-code-link">
        Diet Code
      </Link>
      <div className="nav-links">
        <Link to="/why">Open Can</Link>
        <Link to="/taste">Taste it</Link>
      </div>
    </nav>
  );
}

export default Navbar;
