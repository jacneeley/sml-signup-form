import React from 'react';
import {useState} from 'react';

export default function form(){

    const handleSubmit = (e) => {
        alert("Sent!");
    }

    return (
        <div className='form-container center'>
            <form onSubmit={handleSubmit}>
                <label>Parent/Guardian's Full Name:</label>
                <input className="text-input" type="text" required/>
                
                <label>Child's Full Name:</label>
                <input className="text-input" type="text" required/>
                
                <label>Child's Age:</label>
                <input className="text-input" type="text" required/>
                

                <p>A laptop is needed for this camp.The library can provide one to those who need one, but there is a limited quantity.</p>
                <p>Will your child be able to bring their own laptop?</p>
                
                <label className ="radio-label"><input type="radio" value="Yes"required/>Yes</label>
                <label className ="radio-label"><input type="radio" value="No" checked required/>No</label>
                
                <button className= "submit-btn" type="submit">Submit</button>
            </form>      
        </div>
    )
}