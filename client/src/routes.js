import React from 'react';
import {Route, IndexRoute, IndexRedirect} from 'react-router';
import Dashboard from './containers/Dashboard';
import BattleNetSelector from './containers/BattleNetSelector';
import App from './containers/App';
import Overview from './containers/Overview';

export default(
  <Route>
    <Route path="/" component={App}>
      <IndexRoute component={BattleNetSelector}/>
    </Route>
    <Route path="/profile/:battlenet" component={App}>
      <IndexRedirect to="/profile/:battlenet/Overview" />
      <Route path="/profile/:battlenet/Overview" component={Overview} />
    </Route>
  </Route>
);
