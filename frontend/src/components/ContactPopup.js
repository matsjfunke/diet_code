import React from "react";
import "./ContactPopup.css";

function ContactPopup({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="popup-overlay">
      <div className="popup-content">
        <button className="close-button" onClick={onClose}>
          &times;
        </button>
        <h2>Contact Me</h2>
        <ul className="contact-list">
          <li>
            <a href="mailto:mats.funke@gmail.com">Email</a>
          </li>
          <li>
            <a
              href="https://twitter.com/matsjfunke13"
              target="_blank"
              rel="noopener noreferrer"
            >
              Twitter
            </a>
          </li>
          <li>
            <a
              href="https://www.linkedin.com/in/matsjfunke"
              target="_blank"
              rel="noopener noreferrer"
            >
              LinkedIn
            </a>
          </li>
          <li>
            <a
              href="https://github.com/matsjfunke"
              target="_blank"
              rel="noopener noreferrer"
            >
              GitHub
            </a>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default ContactPopup;
