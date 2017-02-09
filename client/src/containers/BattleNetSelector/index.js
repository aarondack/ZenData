import React from 'react';
import Paper from 'material-ui/Paper';
import './BattleNetSelector.css';

class BattleNetSelect extends React.Component {
  render() {
    return (
      <div className="selector-container">
        <div className="image-holder">
          <div className="selector-image"/>
          <h2 className="zenData">ZenData</h2>
        </div>
        <div className="input-holder">
        <div className="icon" />        
        <Paper>
          <input type="text" placeholder={'Input your Battlenet ID'} className="battlnet-input" />                          
        </Paper>
        </div>
      </div>
    );
  };
};

  export default BattleNetSelect;
