import React, {useEffect, useState} from "react";

import { Grid } from "@material-ui/core";
import MUIDataTable from "mui-datatables";
import CircularProgress from '@material-ui/core/CircularProgress';

import axios from "../../service/axios";
import { isEmpty } from "../../utils/stringUtil";

//components
import { Typography } from "../../components/Wrappers";

export default function List(props) {

    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(20);
    const [count, setCount] = useState(10);
    const [sortOrder, setSortOrder] = useState({});
    const [data, setData] = useState(["Loading Data..."]);
    const [isLoading, setIsLoading] = useState(false);

    const changeTable = (page, searchText, sortOrder) => {
        console.log(page, searchText, sortOrder);
        setIsLoading(true);
        xhrRequest(page, searchText, sortOrder);
    }

    const prepareQueryString = (page=0, searchText="", sortOrder={}) => {

        console.log(page, searchText, sortOrder);
        let queryString = "?";
        if(!isEmpty(page)) {
            queryString +=  "page="+(page+1);
        } else {
            queryString +=  "page=1";   
        }

        if(!isEmpty(searchText)) {
            queryString += "&searchText=" + searchText;        
        }
        if(sortOrder.name && !isEmpty(sortOrder.name)) {
            queryString += "&sort="+sortOrder.name+"&sortDir="+ (sortOrder.direction === "" ? "asc" : sortOrder.direction);    
        }
        return queryString;
    }

    const xhrRequest = (page=0, searchText="", sortOrder={}) => {
        axios.get(props.url + prepareQueryString(page, searchText, sortOrder))
        .then(res => {
            setIsLoading(false);
            setData(res.data.payload.results);
            setPage(res.data.payload.page - 1);
            setCount(res.data.payload.total);
            setRowsPerPage(res.data.payload.page_size);
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
        page: page,
        onTableChange: (action, tableState) => {
            console.log(action, tableState);
            switch (action) {
                case 'changePage':
                    changeTable(tableState.page, tableState.searchText, tableState.sortOrder);
                    break;
                case 'sort':
                    changeTable(tableState.page, tableState.searchText, tableState.sortOrder);
                    break;
                case 'search':
                    changeTable(tableState.page, tableState.searchText, tableState.sortOrder);
                    break;
                default:
                    console.log('action not handled.');
            }
        }
    };

    useEffect(() => {
        xhrRequest();   
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