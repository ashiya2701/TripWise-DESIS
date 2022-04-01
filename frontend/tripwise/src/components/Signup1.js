import 'semantic-ui-css/semantic.min.css';
import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
// import { Component } from 'react/cjs/react.production.min';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import {Button, Form , Modal, Icon, Dropdown, Input, Card, Feed} from 'semantic-ui-react';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class Signup1 extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            name:"",
            email:"",
            username:"",
            phone:"",
            password:"",
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
<Form.Field >
<Input type="email" value={this.state.email} onChange={event => this.HandleemailChange(event)} placeholder="email" required /></Form.Field>
<Form.Field >
<Input type="text" value={this.state.username} onChange={event => this.HandleusernameChange(event)} placeholder="Username" required /></Form.Field>
<Form.Field >
<Input type="text" value={this.state.phone} onChange={event => this.HandlephoneChange(event)} placeholder="phone" required /></Form.Field>
<Form.Field >
<Input type="password" value={this.state.password} onChange={event => this.HandlepasswordChange(event)} placeholder="password" required />
</Form.Field> 
            
<Button type="submit" color="black">Signup</Button>
            </Form>
            </div>
        
           
        );
    }


    async handleSubmit(event){

        event.preventDefault();

      
        let formData = { 
            email: this.state.email,
            username: this.state.username,
            name: this.state.name,
            password: this.state.password,
            phone_number:this.state.phone

        }

        console.log(formData);


        const response= await axios(
            {url: 'http://localhost:5000/sign-up' ,
            method:'POST', 
        // mode: "no-cors",
            data: formData
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
    async HandleemailChange(event){
        this.setState({
            email: event.target.value
        });

    }
    async HandleusernameChange(event){
        this.setState({
            username: event.target.value
        });

    }
    async HandlephoneChange(event){
        this.setState({
            phone: event.target.value
        });

    }
    async HandlepasswordChange(event){
        this.setState({
            password: event.target.value
        });

    }
    async componentDidMount(){
       
          


    }
        
}



export default Signup1;