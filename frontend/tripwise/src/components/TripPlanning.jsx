import React from "react";
import {Button, Form , Input} from 'semantic-ui-react';
import Hotels from "./hotels";
import Itinerary from "./Itinerary";

function Landing(){
    const [city,setCity] = React.useState("");
    const [submit,setSubmit] = React.useState(false);
    function handleChange(e){
        setCity(e.target.value);
        setSubmit(false);
    }
    function handleSubmit(e){
        e.preventDefault();
        setSubmit(true);
    }
    return (
        <div>
            <h1>Trip Planning</h1>
            <Form onSubmit={handleSubmit} >
                <Form.Field >
                    <Input type="text" value={city} onChange={handleChange} placeholder="Enter Destination (E.g. Delhi)" required />
                </Form.Field>

                <Button type="submit" color="black">Plan Trip!</Button>
            </Form>

            <Hotels city={city} submit={submit}/>
            <Itinerary city={city} submit={submit}/>
        </div>
        
    );
}

export default Landing;