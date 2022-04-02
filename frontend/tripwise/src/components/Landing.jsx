import React from "react";
import { Link } from 'react-router-dom';

function Landing(){
    return (
        <div>
            <Link to='/TripPlanning' > Plan your trip </Link>
        </div>
        
    );
}

export default Landing;