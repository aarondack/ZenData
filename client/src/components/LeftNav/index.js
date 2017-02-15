import React from 'react';
import './LeftNav.css';
import { Link, withRouter } from 'react-router';
import img from '../../public/Dashboard.png';

const HEADERS = ['Overview', 'Heroes', 'Achievements', 'Insights']

const LeftNav = ({ router }) => (
  <div className="container">
    <div className="leftNavTable">
      {HEADERS.map((value, key) =>
        <div key={value} className="item">
          <Link to={`/profile/${router.params.battlenet}/${value}`} className="link">
            <span className="option">{value}</span>
          </Link>
        </div>
      )}
    </div>
  </div>
);
export default withRouter(LeftNav);
