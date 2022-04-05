import React, {Component} from 'react';
import {Button} from 'semantic-ui-react';
import axios from 'axios';

class Itinerary extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            answer:[]
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(

            <div>

            <h3>Itinerary</h3>
            <Button type="submit" color="black" onClick={()=>this.generateItinerary(this.props.destination)}>Generate Itinerary</Button>
            <div>

            {this.state.answer.map((place) => {
                return(
                    <div key= {place[0]}>
                        
                        {place[1]}
                        &nbsp;
                        ({place[2]}
                        &nbsp;,
                        {place[3]})
                        <br/>
                        |
                        <br/>
                        v        

                    </div>
                );

            })
            
            }
            </div>
            </div> 
        );
    }

    async generateItinerary(city){
      
        let formData = { 
            cityName: city
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