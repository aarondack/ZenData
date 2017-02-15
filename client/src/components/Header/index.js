import React from 'react';
import AppBar from 'material-ui/AppBar';
import Avatar from 'material-ui/Avatar';
import './Header.css';

const Header = ({ profile, name }) => (
  <div className="header">
      <div className="logo" />
      <div className="profiles">
        <h4 className="profileName">{name}</h4>
        <div className="avatar">
        <Avatar src={profile[0].about.avatar} />
      </div>
    </div>
  </div>
);

export default Header;
