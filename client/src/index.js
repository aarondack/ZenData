import React from 'react';
import { render } from 'react-dom';
import configureStore from './store/configureStore';
import { browserHistory } from 'react-router';
import { syncHistoryWithStore } from 'react-router-redux';
import Root from './containers/Root';

const store = configureStore();
const history = syncHistoryWithStore(browserHistory, store);

render(
  <Root
    store={store}
    history={history}
    />,
  document.getElementById('app')
);
