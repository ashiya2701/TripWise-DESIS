import React, {Component} from 'react';
import axios from 'axios';
import {Button} from 'semantic-ui-react';

class Hotels extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
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

            <h3>Hotel Suggestion</h3>
            <Button type="submit" color="black" onClick={()=>this.getHotelSuggestions(this.props.destination)}>Give Hotel Suggestion</Button>
            <div>

            Price:

            {this.state.hotelsPrice.map((hotel) => {
                return(
                    <div key= {hotel.id}>
                    Name: {hotel.name} &nbsp; &nbsp;
                    Price: Rs. {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} km &nbsp; &nbsp; 
                    Distance From Railways: {hotel.distancefromrailways} km &nbsp; &nbsp; 
                    Time from Airport: {hotel.timefromairport} hr &nbsp; &nbsp; 
                    Time from Railways: {hotel.timefromrailways} hr &nbsp; &nbsp; 
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
                    Price: Rs. {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} km &nbsp; &nbsp; 
                    Distance From Railways: {hotel.distancefromrailways} km &nbsp; &nbsp; 
                    Time from Airport: {hotel.timefromairport} hr &nbsp; &nbsp; 
                    Time from Railways: {hotel.timefromrailways} hr &nbsp; &nbsp; 
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
                    Price: Rs. {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} km &nbsp; &nbsp; 
                    Distance From Railways: {hotel.distancefromrailways} km &nbsp; &nbsp; 
                    Time from Airport: {hotel.timefromairport} hr &nbsp; &nbsp; 
                    Time from Railways: {hotel.timefromrailways} hr &nbsp; &nbsp; 
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
                    Price: Rs. {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} km &nbsp; &nbsp; 
                    Distance From Railways: {hotel.distancefromrailways} km &nbsp; &nbsp; 
                    Time from Airport: {hotel.timefromairport} hr &nbsp; &nbsp; 
                    Time from Railways: {hotel.timefromrailways} hr &nbsp; &nbsp; 
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
                    Price: Rs. {hotel.price} &nbsp; &nbsp;
                    Distance From Airport: {hotel.distancefromairport} km &nbsp; &nbsp; 
                    Distance From Railways: {hotel.distancefromrailways} km &nbsp; &nbsp; 
                    Time from Airport: {hotel.timefromairport} hr &nbsp; &nbsp; 
                    Time from Railways: {hotel.timefromrailways} hr &nbsp; &nbsp; 
                    </div>
                );

            })
            
            }
            </div>
            
            </div> 
        );
    }

    async getHotelSuggestions(city){


        console.log("abc")

        const response= await axios(
            {url: 'http://localhost:5000/hotels?CityName='+city,
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