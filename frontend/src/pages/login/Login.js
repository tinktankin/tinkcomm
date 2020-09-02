import React, {useState} from "react";
import Grid from "@material-ui/core/Grid";
import CircularProgress from "@material-ui/core/CircularProgress";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Avatar from '@material-ui/core/Avatar';
import Link from '@material-ui/core/Link';
import Container from '@material-ui/core/Container';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';


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
        <Container component="main" maxWidth="xs">
        <div className={classes.paper}>
            <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
            Sign in
            </Typography>
            <form className={classes.form} noValidate>
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="companyCode"
                    label="Company Code"
                    name="companycode"
                    autoComplete="email"
                    autoFocus
                    value={companyCodeValue}
                    onChange={e => setCompanyCodeValue(e.target.value)}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="email"
                    label="Email Address"
                    name="email"
                    autoComplete="email"
                    value={emailValue}
                    onChange={e => setEmailValue(e.target.value)}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    name="password"
                    label="Password"
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    value={passwordValue}
                    onChange={e => setPasswordValue(e.target.value)}
                />
            {/* <FormControlLabel
                control={<Checkbox value="remember" color="primary" />}
                label="Remember me"
            /> */}
                {isLoading ? (
                  <CircularProgress size={26} className={classes.loginLoader} />
                ) : (
                  <Button
                    disabled={
                        emailValue.length === 0 || passwordValue.length === 0 || companyCodeValue.length ==0
                    }
                    onClick={() =>
                      loginUser(
                        userDispatch,
                        emailValue,
                        passwordValue,
                        companyCodeValue,
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
                    Login
                  </Button>
                )}
                {/* <Button
                    type="button"
                    fullWidth
                    variant="contained"
                    color="primary"
                    className={classes.submit}
                >
                    Sign In
                </Button> */}
                <Grid container>
                    <Grid item xs>
                    <Link href="#" variant="body2">
                        Forgot password?
                    </Link>
                    </Grid>
                    <Grid item>
                    <Link href="#" variant="body2">
                        {"Don't have an account? Sign Up"}
                    </Link>
                    </Grid>
                </Grid>
            </form>
            <CopyRight />
        </div>
    </Container>
    );
}

export default withRouter(Login);