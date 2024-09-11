import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { TypeAnimation } from "react-type-animation";
import "./Home.css";
import sodaCan from "../assets/soda-can-no-bg.png";

function Home() {
  const [isWiderThanTall, setIsWiderThanTall] = useState(false);

  useEffect(() => {
    const checkAspectRatio = () => {
      setIsWiderThanTall(window.innerWidth > window.innerHeight);
    };

    // Check on mount
    checkAspectRatio();

    // Add event listener for window resize
    window.addEventListener("resize", checkAspectRatio);

    // Cleanup
    return () => window.removeEventListener("resize", checkAspectRatio);
  }, []);

  return (
    <div className="home-container">
      <div className="content-wrapper">
        <h1 className="header huge">DIET CODE</h1>
        <h3 className="sub-header">
          <TypeAnimation
            sequence={["Don't be scared to delete, embrace it!", 1000]}
            wrapper="span"
            speed={25}
            style={{ display: "inline-block" }}
            repeat={1}
            cursor={false}
          />
        </h3>
        <main className="home-content">
          {isWiderThanTall && (
            <img src={sodaCan} alt="Soda Can" className="soda-can-image" />
          )}
          <blockquote>
            "Always code as if the guy who ends up maintaining your code will be
            a violent psychopath who knows where you live." ~ Martin Golding
          </blockquote>
          <div className="button-container">
            <Link to="/why" className="button">
              Why Diet Code?
            </Link>
            <Link to="/taste" className="button">
              Taste Diet Code
            </Link>
          </div>
        </main>
      </div>
    </div>
  );
}

export default Home;
