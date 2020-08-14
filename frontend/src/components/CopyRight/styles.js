import { makeStyles } from "@material-ui/styles";

export default makeStyles(theme => ({
    copyright: {
        marginTop: theme.spacing(4),
        whiteSpace: "nowrap",
        [theme.breakpoints.up("md")]: {
          position: "absolute",
          bottom: theme.spacing(2),
        },
    },
}));