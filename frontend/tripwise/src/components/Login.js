import React, {Component} from 'react';
import axios from 'axios';
import {Button, Form, Input} from 'semantic-ui-react';
import Cookies from 'universal-cookie';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();

class Login extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            username:"",
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
                <Input type="text" value={this.state.username} onChange={event => this.HandleusernameChange(event)} placeholder="Username" required /></Form.Field>

                <Form.Field >
                <Input type="password" value={this.state.password} onChange={event => this.HandlepasswordChange(event)} placeholder="Password" required />
                </Form.Field> 
                            
                <Button type="submit" color="black">Login</Button>
            </Form>
            </div>
        
           
        );
    }


    async handleSubmit(event){

        event.preventDefault();
      
        let formData = { 
            username: this.state.username,
            password: this.state.password,
        }

        console.log(formData);


        const response= await axios(
            {url: 'http://localhost:5000/login' ,
            method:'POST', 
            data: formData
            }
        )
        .then( 
        // console.log("request.. ")
        
        )
        .catch(err => {
            // console.log(err)
            // console.log("request!!!!")
        })
        console.log(response)
        console.log(response.data)

        cookies.set('token_splitwise', response.data , { path: '/' });

        console.log(cookies.get('token_splitwise'));
    }
    
    async HandleusernameChange(event){
        this.setState({
            username: event.target.value
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



export default Login;