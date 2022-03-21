import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
// import { Component } from 'react/cjs/react.production.min';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import {Button, Form , Modal, Icon, Dropdown, Input, Card, Feed} from 'semantic-ui-react';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();

class planner extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            src:"",
            dest:"",
            answer: []
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
            
            <div>

            {this.state.answer.map((route) => {
                return(
                    <div key= {route[0]}>
                        
                        Name: {route[1]}
                        &nbsp;
                        x-coordinate: {route[2]}
                        &nbsp;
                        y-coordinate: {route[3]}



                    </div>
                );

            })
            
            }
            </div>
            </div>
           
        );
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

    async handleSubmit(event){

        event.preventDefault();

        let data= {"src": this.state.src, "dest": this.state.dest} 
        

        console.log(formData);
        const response= await axios(
            {url: 'http://localhost:5000/planner' ,
            method:'GET', 
        // mode: "no-cors",S
            data: FormData
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
        console.log(response.data)

        this.setState({
            answer: response.data
        });
        

       
    }
  
    
    async componentDidMount(){
       
        
    }
        
}



export default planner;