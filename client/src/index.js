import React from 'react';
import { render } from 'react-dom';
import DropDownMenu from 'material-ui/DropDownMenu';
import MenuItem from 'material-ui/MenuItem';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';

const Header = () => (
  <AppBar title="Overwatcher" />
);

const Root = () => (
  <MuiThemeProvider>
    <Header />
  </MuiThemeProvider>
);

render(
  <Root />,
  document.getElementById('app')
);
