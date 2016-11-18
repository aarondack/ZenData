import React from 'react';
import AppBar from 'material-ui/AppBar';
import './Dashboard.css';
import { connect } from 'react-redux';
import { requestProfileBlob } from '../../actions';

const Header = () => (
  <AppBar title="Overwatcher" style={{backgroundColor: '#FFF' }}/>
);

class Dashboard extends React.Component {
  componentDidMount() {
    const { requestProfile, profileName } = this.props;
    requestProfile(profileName);
  }
  render() {
    return(
      <Header />
    );
  }
};

const mapStateToProps = (state, ownProps) => {
  return {
    profileName: ownProps.params.battlenet
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    requestProfile: (profileName) => {
      dispatch(requestProfileBlob(profileName))
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Dashboard);
