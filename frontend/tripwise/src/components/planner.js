import React, {Component} from 'react';
import {Button} from 'semantic-ui-react'
import axios from 'axios';

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
                        Fastest Route: 
                        {this.convertToRoute(y[1])}
                        &nbsp;,
                        Total Time: {y[0]} hr
                        &nbsp;
                        <br/>
                        Cheapest Route: 
                        {this.convertToRoute(y[1])}
                        &nbsp;,   
                        Total Price : Rs. {y[2]}
                        &nbsp;                   

                    </div>
                );

            })
            
            }
            </div>
            </div>
           
        );
    } 
    
    convertToRoute(y){
        var s = ""; 
        for(var i=0;i<y.length-1;i++)
            s+=y[i][1]+" - >";
        s+=y[y[1].length-1][1];
        return s;
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