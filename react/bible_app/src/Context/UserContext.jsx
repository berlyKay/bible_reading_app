import React, { createContext, useState} from "react";

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
    const [userStatus, setUserStatus] = useState({ isAuthenticated: false, username: ""});

    return (
        <UserContext.Provider value={{ userStatus, setUserStatus}}>
            {children}
        </UserContext.Provider>
    );
};