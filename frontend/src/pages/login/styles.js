import { makeStyles } from "@material-ui/styles";

export default makeStyles(theme => ({
    container: {
        height: "100vh",
        width: "100vw",
        display: "flex",
        justifyContent: "center",
        flexDirection: "column",
        alignItems: "center",
        position: "absolute",
        top: 0,
        left: 0,
    },
    cardContainer: {
        position: "absolute",
        top: 130,
        width: "35%",
        height: "40%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        [theme.breakpoints.down("md")]: {
          width: "50%",
        },
    },
    greeting: {
        fontWeight: 500,
        textAlign: "center",
        marginTop: theme.spacing(4),
    },    
    textFieldUnderline: {
        "&:before": {
            borderBottomColor: theme.palette.primary.light,
        },
        "&:after": {
            borderBottomColor: theme.palette.primary.main,
        },
        "&:hover:before": {
            borderBottomColor: `${theme.palette.primary.light} !important`,
        },
    },
    textField: {
        borderBottomColor: theme.palette.background.light,
    },
    formButtons: {
        width: "100%",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
    },
    errorMessage: {
        textAlign: "center",
    },
    cardAction: {
        width: "80%"
    },
    loginButton: {
        textTransform: "none",
        fontWeight: 600,
    },
    forgetButton: {
        textTransform: "none",
        fontWeight: 400,
    },
    loginLoader: {
        marginLeft: theme.spacing(4),
    },
}));