import React from "react";
import {Button, Form , Input} from 'semantic-ui-react';
import Hotels from "./hotels";
import Itinerary from "./Itinerary";

function TripPlanning(){
    const [city,setCity] = React.useState("");
    function handleChange(e){
        setCity(e.target.value);
    }
    return (
        <div>
            <h1>Trip Planning</h1>
            
            <Input type="text" value={city} onChange={handleChange} placeholder="Enter Destination (E.g. Delhi)" required />

            <Hotels city={city} />
            <Itinerary city={city}/>
        </div>
        
    );
}

export default TripPlanning;