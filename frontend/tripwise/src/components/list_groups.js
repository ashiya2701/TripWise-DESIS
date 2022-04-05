import React, {Component} from 'react';
import axios from 'axios';
import {Button, Form , Modal, Icon, Input, Card, Feed} from 'semantic-ui-react';
import { Dropdown } from 'semantic-ui-react'
import Cookies from 'universal-cookie';
import {Link} from 'react-router-dom';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const cookies = new Cookies();


class ListGroups extends Component{
    constructor(props)
    {
        super(props);
        this.state = { 
            groups:[]
            
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(
            <div>

            {this.state.groups.map((group) => {
                return(
                    <div key= {group.id}>
                    Group name: {group.name} &nbsp;
                    Group description: {group.desc} &nbsp;
                    <br/>

                    Members:

                    {group.members.map((member) => {
                        return(
                            <div key= {member.id}>
                            Name: {member.name} &nbsp;
                            Username: {member.username} &nbsp;
                            Email: {member.email} &nbsp;
                            Phone number: {member.phoneNumber} &nbsp;
                            </div>
                        );
                        })
                    }

                    <></>

                    <br/>
                    <br/>
                    <br/>

                    <Button type="submit" color="black"><Link to={"/Group?id="+group.id}>Check in</Link></Button>
                                    
                    </div>
                );
                })
            }

                        
            
            </div> 
        );
    }

    async openGroup(group_id){

        // console.log(data.value)
        
        
    }
    
    async componentDidMount(){

        const response= await axios(
            {url: 'http://localhost:5000/group/list' ,
            method:'GET',
            headers: {'access-token': cookies.get('token_splitwise') }
            }
        )
        .then(        
        
        )
        .catch(err => {
            
        })
        
        if(response===undefined||response.status!=200){
            alert("Couldn't fetch your data, either you are not logged in or an error occured");
        }
        console.log(response) 
        this.setState({
            groups: response.data

        })
        
        console.log(response.data)

    }
        
}
export default ListGroups;