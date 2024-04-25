import axios from 'axios'
import React, { useState, useEffect } from "react";

export default function AdminView(){
    
    const [loggedIn, setLoggedIn] = useState(false);
    //submissions
    const [subData, setSubData] = useState([]);

    function AdminLogin(){

        function getCredentials(credentials){
            console.log(credentials)
            axios({
                method: "post",
                url:"http://localhost:5000/auth/",
                data: credentials
            })
            .then(response => {
                console.log(response.data)
                if(response.data === 1 & response.status === 200){
                    setLoggedIn(true);
                }
                else{
                    alert("An error ocurred \nadmin not found \nstatus: " + response.data);
                }
            })
            .catch(error => console.error("ERROR: "+ error));
        }

        const handleForm = (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);

            const email = formData.get("email");
            const phone = formData.get("phone");

            if(!email || !phone){
                alert("invalid")
                return;
            }

            const payload = Object.fromEntries(formData);

            getCredentials(payload);
        }

        return (
            <>
                <form className='form-container' onSubmit={handleForm}>
                <div className='fields'>
                    <label>Email:</label>
                    <input className="text-input" name="email" type="text"/>
                    <label>Phone:</label>
                    <input className="text-input" name="phone" type="text"/> 
                    </div>
                <button className="submit-btn" type="submit">Log In</button>
                </form>
            </>
        )
    }

    function getSubmissionData(){
        axios.get("http://localhost:5000/attendees/")
        .then(response => {
            if(response.status === 200){
                console.log(response)
                setSubData(response.data);
            }
            else{
                alert("An error ocurred \nstatus: " + response.status);
            }
        })
        .catch(error => console.error("ERROR: "+ error));  
    }

    function DisplayResults(){
        
        return (
            <>
                <h2>Submissions</h2>
                <table>
                    <thead>
                        <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Child's Name</th>
                        <th>Age</th>
                        <th>Needs Laptop?</th>
                        </tr>
                    </thead>
                    <tbody>
                        {subData.map((attendee, id) => {
                            return (
                                <tr key = {id}>
                                    <td>{attendee.parentName}</td>
                                    <td>{attendee.email}</td>
                                    <td>{attendee.phone}</td>
                                    <td>{attendee.childName}</td>
                                    <td>{attendee.childAge}</td>
                                    <td>{attendee.laptop}</td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </>
        );
    }

    useEffect(() => {
        if (loggedIn) {
            getSubmissionData();
        }
    }, [loggedIn]);

    return(
        <>
            {
                !loggedIn ? <AdminLogin /> : (subData.length === 0 ? <p>Loading...</p> : <DisplayResults />)
            }
        </>
    );
}