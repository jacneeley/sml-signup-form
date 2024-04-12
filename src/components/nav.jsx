import React from "react";
import {useState} from "react";

export default function Nav(){
    const [popup, setPopup] = useState(false);

    function handlePopup(){
        console.log("Clicked");
        if(!popup){
            setPopup(true);
        }
        else {
            setPopup(false);
            
        }
    }

    return (
        <div id="nav" class="nav-links">
            <h2>Signup Form</h2>
            <a className="abt-button" onClick={()=> handlePopup()}>About</a>
            <hr></hr>
            <div id="popup" className={popup == false ? "pop-up" : "pop-up display-popup"}>
                <a className="close-btn" onClick={() => handlePopup()}>X</a>
                <div className="popup-content">
                    <h2>About</h2>
                    <p>The San Marcos Will not save and distribute your data.</p>
                    <p>All Data gathered in this form is for attendance purposes only.</p>
                    <p>For more information refer to our data use policy.</p>
                    <p>Thank you for taking interest in this program!</p>
                </div>
            </div>
        </div>
    )
}