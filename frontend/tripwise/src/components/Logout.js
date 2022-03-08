import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
// import { Component } from 'react/cjs/react.production.min';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import {Button, Form , Modal, Icon, Dropdown, Input, Card, Feed} from 'semantic-ui-react';
import Cookies from 'universal-cookie';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();

class Logout extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            username:"",
            password:"",
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(

            <div>
            <Form onSubmit={event => this.handleSubmit(event)} >
                <Button type="submit" color="black">Logout</Button>
            </Form>
            </div>
        
           
        );
    }


    async handleSubmit(event){

        event.preventDefault();
      
        let formData = { 
            access_token: cookies.get('token_splitwise')
        }

        console.log(formData);


        const response= await axios(
            {url: 'http://localhost:5000/logout' ,
            method:'POST', 
            data: formData
            }
        )
        .then( 
        // console.log("request.. ")
        cookies.set('token_splitwise', "", { path: '/' })
        
        )
        .catch(err => {
            // console.log(err)
            // console.log("request!!!!")
        })
        console.log(response)
        console.log(response.data)

        // cookies.set('token_splitwise', response.data, { path: '/' });

        console.log(cookies.get('token_splitwise'));
    }
    
    async componentDidMount(){

    }
        
}



export default Logout;