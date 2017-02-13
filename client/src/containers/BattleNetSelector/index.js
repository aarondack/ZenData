import React from 'react';
import Paper from 'material-ui/Paper';
import './BattleNetSelector.css';
import { Link } from 'react-router';

class BattleNetSelect extends React.Component {
  state = {
    username: '',
  };

  onChange = event => {
    this.setState({ 
      username: event.target.value,
    });
  };

  render() {
    const { username } = this.state;
    return (
      <div className="selector-container">
        <div className="image-holder">
          <div className="selector-image"/>
          <h2 className="zenData">ZenData</h2>
        </div>
        <div className="input-holder">
        <div className="icon" />        
        <Paper>
          <input 
            type="text" 
            placeholder={'Input your Battlenet ID'} 
            className="battlnet-input" 
            onChange={this.onChange}
          />                          
        </Paper>
          <Link to={`/profile/${username}`}>
            <button className="search-button">Search</button>
          </Link>
        </div>
      </div>
    );
  };
};

  export default BattleNetSelect;
