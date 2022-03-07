import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
// import { Component } from 'react/cjs/react.production.min';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import {Button, Form , Modal, Icon, Dropdown, Input, Card, Feed} from 'semantic-ui-react';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class HotelSuggestion extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            name:"",
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(

            <div>
            <Form onSubmit={event => this.handleSubmit(event)} >
            <Form.Field >
            <Input type="text" value={this.state.name} onChange={event => this.HandleNameChange(event)} placeholder="Name" required />
            </Form.Field>
                        
            <Button type="submit" color="black">Create Project</Button>
            </Form>
            </div>
        
           
        );
    }


    async handleSubmit(event){

        event.preventDefault();

        let data= {"name": this.state.name} 


        const response= await axios(
            {url: 'http://localhost:5000/cities/list' ,
            method:'POST', 
        // mode: "no-cors",
            data: data
            }
        )
        .then( 
        console.log("request.. ")
        
        )
        .catch(err => {
            console.log(err)
            console.log("request!!!!")
        })

        console.log(response)

       
    }
    
    async HandleNameChange(event){
        this.setState({
            name: event.target.value
        });

    }
    
    async componentDidMount(){
       
        
    }
        
}



export default HotelSuggestion;