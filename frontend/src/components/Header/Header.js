import React, { useState } from "react";

//MUI
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Menu from "@material-ui/core/Menu";
import MenuItem from "@material-ui/core/MenuItem";

import {
    Menu as MenuIcon,
    ArrowBack as ArrowBackIcon,
    Person as AccountIcon,
} from "@material-ui/icons";

import classNames from "classnames";

//components
import { Typography } from "../Wrappers/Wrappers";

// context
import { useLayoutState, useLayoutDispatch, toggleSidebar} from "../../context/LayoutContext";
  import { useUserDispatch, signOut } from "../../context/UserContext";

// styles
import useStyles from "./styles";

export default function Header(props) {
    const classes = useStyles();

  // global
    const layoutState = useLayoutState();
    const layoutDispatch = useLayoutDispatch();
    const userDispatch = useUserDispatch();

    // local
    const [profileMenu, setProfileMenu] = useState(null);

    return(
        <AppBar position="fixed" className={classes.appBar}>
            <Toolbar className={classes.toolbar}>
                <IconButton 
                    color="inherit" 
                    onClick={() => toggleSidebar(layoutDispatch)}
                    className={classNames(classes.headerMenuButton,classes.headerMenuButtonCollapse)}
                >
                    {layoutState.isSidebarOpened ? (
                        <ArrowBackIcon
                            classes={{root: classNames(classes.headerIcon,classes.headerIconCollapse)}}
                        />
                    ) : (
                        <MenuIcon
                            classes={{root: classNames(classes.headerIcon,classes.headerIconCollapse)}}
                        />
                    )}
                </IconButton>
                <Typography variant="h6" weight="medium" className={classes.logotype}>
                    Welcome Admin
                </Typography>
                <div className={classes.grow} />
                <IconButton
                    aria-haspopup="true"
                    color="inherit"
                    className={classes.headerMenuButton}
                    aria-controls="profile-menu"
                    onClick={e => setProfileMenu(e.currentTarget)}
                >
                    <AccountIcon classes={{ root: classes.headerIcon }} />
                </IconButton>
                <Menu
                    id="profile-menu"
                    open={Boolean(profileMenu)}
                    anchorEl={profileMenu}
                    onClose={() => setProfileMenu(null)}
                    className={classes.headerMenu}
                    classes={{ paper: classes.profileMenu }}
                    disableAutoFocusItem
                >
                    <div className={classes.profileMenuUser}>
                        <Typography variant="h4" weight="medium">
                            John Smith
                        </Typography>
                    </div>
                    <MenuItem className={classNames(classes.profileMenuItem,classes.headerMenuItem)}>
                        <AccountIcon className={classes.profileMenuIcon} /> Profile
                    </MenuItem>
                    <div className={classes.profileMenuUser}>
                        <Typography className={classes.profileMenuLink} color="primary"
                            onClick={() => signOut(userDispatch, props.history)}>
                            Sign Out
                        </Typography>
                    </div>
                </Menu>
            </Toolbar>
        </AppBar>
    );
}