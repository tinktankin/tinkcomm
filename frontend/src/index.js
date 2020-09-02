import React from 'react';
import ReactDOM from 'react-dom';
import * as serviceWorker from './serviceWorker';
import { ThemeProvider } from "@material-ui/styles";
import { CssBaseline } from "@material-ui/core";

import Themes from "./themes";
import App from './App';
import { UserProvider } from "./context/UserContext";
import { LayoutProvider } from "./context/LayoutContext";

ReactDOM.render(
    <LayoutProvider>
      <UserProvider>
        <ThemeProvider theme={Themes.default}>
          <CssBaseline />
          <App />
        </ThemeProvider>
      </UserProvider>
    </LayoutProvider>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
