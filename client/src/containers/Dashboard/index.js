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
    const { requestProfile } = this.props;
    requestProfile();
  }
  render() {
    return(
      <Header />
    );
  }
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    requestProfile: () => {
      dispatch(requestProfileBlob())
    }
  }
}

export default connect(null, mapDispatchToProps)(Dashboard);
