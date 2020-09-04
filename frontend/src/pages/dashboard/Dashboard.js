import React from "react";

// styles
import useStyles from "./styles";

//components
import PageTitle from "../../components/PageTitle";

export default function Dashboard(props) {
    
    const classes = useStyles();
    
    return (
        <>
            <PageTitle title="Dashboard"/>
        </>
    );
}