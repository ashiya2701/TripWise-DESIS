import React from "react";
import { Link } from 'react-router-dom';
import {Button} from 'semantic-ui-react';

function Landing(){
    return (
        <div>
            <h1>TripWise</h1>
            <Button color="black"><Link to='/TripPlanning' > Plan your trip </Link></Button>
            <Button color="black"><Link to='/Splitwise' > Go to Dashboard </Link></Button>
            <Button color="black"><Link to='/LoginSignUp' > Login/SignUp </Link></Button>
        </div>
        
    );
}

export default Landing;