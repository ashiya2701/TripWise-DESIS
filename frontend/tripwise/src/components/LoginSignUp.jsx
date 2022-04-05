import React from 'react'
import { Grid, Segment } from 'semantic-ui-react'
import Login from './Login'
import Signup from './Signup'
import { Navigate } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'universal-cookie';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();


const LoginSignUp = () => {
    
    return(
    
    <Segment placeholder>
        <Grid columns={2} relaxed='very' stackable>
        <Grid.Column>
            <h3>Login</h3>
            <Login/>
        </Grid.Column>

        <Grid.Column>
            <h3>Sign-Up</h3>
            <Signup/>
        </Grid.Column>
        </Grid>
    </Segment>
)}

export default LoginSignUp
