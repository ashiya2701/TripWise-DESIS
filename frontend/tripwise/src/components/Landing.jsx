import React from "react";
import { Link } from 'react-router-dom';
import {Button} from 'semantic-ui-react';
import axios from 'axios';
import Cookies from 'universal-cookie';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();
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