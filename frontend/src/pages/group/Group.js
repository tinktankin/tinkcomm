import React, {useEffect, useState} from "react";

import { Grid } from "@material-ui/core";
import MUIDataTable from "mui-datatables";

import axios from "../../service/axios";

// styles
import useStyles from "./styles";

//components
import PageTitle from "../../components/PageTitle";

export default function Group(props) {
    const classes = useStyles();
    const [groups, setGroups] = useState([]);

    const columns = [
        { name: "name", label: "Name", options: { filter: true, sort: true, }, },
        { name: "status", label: "Status", options: { filter: true, sort: true, }, },
        { name: "description", label: "Description", options: { filter: false,sort: false, }, },
        { name: "dateCreated", label: "Date Created", options: { filter: false,sort: false, }, },
        { name: "dateModified", label: "Date Modified", options: { filter: false,sort: false, }, },
    ];

    useEffect(() => {
        axios.get("/groups")
        .then(res => {
            console.log(res);
            setGroups(res.data.data);
        })
        .catch(err => {console.log(err)})    
    }, []);
    
    return (
        <>
            <PageTitle title="Group" />
            <Grid container spacing={4}>
                <Grid item xs={12}>
                <MUIDataTable
                    title="Group List"
                    data={groups}
                    columns={columns}
                    options={{
                        filterType: "checkbox",
                        download: false,
                        print: false
                    }}
                />
                </Grid>
            </Grid>
        </>
    );
}