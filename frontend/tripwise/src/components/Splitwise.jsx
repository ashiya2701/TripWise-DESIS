import React from "react";
import { Link } from 'react-router-dom';
import {Button} from 'semantic-ui-react';
import axios from 'axios';
import Cookies from 'universal-cookie';
import Logout from './Logout';
import CreateGroup from './create_group'
import GroupList from './list_groups';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();

function Splitwise(){

    if(cookies.get('token_splitwise')===undefined||cookies.get('token_splitwise').length===0){
        return (
            <div>
                <Button color="black"><Link to='/LoginSignUp' > Login/SignUp </Link></Button>
            </div>
            
        );
    }else{

    return (
        <div>
            <CreateGroup/>
            <GroupList/>
            <Logout/>
        </div>
        
    );
    }
}

export default Splitwise;