import axios from 'axios'
import React from "react";
import {useState} from 'react';

export default function form(){

    const[radio, setRadio] = useState("No");

    const handleChange = (e) => {
        setRadio(e.target.value);
    }

    const submitForm= (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);

        //validate
        const parentName = formData.get("parentName");
        const email = formData.get("email");
        const phone = formData.get("parentPhone");
        const childName = formData.get("childName");
        const childAge = formData.get("childAge");
        const hasLaptop = formData.get("laptop");

        if(!parentName || !email || !phone || !childName || !childAge || !hasLaptop){
            alert("Please enter all missing values");
            return;
        }
        else {
            console.log("No Missing Fields: Success!");
        }

        const payload = Object.fromEntries(formData);

        sendToBackend(payload);
    }

    function sendToBackend(jsobj){
        console.log(jsobj)
        axios({
            method: "post",
            url:'http://localhost:5000/attendees/add', 
            data:jsobj,
        })
        .then(response => {console.log(response)
            console.log(response.status);
            if(response.status == 200){
                alert("Sent!");
                return window.location.replace("/success");
            }
            else {
                alert("Error..." + "\n" + response.statusText + "\nPlease try again later, or email JakNeeley@outlook.com");
            }
        })
        .catch(error => console.error("ERROR: "+ error));
    }


    return(
        <div className='form-container'>
            <h2>Code Camp </h2>
            <form onSubmit={submitForm}>
                <label>Parent/Guardian's Full Name:</label>
                <input className="text-input" name="parentName" type="text" maxLength="50" required/>

                <label>Guardian Email:</label>
                <input className="text-input" name="email" type="email" placeholder="email@email.com" maxLength="100" required/>

                <label>Guardian Phone:</label>
                <input className="text-input" name="parentPhone" type="text" placeholder="xxx-xxx-xxxx" minLength="10" maxLength="12" required/>

                <label>Child's Full Name:</label>
                <input className="text-input" name="childName" type="text" maxLength="50" required/>

                <label>Child's Age:</label>
                <input className="text-input" name="childAge" type="text" min="9" maxLength="2" required/>


                <p>A laptop is needed for this camp.The library can provide one to those who need one, but there is a limited quantity.</p>
                <p>Will your child be able to bring their own laptop?</p>


                <label className ="radio-label">
                    <input 
                        type="radio" 
                        value="Yes" 
                        name="laptop" 
                        checked={radio === "Yes"} 
                        required
                        onChange = {handleChange}
                    />
                    Yes
                    </label>
                <label className ="radio-label">
                    <input 
                        type="radio" 
                        value="No" 
                        name="laptop" 
                        checked={radio === "No"} 
                        required
                        onChange = {handleChange}
                    />
                    No
                    </label>


                <button className= "submit-btn" type="submit">Submit</button>
            </form>      
        </div>
    )
}
