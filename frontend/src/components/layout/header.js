import React from "react";
import { Link } from "react-router-dom";

function Header() {
  return (
    <div>
      <ul>
        <li>
          <Link to="/"> Home</Link>
        </li>
        <li>
          <Link to="/speaker"> Speakers</Link>
        </li>
        <li>
          <Link to="/speaker/create"> Add Speaker</Link>
        </li>
      </ul>
    </div>
  );
}

export default Header;
