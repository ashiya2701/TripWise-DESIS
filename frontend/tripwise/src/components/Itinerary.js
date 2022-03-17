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

class Itinerary extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            name:"",
            answer:[]
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(

            <div>

            <Form onSubmit={event => this.handleSubmit(event)} >
                <Form.Field >
                    <Input type="text" value={this.state.name} onChange={event => this.HandlenameChange(event)} placeholder="city name" required />
                </Form.Field>

                <Button type="submit" color="black">Generate Itinerary</Button>
            </Form>

            <div>

            {this.state.answer.map((place) => {
                return(
                    <div key= {place[0]}>
                        
                        Name: {place[1]}
                        &nbsp;
                        x-coordinate: {place[2]}
                        &nbsp;
                        y-coordinate: {place[3]}



                    </div>
                );

            })
            
            }
            </div>
            </div> 
        );
    }

    async HandlenameChange(event){
        this.setState({
            name: event.target.value
        });

    }


    async handleSubmit(event){

        event.preventDefault();
      
        let formData = { 
            cityName: this.state.name 
        }

        console.log(formData);

        const response= await axios(
            {url: 'http://localhost:5000/generate_itinerary' ,
            method:'POST', 
            data: formData
            }
        )
        .then(        
        
        )
        .catch(err => {
            
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
export default Itinerary;