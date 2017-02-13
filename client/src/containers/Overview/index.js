import React from 'react';
import Panel from '../../components/Panel';
import Dashboard from '../Dashboard';
import './Overview.css';

class Overview extends React.Component {
  render() {
    return (
    <div>
      <Dashboard />
      <div className="overview-container">
        <Panel />
      </div>
    </div>
    );
  }
}

export default Overview;