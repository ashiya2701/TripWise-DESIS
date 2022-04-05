import React from "react";
import {Input} from 'semantic-ui-react';
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
            <hr/>
            <Planner source = {source} destination={destination}/><hr/>
            <Hotels destination={destination} /><hr/>
            <Itinerary destination={destination}/>
        </div>
        
    );
}

export default TripPlanning;