import React from "react";

// styles
import useStyles from "./styles";

//components
import PageTitle from "../../components/PageTitle";
import  List from "../../components/List";
import {Button} from "@material-ui/core";
import { Link } from "react-router-dom";

export default function Group(props) {
    const classes = useStyles();
    const columns = [
        { name: "name", label: "Name", options: { filter: true, sort: true, }, },
        { name: "status", label: "Status", options: { filter: true, sort: true, }, },
        { name: "description", label: "Description", options: { filter: false, sort: false, }, },
        { name: "dateCreated", label: "Date Created", options: { filter: false, sort: false, }, },
        { name: "dateModified", label: "Date Modified", options: { filter: false, sort: false, }, },
    ];
    
    return (
        <>
            <PageTitle title="Group" />
            <List url="/groups" title="Group List" columns={columns}/>
            <Link to="/app/groups/add">
                <Button renderAs="button">Add Group</Button>
            </Link>
        </>
    );
}