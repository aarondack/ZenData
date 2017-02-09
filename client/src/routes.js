import React from 'react';
import { Route, IndexRoute } from 'react-router';
import Dashboard from './containers/Dashboard';
import BattleNetSelector from './containers/BattleNetSelector';
import App from './containers/App';

export default(
  <Route path="/" component={App}>
    <IndexRoute component={BattleNetSelector} />
    <Route path="/profile/:battlenet" component={Dashboard} />
  </Route>
);
