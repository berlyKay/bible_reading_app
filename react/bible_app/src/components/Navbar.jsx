import React, { useState, useEffect, useContext } from "react"
import { Link } from "react-router-dom"
import { UserContext } from "../Context/UserContext"


export default function Navbar() {
    const { userStatus, setUserStatus } = useContext(UserContext);
    
    useEffect(() => {
        const fetchUserStatus = async () => {
            try {
                const response = await fetch('http://localhost:8000/account/');
                const data = await response.json();

                setUserStatus({
                    isAuthenticated: data.isAuthenticated,
                    username: data.username || "",
                })
        } catch (error) {
            console.error("Error fetching user status:", error);
        }
        };

        fetchUserStatus()
    }, [location.pathname, setUserStatus])
    
    return (
        <nav>
            <ul>
                <li>
                    <Link to="/home">Home</Link>
                </li>
                <li>
                    <Link to="/plan">Plan</Link>
                </li>
                <li>
                    <Link to="/proverb">Proverb</Link>
                </li>
                {userStatus.isAuthenticated ? (
                    <>
                        <li>
                            <Link to="/account">Account ({userStatus.username})</Link>
                        </li>
                        <li>
                            <a 
                                onClick={async () => {
                                    try {
                                     await fetch('http://localhost:8000/logout');
                                     setUserStatus({ isAuthenticated: false, username: ""});
                                     window.location.href = "/";
                                    } catch (error) {
                                        console.error("Error logging out:", error);
                                    }
                                }}
                            >
                                Log Out
                            </a>
                        </li>
                    </>
                ) : (
                    <>
                        <li>
                            <Link to="http://localhost:8000/signup">Signup</Link>
                        </li>
                        <li>
                            <a
                                href="http://localhost:8000/login"
                                onClick={async () => {
                                    const response = await fetch("http://localhost:8000/account")
                                    const responseData = await response.json();
                                    console.log(responseData)
                                    setUserStatus({
                                        isAuthenticated: responseData.isAuthenticated,
                                        username: responseData.usernam
                                    });
                                }}
                            >
                                Log In
                            </a>
                        </li>
                            {console.log(userStatus)}
                            {console.log("yes")}
                    </>
                    )}
            </ul>
        </nav>
    )
}



