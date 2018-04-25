import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';

//bootstrap
import './css/bootstrap.css';
import './css/bootstrap-theme.css';

//style sheets
import './css/index.css';

//components dir
import App from './components/App.js';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<BrowserRouter><App /></BrowserRouter>, document.getElementById('root'));
registerServiceWorker();

