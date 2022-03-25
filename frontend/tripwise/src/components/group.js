import React, {Component} from 'react';
import axios from 'axios';
import {Button, Form , Modal, Icon, Input, Card, Feed} from 'semantic-ui-react';
import { Dropdown } from 'semantic-ui-react'
import Cookies from 'universal-cookie';
// import { useLocation } from 'react-router-dom';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();


class Group extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(

            <div>

            {/* <Form onSubmit={event => this.handleSubmit(event)} >

                <Form.Field >
                    <Input type="text" value={this.state.name} onChange={event => this.HandleNameChange(event)} placeholder="group name" required />
                </Form.Field>

                <Form.Field >
                    <Input type="text" value={this.state.desc} onChange={event => this.HandleDescChange(event)} placeholder="group description" required />
                </Form.Field>

                <Form.Field>

                    <Dropdown
                        placeholder='Members'
                        options={this.state.users}
                        fluid multiple selection
                        onChange={(event,data) =>this.handleGroupMemberChange(event , data)
                        }
                    />
                </Form.Field>

                <Button type="submit" color="black">Create group</Button>
            </Form> */}

            
            </div> 
        );
    }

    // async handleGroupMemberChange(event, data){

    //     console.log(data.value)

    //     this.setState({
    //         selected_members: data.value
    //     });
        
    // }


    // async HandleNameChange(event){
    //     this.setState({
    //         name: event.target.value
    //     });

    // }

    // async HandleDescChange(event){
    //     this.setState({
    //         desc: event.target.value
    //     });

    // }

    async handleSubmit(event){

        // event.preventDefault();
      
        // let formData = { 
        //     groupName: this.state.name,
        //     groupDesc:  this.state.desc,
        //     Members: this.state.selected_members
        // }

        // console.log(formData);

        // const response= await axios(
        //     {url: 'http://localhost:5000/group/create' ,
        //     method:'POST', 
        //     data: formData,
        //     headers: {'access-token': cookies.get('token_splitwise') }
        //     }
        // )
        // .then(        
        
        // )
        // .catch(err => {
            
        // })
        // console.log(response)
        // console.log(response.data)

        // this.setState({
        //     answer: response.data
        // });
        
    }
    
    async componentDidMount(){

        // eslint-disable-next-line no-restricted-globals
        const params= new URLSearchParams(location.search);
        const id= params.get("id");

        const response= await axios(
            {url: 'http://localhost:5000/group/1' ,
            method:'GET',
            headers: {'access-token': cookies.get('token_splitwise') }
            }
        )
        .then(        
        
        )
        .catch(err => {
            
        })

        console.log(response)

        // let user_list= []
                
        // for(let u in response.data){
            
        //     let dict = {};
        //     dict["key"] = response.data[u]["id"];
        //     dict["value"] = response.data[u]["id"];
        //     // dict["label"] = response.data[u]["username"];
        //     dict["text"] = response.data[u]["username"];

        //     user_list.push(dict);
        // }

        // this.setState({
        //     users:user_list
        // })

        // console.log(this.state.users)     

    }
        
}
export default Group;