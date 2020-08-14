import React from 'react';
import Typography from "@material-ui/core/Typography";
// styles
import useStyles from "./styles";

export default function CopyRight(props) {
    const classes = useStyles();
    
    return (
        <Typography color="primary" className={classes.copyright}>
            © 2019-2022 Tink Communicator. All rights reserved.
        </Typography>    
    );
}