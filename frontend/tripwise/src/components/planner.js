import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
// import { Component } from 'react/cjs/react.production.min';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import {Button, Form , Modal, Icon, Dropdown, Input, Card, Feed} from 'semantic-ui-react';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class Template extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            src:"",
            dest:"",
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(

            <div>
            <Form onSubmit={event => this.handleSubmit(event)} >
            <Form.Field >
            <Input type="text" value={this.state.src} onChange={event => this.HandleSrcChange(event)} placeholder="Src" required />
            </Form.Field>
            <Form.Field >
            <Input type="text" value={this.state.dest} onChange={event => this.HandleDestChange(event)} placeholder="Dest" required />
            </Form.Field>
                        
            <Button type="submit" color="black">Find Best Route</Button>
            </Form>
            </div>
        
           
        );
    }


    async handleSubmit(event){

        event.preventDefault();

        let data= {"src": this.state.src, "dest": this.state.dest} 
        


        const response= await axios(
            {url: 'http://localhost:5000/planner' ,
            method:'GET', 
        // mode: "no-cors",S
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
    
    async HandleSrcChange(event){
        this.setState({
            src: event.target.value
        });

    }
    async HandleDestChange(event){
        this.setState({
            dest: event.target.value
        });

    }
    
    async componentDidMount(){
       
        
    }
        
}



export default Template;