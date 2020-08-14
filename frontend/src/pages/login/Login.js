import React, {useState} from "react";
import Grid from "@material-ui/core/Grid";
import CircularProgress from "@material-ui/core/CircularProgress";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Card from "@material-ui/core/Card";
import Fade from "@material-ui/core/Fade";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";

import { withRouter } from "react-router-dom";

// context
import { useUserDispatch, loginUser } from "../../context/UserContext";

//components
import CopyRight from "../../components/CopyRight";

// styles
import useStyles from "./styles";

function Login(props) {
    const classes = useStyles();
    const userDispatch = useUserDispatch();

    //local
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [companyCodeValue, setCompanyCodeValue] = useState("");
    const [emailValue, setEmailValue] = useState("");
    const [passwordValue, setPasswordValue] = useState("");
    
    return (
        <Grid className={classes.container}>
            <Card className={classes.cardContainer}>
                <CardContent>
                    <Typography variant="h2" className={classes.greeting}>
                        Login
                    </Typography>
                    <TextField id="companyCode"
                        InputProps={{
                        classes: {
                            underline: classes.textFieldUnderline,
                            input: classes.textField,
                        },
                        }}
                        value={companyCodeValue}
                        onChange={e => setCompanyCodeValue(e.target.value)}
                        margin="normal"
                        placeholder="Company Code"
                        type="text"
                        fullWidth
                    />

                    <TextField
                        id="email"
                        InputProps={{
                        classes: {
                            underline: classes.textFieldUnderline,
                            input: classes.textField,
                        },
                        }}
                        value={emailValue}
                        onChange={e => setEmailValue(e.target.value)}
                        margin="normal"
                        placeholder="Email Adress"
                        type="email"
                        fullWidth
                    />

                    <TextField
                        id="password"
                        InputProps={{
                        classes: {
                            underline: classes.textFieldUnderline,
                            input: classes.textField,
                        },
                        }}
                        value={passwordValue}
                        onChange={e => setPasswordValue(e.target.value)}
                        margin="normal"
                        placeholder="Password"
                        type="password"
                        fullWidth
                    />
                    <Fade in={error}>
                        <Typography color="secondary" className={classes.errorMessage}>
                            Something is wrong with your login or password :(
                        </Typography>
                    </Fade>
                </CardContent>
                <CardActions className={classes.cardAction} >
                    {isLoading ? (
                        <CircularProgress size={26} className={classes.loginLoader} />
                    ) : (
                    <Button variant="contained" color="primary" size="large" fullWidth className={classes.loginButton}
                        disabled={
                            emailValue.length === 0 || passwordValue.length === 0 || companyCodeValue.length === 0
                        }
                        onClick={() =>
                        loginUser(
                            userDispatch,
                            emailValue,
                            passwordValue,
                            props.history,
                            setIsLoading,
                            setError,
                        )
                        }
                    >
                        Login
                    </Button>
                    )}
                    <Button color="primary" fullWidth size="large" className={classes.forgetButton}>
                    Forget Password
                    </Button>
                </CardActions>  
            </Card>
            <CopyRight />
        </Grid>
    );
}

export default withRouter(Login);