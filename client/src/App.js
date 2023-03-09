import React, { useState, useEffect } from "react";
import './App.css';

function App() {
  const [currentDate, setCurrentDate] = useState("");
  const [currentTime, setCurrentTime] = useState("");
  const [menu, setMenu] = useState({
    random_leves: "",
    random_foetel: "",
    random_desszert: "",
  });

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("/current-date")
        .then((response) => response.text())
        .then((data) => setCurrentDate(data));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("/current-time")
        .then((response) => response.text())
        .then((data) => setCurrentTime(data));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const generateMenu = async () => {
    const menuResponse = await fetch("/menu");
    const menuData = await menuResponse.json();
    setMenu(menuData);
  };

  const { random_leves, random_foetel, random_desszert } = menu;

  return (
    <div className="container">
      <div className="header">
        <button className="title" onClick={generateMenu}>Mit együnk ma?</button>
        <h3 className="date">
          Budapest - {currentDate} - {currentTime}
        </h3>
      </div>
      <div className="row">
        <div className="column">
          <h2 className="subtitle">Leves</h2>
          <p>{menu.random_leves}</p>
        </div>
        <div className="separator"></div>
        <div className="column">
          <h2 className="subtitle">Főétel</h2>
          <p>{menu.random_foetel}</p>
        </div>
        <div className="separator"></div>
        <div className="column">
          <h2 className="subtitle">Desszert</h2>
          <p>{menu.random_desszert}</p>
        </div>
      </div>
    </div>
  );
}

export default App;
