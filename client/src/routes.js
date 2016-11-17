import React from 'react';
import { Route } from 'react-router';
import Dashboard from './containers/Dashboard';
import App from './containers/App';

export default(
  <Route path="/" component={App}>
    <Route path="/profile/:battlenet" component={Dashboard} />
  </Route>
);
