import React from 'react';
import { HashRouter, Route, Switch, Redirect } from "react-router-dom";

// components
import Layout from "./components/Layout";

// pages
import Error from "./pages/error";
import Login from "./pages/login";

// context
import { useUserState } from "./context/UserContext";

function App() {
  // global
  const { isAuthenticated } = useUserState();
  return (
    <HashRouter>
      <Switch>
        <Route exact path="/" render={() => <Redirect to="/dashboard" />} />
        <PrivateRoute path="/dashboard" component={Layout} />
        <PublicRoute path="/login" component={Login} />
        <Route component={Error} />
      </Switch>
    </HashRouter>
  );

  function PrivateRoute({ component, ...rest }) {
    return(
      <Route {...rest} 
        render={ props => isAuthenticated ? 
          ( React.createElement(component, props)) :
          (<Redirect to={{ pathname: "/login", state: { from: props.location}}}/>)
        }
      />
    );
  }

  function PublicRoute({ component, ...rest }) {
    return (
      <Route {...rest} 
        render={ props => isAuthenticated ? 
          (<Redirect to={{ pathname: "/" }} />) : 
          (React.createElement(component, props))
        }
      />
    );
  }
}

export default App;
