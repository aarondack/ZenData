import React from 'react';
import './LeftNav.css';
import img from '../../public/Dashboard.png';

const HEADERS = ['Overview', 'Heroes', 'Achievements', 'Insights']

const LeftNav = () => (
  <div className="container">
    <div className="leftNavTable">
      {HEADERS.map((value, key) =>
        <div key={value} className="item">
          <span className="option">{value}</span>
        </div>
      )}
    <img src={img} />
    </div>
  </div>
);

export default LeftNav;
