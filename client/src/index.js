import React from 'react';
import { render } from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import App from './containers/App';

const Root = () => (
  <MuiThemeProvider>
    <App />
  </MuiThemeProvider>
);

render(
  <Root />,
  document.getElementById('app')
);
