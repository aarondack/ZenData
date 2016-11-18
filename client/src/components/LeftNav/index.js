import React from 'react';
import './LeftNav.css';

const HEADERS = ['Overview', 'Heroes', 'Achievements', 'Insights']

const LeftNav = () => (
  <div className="container">
    <div className="leftNavTable">
      {HEADERS.map(value =>
        <div className="item">
          <span className="option">{value}</span>
        </div>
      )}
    </div>
  </div>
);

export default LeftNav;
