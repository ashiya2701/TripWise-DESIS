import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
// import { Component } from 'react/cjs/react.production.min';
import { useLocation } from 'react-router-dom';
// import { CookiesProvider, withCookies, Cookies} from 'react-cookie'
import Cookies from 'universal-cookie';
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
            answer: []
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(

            <div>
            <h3>Flight Suggestion</h3>
            <Button type="submit" color="black" onClick={()=>this.handleSubmit()}>Find Best Route</Button>
    
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
    

    async handleSubmit(event){

        // let formData= {"source": this.state.source, "dest": this.state.dest} 
        

        // console.log(formData);
        const response= await axios(
            {url: 'http://localhost:5000/generate_plan?source='+this.props.source+'&dest='+this.props.destination,
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