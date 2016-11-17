import React from 'react';
import AppBar from 'material-ui/AppBar';
import './App.css';

const Header = () => (
  <AppBar title="Overwatcher" style={{backgroundColor: '#FFF' }}/>
);

class App extends React.Component {
  render() {
    return(
      <Header />
    );
  }
};

export default App;
