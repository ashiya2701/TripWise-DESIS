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
            state:"",
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
<Input type="text" value={this.state.state} onChange={event => this.HandlestateChange(event)} placeholder="state" required /></Form.Field>
<Form.Field >
<Input type="text" value={this.state.username} onChange={event => this.HandleusernameChange(event)} placeholder="Username" required /></Form.Field>
<Form.Field >
<Input type="text" value={this.state.phone} onChange={event => this.HandlephoneChange(event)} placeholder="phone" required /></Form.Field>
<Form.Field >
<Input type="password" value={this.state.password} onChange={event => this.HandlepasswordChange(event)} placeholder="password" required />
</Form.Field> 
            
<Button type="submit" color="black">Create Project</Button>
            </Form>
            </div>
        
           
        );
    }


    async handleSubmit(event){
        event.preventDefault();

        // console.log(Cookies.get("csrftoken"));
        
        let formData = { 
            name: this.state.name,
            email: this.state.email ,
            // state:this.state.state ,
            username: this.state.username,
            phone_number: this.state.phone,
            password: this.state.password

        }

        console.log(formData);

        const response= await axios({url:'http://127.0.0.1:5000/login/' ,
        method:'POST', 
        data:formData , 
        withCredentials:true, 
        headers: {"Content-Type": "application/json", }})
        .then(
        console.log("request.. ")
        
        )
        .catch(err => {
           console.log("request!!!!")
        })

        console.log(response);

      

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
    async HandlestateChange(event){
        this.setState({
            state: event.target.value
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