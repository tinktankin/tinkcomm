import React from "react";
import { Route, Switch, Redirect, withRouter} from "react-router-dom";

// styles
import useStyles from "./styles";

// components
import Header from "../Header";
import Sidebar from "../Sidebar";

function Layout(props) {
    const classes = useStyles();
    return (
        <div className={classes.root}>
            <>
                <Header history={props.history} />
                <Sidebar />
            </>
        </div>
    );
}

export default Layout;