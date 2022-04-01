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

class Hotels extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            name:"",
            hotelsPrice:[],
            hotelsDistanceFromAirport:[],
            hotelsDistanceFromRailways:[],
            hotelsTimeFromAirport:[],
            hotelsTimeFromRailways:[]
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

                <Button type="submit" color="black">Give Hotel Suggestion</Button>
            </Form>

            <div>

            Price:

            {this.state.hotelsPrice.map((hotel) => {
                return(
                    <div key= {hotel.id}>
                    Name: {hotel.name} &nbsp; &nbsp;
                    Price: {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} &nbsp; &nbsp;
                    Distance From Railways: {hotel.distancefromrailways} &nbsp; &nbsp;
                    Time from Airport: {hotel.timefromairport} &nbsp; &nbsp;
                    Time from Railways: {hotel.timefromrailways} &nbsp; &nbsp;


                    </div>
                );

            })
            
            }


            <br/>
            <br/>
            <br/>
            Distance From Airport:


            {this.state.hotelsDistanceFromAirport.map((hotel) => {
                return(
                    <div key= {hotel.id}>
                    Name: {hotel.name} &nbsp; &nbsp;
                    Price: {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} &nbsp; &nbsp;
                    Distance From Railways: {hotel.distancefromrailways} &nbsp; &nbsp;
                    Time from Airport: {hotel.timefromairport} &nbsp; &nbsp;
                    Time from Railways: {hotel.timefromrailways} &nbsp; &nbsp;


                    </div>
                );

            })
            
            }

            <br/>
            <br/>
            <br/>

            Distance From Railways:

            {this.state.hotelsDistanceFromRailways.map((hotel) => {
                return(
                    <div key= {hotel.id}>
                    Name: {hotel.name} &nbsp; &nbsp;
                    Price: {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} &nbsp; &nbsp;
                    Distance From Railways: {hotel.distancefromrailways} &nbsp; &nbsp;
                    Time from Airport: {hotel.timefromairport} &nbsp; &nbsp;
                    Time from Railways: {hotel.timefromrailways} &nbsp; &nbsp;


                    </div>
                );

            })
            
            }

            <br/>
            <br/>
            <br/>

            Time from Airport:

            {this.state.hotelsTimeFromAirport.map((hotel) => {
                return(
                    <div key= {hotel.id}>
                    Name: {hotel.name} &nbsp; &nbsp;
                    Price: {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} &nbsp; &nbsp;
                    Distance From Railways: {hotel.distancefromrailways} &nbsp; &nbsp;
                    Time from Airport: {hotel.timefromairport} &nbsp; &nbsp;
                    Time from Railways: {hotel.timefromrailways} &nbsp; &nbsp;


                    </div>
                );

            })
            
            }

            <br/>
            <br/>
            <br/>

            Time from Railways:


            {this.state.hotelsTimeFromRailways.map((hotel) => {
                return(
                    <div key= {hotel.id}>
                    Name: {hotel.name} &nbsp; &nbsp;
                    Price: {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} &nbsp; &nbsp;
                    Distance From Railways: {hotel.distancefromrailways} &nbsp; &nbsp;
                    Time from Airport: {hotel.timefromairport} &nbsp; &nbsp;
                    Time from Railways: {hotel.timefromrailways} &nbsp; &nbsp;


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

        console.log("abc")

        const response= await axios(
            {url: 'http://localhost:5000/hotels?CityName='+this.state.name ,
            method:'GET',
            }
        )
        .then(        
        )
        .catch(err => {
            
        })

        console.log(response.data)

        this.setState({
            hotelsPrice:response.data.price,
            hotelsDistanceFromAirport:response.data.distancefromairport,
            hotelsDistanceFromRailways:response.data.distancefromrailways,
            hotelsTimeFromAirport:response.data.timefromairport,
            hotelsTimeFromRailways:response.data.timefromrailways,
        })
        
    }
    
    async componentDidMount(){
        


    }
        
}
export default Hotels;