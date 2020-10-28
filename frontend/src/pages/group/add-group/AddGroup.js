import React, {useState} from "react";
import CircularProgress from "@material-ui/core/CircularProgress";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Fade from "@material-ui/core/Fade";

// context
import { useUserDispatch} from "../../../context/UserContext";

//components
import PageTitle from "../../../components/PageTitle";

// styles
import useStyles from "../styles";
import axios from "axios";
import {BASE_URL} from "../../../utils/constant";

export default function AddGroup(props) {
    const classes = useStyles();
    const userDispatch = useUserDispatch();

    //local
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [nameValue, setNameValue] = useState("");
    const [statusValue, setStatusValue] = useState("");
    const [descriptionValue, setDescriptionValue] = useState("");

    const addGroup = (dispatch, name, status, description, history, setIsLoading, setError) => {
    setError(false);
    setIsLoading(true);

    if (!!name) {
        axios.post(BASE_URL + "/groups", {"name":name, "status":status, "description":description})
        .then((response) => {
            setError(null)
            setIsLoading(false)
            dispatch({ type: 'Group Added Successfully' })
            history.push('/')
        })
        .catch((error) => {
            setError(true);
            setIsLoading(false);
        });
    } else {
        setError(true);
        setIsLoading(false);
    }
    }

    return (
      <>
        <PageTitle title="Add Group" />
        <div className={classes.paper}>
            <form className={classes.form} noValidate>
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="name"
                    label="Name"
                    name="name"
                    autoComplete="name"
                    autoFocus
                    value={nameValue}
                    onChange={e => setNameValue(e.target.value)}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="status"
                    label="Status"
                    name="status"
                    autoComplete="status"
                    value={statusValue}
                    onChange={e => setStatusValue(e.target.value)}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    name="description"
                    label="Description"
                    type="description"
                    id="description"
                    autoComplete="description"
                    value={descriptionValue}
                    onChange={e => setDescriptionValue(e.target.value)}
                />
                <Fade in={error}>
                <Typography color="secondary" className={classes.errorMessage}>
                  Something is wrong!
                </Typography>
              </Fade>
                {isLoading ? (
                  <CircularProgress size={26} />
                ) : (
                  <Button
                    disabled={
                        nameValue.length === 0
                    }
                    onClick={() =>
                      addGroup(
                        userDispatch,
                        nameValue,
                        statusValue,
                        descriptionValue,
                        props.history,
                        setIsLoading,
                        setError,
                      )
                    }
                    variant="contained"
                    color="primary"
                    size="large"
                    fullWidth
                    className={classes.submit}
                  >
                    Submit
                  </Button>
                )}
            </form>
        </div>
      </>
    );
}