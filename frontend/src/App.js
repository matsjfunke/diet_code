import React, { useState } from "react";
import { Route, Routes, Navigate } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import ContactPopup from "./components/ContactPopup";
import Home from "./pages/Home";
import Why from "./pages/Why";
import Taste from "./pages/Taste";

function App() {
    const [isContactPopupOpen, setIsContactPopupOpen] = useState(false);

    const openContactPopup = () => setIsContactPopupOpen(true);
    const closeContactPopup = () => setIsContactPopupOpen(false);
    return (
        <div className="App">
            <Navbar />
            <Routes>
                <Route path="/" element={<Navigate to="/home" />} />
                <Route path="/home" element={<Home />} />
                <Route path="/why" element={<Why />} />
                <Route path="/taste" element={<Taste />} />
            </Routes>
            <ContactPopup isOpen={isContactPopupOpen} onClose={closeContactPopup} />
            <Footer onContactClick={openContactPopup} />
        </div>
    );
}

export default App;
