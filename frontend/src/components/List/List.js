import React, {useEffect, useState} from "react";

import { Grid } from "@material-ui/core";
import MUIDataTable from "mui-datatables";
import CircularProgress from '@material-ui/core/CircularProgress';

import axios from "../../service/axios";

//components
import { Typography } from "../../components/Wrappers";

export default function List(props) {

    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(10);
    const [count, setCount] = useState(1);
    const [sortOrder, setSortOrder] = useState({});
    const [data, setData] = useState(["Loading Data..."]);
    const [isLoading, setIsLoading] = useState(false);

    const changeTable = (page, sortOrder) => {
        console.log(page, sortOrder);
        setIsLoading(true);
        xhrRequest(page, sortOrder);
    }

    const xhrRequest = (page, sortOrder = {}) => {
        axios.get(props.url + "?page="+page)
        .then(res => {
            setIsLoading(false);
            setData(res.data.payload);
            setPage(page);
            setSortOrder(sortOrder);
            setCount(res.data.payload.length)
        })
        .catch(err => {console.log(err)})     
    }


    const options = {
        filter: true,
        filterType: 'dropdown',
        responsive: 'vertical',
        serverSide: true,
        count: count,
        rowsPerPage: rowsPerPage,
        rowsPerPageOptions: [],
        sortOrder: sortOrder,
        download: false,
        print: false,
        onTableChange: (action, tableState) => {
            console.log(action, tableState);
            switch (action) {
                case 'changePage':
                    changeTable(tableState.page, tableState.sortOrder);
                    break;
                case 'sort':
                    changeTable(tableState.page, tableState.sortOrder);
                    break;
                default:
                    console.log('action not handled.');
            }
        }
    };

    useEffect(() => {
        xhrRequest(0, 10);   
    }, []);
    
    return (
        <>
            <Grid container spacing={4}>
                <Grid item xs={12}>
                <MUIDataTable
                    title= {<Typography variant="h6">
                    {props.title}
                    {isLoading && <CircularProgress size={24} style={{marginLeft: 15, position: 'relative', top: 4}} />}
                    </Typography>
                    }
                    data={data}
                    columns={props.columns}
                    options={options}
                />
                </Grid>
            </Grid>
        </>
    );
}