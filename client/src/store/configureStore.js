import { createStore, compose, applyMiddleware } from 'redux';
import { routerMiddleware } from 'react-router-redux';
import { browserHistory } from 'react-router';
import rootReducer from '../reducers';
import createSagaMiddleware from 'redux-saga';
import rootSaga from '../sagas';

const configureStore = (initialState) => {
  const sagaMiddleware = createSagaMiddleware();

  const configStore = compose(
    applyMiddleware(sagaMiddleware, routerMiddleware(browserHistory)),
    window.devToolsExtension ? window.devToolsExtension() : dev => dev)(createStore);

  const store = configStore(rootReducer, initialState);
  sagaMiddleware.run(rootSaga);

  return store;
}

export default configureStore;
