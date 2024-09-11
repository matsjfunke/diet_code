// components/Footer.js
import React from "react";
import "./Footer.css";

function Footer({ onContactClick }) {
    return (
        <footer className="footer">
            <p className="footer-text">
                &copy; 2024 matsjfunke. All rights reserved.
            </p>
            <button onClick={onContactClick} className="contact-button">
                Contact
            </button>
        </footer>
    );
}

export default Footer;
