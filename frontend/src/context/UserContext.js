import React from "react";

const UserStateContext = React.createContext();
const UserDispatchContext = React.createContext();

const userReducer = (state, action) => {
    switch (action.type) {
        case "LOGIN_SUCCESS":
            return { ...state, isAuthenticated: true };
        case "SIGN_OUT_SUCCESS":
            return { ...state, isAuthenticated: false };
        default: {
            throw new Error(`Unhandled action type: ${action.type}`);
        }
    }
}

const UserProvider = ({ children }) => {
    const [state, dispatch] = React.useReducer(userReducer, {
      isAuthenticated: !!localStorage.getItem("id_token"),
    });
  
    return (
      <UserStateContext.Provider value={state}>
        <UserDispatchContext.Provider value={dispatch}>
          {children}
        </UserDispatchContext.Provider>
      </UserStateContext.Provider>
    );
}

const useUserState = () => {
    const context = React.useContext(UserStateContext);
    if (context === undefined) {
      throw new Error("useUserState must be used within a UserProvider");
    }
    return context;
}
  
const useUserDispatch = () => {
    const context = React.useContext(UserDispatchContext);
    if (context === undefined) {
      throw new Error("useUserDispatch must be used within a UserProvider");
    }
    return context;
}

const loginUser = (dispatch, login, password, history, setIsLoading, setError) => {
    setError(false);
    setIsLoading(true);
  
    if (!!login && !!password) {
        setTimeout(() => {
            localStorage.setItem('id_token', 1)
            setError(null)
            setIsLoading(false)
            dispatch({ type: 'LOGIN_SUCCESS' })
            history.push('/')
        }, 2000);
    } else {
        dispatch({ type: "LOGIN_FAILURE" });
        setError(true);
        setIsLoading(false);
    }
}

function signOut(dispatch, history) {
    localStorage.removeItem("id_token");
    dispatch({ type: "SIGN_OUT_SUCCESS" });
    history.push("/login");
}

export { UserProvider, useUserState, useUserDispatch, loginUser, signOut };

