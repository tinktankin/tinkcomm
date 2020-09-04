import React, { useState, useEffect } from "react";
import Drawer from "@material-ui/core/Drawer";
import IconButton from "@material-ui/core/IconButton";
import List from "@material-ui/core/List";


// styles
import useStyles from "./styles";
import { useTheme } from "@material-ui/styles";
import { withRouter } from "react-router-dom";
import classNames from "classnames";

import {
    Home as HomeIcon,
    ArrowBack as ArrowBackIcon,
    Group as GroupIcon
} from "@material-ui/icons";

// context
import {
    useLayoutState,
    useLayoutDispatch,
    toggleSidebar,
} from "../../context/LayoutContext";

// components
import SidebarLink from "./components/SidebarLink/SidebarLink";

const structure = [
    { id: 0, label: "Dashboard", link: "/app/dashboard", icon: <HomeIcon /> },
    { id: 1, label: "Group", link: "/app/group", icon: <GroupIcon /> },
];
function Sidebar({ location }) {
    const classes = useStyles();
    const theme = useTheme();

    // global
    const { isSidebarOpened } = useLayoutState();
    const layoutDispatch = useLayoutDispatch();

    // local
    const [isPermanent, setPermanent] = useState(true);
    useEffect(function() {
        window.addEventListener("resize", handleWindowWidthChange);
        handleWindowWidthChange();
        return function cleanup() {
          window.removeEventListener("resize", handleWindowWidthChange);
        };
    });
    return(
        <Drawer
            variant={isPermanent ? "permanent" : "temporary"}
            className={classNames(classes.drawer, {
                [classes.drawerOpen]: isSidebarOpened,
                [classes.drawerClose]: !isSidebarOpened,
            })}
            classes={{
                paper: classNames({
                [classes.drawerOpen]: isSidebarOpened,
                [classes.drawerClose]: !isSidebarOpened,
                }),
            }}
            open={isSidebarOpened}
            >
            <div className={classes.toolbar} />
            <div className={classes.mobileBackButton}>
                <IconButton onClick={() => toggleSidebar(layoutDispatch)}>
                <ArrowBackIcon
                    classes={{
                    root: classNames(classes.headerIcon, classes.headerIconCollapse),
                    }}
                />
                </IconButton>
            </div>
            <List className={classes.sidebarList}>
                {structure.map(link => (
                <SidebarLink
                    key={link.id}
                    location={location}
                    isSidebarOpened={isSidebarOpened}
                    {...link}
                />
                ))}
            </List>
        </Drawer>
    );

    function handleWindowWidthChange() {
        var windowWidth = window.innerWidth;
        var breakpointWidth = theme.breakpoints.values.md;
        var isSmallScreen = windowWidth < breakpointWidth;
    
        if (isSmallScreen && isPermanent) {
          setPermanent(false);
        } else if (!isSmallScreen && !isPermanent) {
          setPermanent(true);
        }
    }
}
export default withRouter(Sidebar);