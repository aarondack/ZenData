import React from 'react';
import { Provider } from 'react-redux';
import routes from '../../routes';
import { Router } from 'react-router';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const Root = ({ store, history }) => (
  <Provider store={store}>
    <div>
    <MuiThemeProvider>
      <Router history={history} routes={routes} />
    </MuiThemeProvider>
    </div>
  </Provider>
);

export default Root;
