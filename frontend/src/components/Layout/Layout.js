import React from "react";
import { Route, Switch, Redirect, withRouter} from "react-router-dom";

// styles
import useStyles from "./styles";
import classnames from "classnames";

// components
import Header from "../Header";
import Sidebar from "../Sidebar";
import Dashboard from "../../pages/dashboard";
import Group from "../../pages/group";

// context
import { useLayoutState } from "../../context/LayoutContext";

function Layout(props) {
    const classes = useStyles();
    const layoutState = useLayoutState();
    return (
        <div className={classes.root}>
            <>
                <Header history={props.history} />
                <Sidebar />
                <div className={classnames(classes.content, {[classes.contentShift]: layoutState.isSidebarOpened,})}>
                    {/* <div className={classes.fakeToolbar} /> */}
                    <Switch>
                        <Route path="/app/dashboard" component={Dashboard} />
                        <Route path="/app/group" component={Group} />
                    </Switch>
                </div>
            </>
        </div>
    );
}

export default withRouter(Layout);