import React from 'react';
import AppBar from 'material-ui/AppBar';
import Avatar from 'material-ui/Avatar';
import './Header.css';

const Header = ({ profile, name }) => (
  <div>
    <AppBar style={{backgroundColor: '#FFF' }}>
    <h4 className="profileName">{name}</h4>
    <div className="avatar">
      <Avatar src={profile[0].about.avatar} />
    </div>
    </AppBar>
  </div>
);

export default Header;
