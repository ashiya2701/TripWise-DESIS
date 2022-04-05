import React from "react";
import {Button, Form , Input} from 'semantic-ui-react';
import Hotels from "./hotels";
import Itinerary from "./Itinerary";
import Planner from "./planner";

function TripPlanning(){
    const [source,setsource] = React.useState("");
    const [destination,setdestination] = React.useState("");
    function handleSrcChange(e){
        setsource(e.target.value);
    }
    function handleDestChange(e){
        setdestination(e.target.value);
    }
    return (
        <div>
            <h1>Trip Planning</h1>
            <Input type="text" value={source} onChange={handleSrcChange} placeholder="Enter Source (E.g. Delhi)" required />
            <Input type="text" value={destination} onChange={handleDestChange} placeholder="Enter Destination (E.g. Delhi)" required />
            <Planner source = {source} destination={destination}/>
            <Hotels destination={destination} />
            <Itinerary destination={destination}/>
        </div>
        
    );
}

export default TripPlanning;