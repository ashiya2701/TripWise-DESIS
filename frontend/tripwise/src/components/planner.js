import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
// import { Component } from 'react/cjs/react.production.min';
import { useLocation } from 'react-router-dom';
import { CookiesProvider, withCookies, Cookies} from 'react-cookie'
import axios from 'axios';
import {Button, Form , Input,} from 'semantic-ui-react'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();

class Planner extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            source:"",
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
            <Input type="text" value={this.state.source} onChange={event => this.HandlesourceChange(event)} placeholder="source" required />
            </Form.Field>
            <Form.Field >
            <Input type="text" value={this.state.dest} onChange={event => this.HandledestChange(event)} placeholder="dest" required />
            </Form.Field>
                        
            <Button type="submit" color="black">Find Best Route</Button>
            </Form>
          
            <div>

            {this.state.answer.map((y) => {
                return(
                    <div key= {y[0]}>
                        Total Time: {y[0]}
                        &nbsp;
                        Fastest Route: {y[1]}
                        &nbsp;
                        Total Price : {y[2]}
                        &nbsp;
                        Cheapest Route: {y[1]}


                       

                    </div>
                );

            })
            
            }
            </div>
            </div>
           
        );
    }
      
    async HandlesourceChange(event){
        this.setState({
            source: event.target.value
           // console.log(source);
        });
        

    }
    async HandledestChange(event){
        this.setState({
            dest: event.target.value
          
        });
      //  console.log(dest);

    }
    

    async handleSubmit(event){

        event.preventDefault();

        // let formData= {"source": this.state.source, "dest": this.state.dest} 
        

        // console.log(formData);
        const response= await axios(
            {url: 'http://localhost:5000/generate_plan?source='+this.state.source+'&dest='+this.state.dest,
            method:'GET', 
        // mode: "no-cors",S
           // data: formData
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
        console.log("abc")

        // const response= await axios(
        //     {url: 'http://localhost:5000/generate_plan?source=Delhi&dest=Mumbai',
        //     method:'POST',
        //     }
        // )
        // .then(        
        // )
        // .catch(err => {
        //     console.log(err)
            
        // })
        // console.log(response.data)
       
        
    }
        
}



export default Planner;