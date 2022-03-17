import React, {Component} from 'react';
import axios from 'axios';
import {Button, Form , Modal, Icon, Input, Card, Feed} from 'semantic-ui-react';
import { Dropdown } from 'semantic-ui-react'
import Cookies from 'universal-cookie';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();


class ListGroups extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(
            <div>

            
            
            </div> 
        );
    }
    
    async componentDidMount(){

        const response= await axios(
            {url: 'http://localhost:5000/group/list' ,
            method:'GET',
            headers: {'access-token': cookies.get('token_splitwise') }
            }
        )
        .then(        
        
        )
        .catch(err => {
            
        })

        console.log(response)     

    }
        
}
export default ListGroups;