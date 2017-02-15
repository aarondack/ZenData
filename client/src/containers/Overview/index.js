import React from 'react';
import Panel from '../../components/Panel';
import Dashboard from '../Dashboard';
import { connect } from 'react-redux';
import CircularProgress from 'material-ui/CircularProgress';
import './Overview.css';

class Overview extends React.Component {
  render() {
    const { fetching } = this.props;
    return (
    <div>
      <Dashboard />
      {
        fetching ? 
      <div className="loading">
        <h3>Loading...</h3>
        <CircularProgress size={80} thickness={5} />
      </div>
      : 
          <div className="overview-container">
          <Panel />
      </div>
      }
    </div>
    );
  }
}


const mapStateToProps = (state, ownProps) => {
  return {
    fetching: state.dashboard.fetching,
  }
}

export default connect(mapStateToProps, null)(Overview);