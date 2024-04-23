import React from "react";
import {useState} from "react";

export default function results(){
    
    const [submission, setSubmission] = useState({});

    
    return (
        <>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Child's Name</th>
                    <th>Child's Age</th>
                    <th>Needs Laptop?</th>
                </tr>
            </table>
        </>
    )
}