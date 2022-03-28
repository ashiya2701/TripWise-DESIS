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
            group_details:{
                desc: "",
                id:"",
                name:"",
                members:[],
            },
            expense_logs:[],
            user_final_logs:[],
            name:"",
            desc:"",
            paid_for:[],
            user_list:[],
            amount:0,
        };
    }

    renderRedirect= () =>{
       
    }

    render(){
        return(

            <div>

                Group name: {this.state.group_details.name} &nbsp;
                Group description: {this.state.group_details.desc} &nbsp;
                <br/>

                Members:

                {this.state.group_details.members.map((member) => {
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

            <Form onSubmit={event => this.handleSubmit(event)} >

                <Form.Field >
                    <Input type="text" value={this.state.desc} onChange={event => this.HandleDescChange(event)} placeholder="Expense description" required />
                </Form.Field>

                <Form.Field >
                    <Input type="number" value={this.state.amount} onChange={event => this.HandleAmountChange(event)} placeholder="Expense amount" required />
                </Form.Field>

                <Form.Field>

                    <Dropdown
                        placeholder='Members'
                        options={this.state.user_list}
                        fluid multiple selection
                        onChange={(event,data) =>this.handleGroupMemberChange(event , data)
                        }
                    />
                </Form.Field>

                <Button color="black">Create new transaction</Button>
            </Form>

            </div> 
        );
    }

    handleGroupMemberChange(event, data){

        this.setState({
            paid_for: data.value
        });
        
    }

    HandleDescChange(event){
        this.setState({
            desc: event.target.value
        });

    }

    HandleAmountChange(event){
        this.setState({
            amount: event.target.value
        });

    }

    async handleSubmit(event){

        event.preventDefault();

        // eslint-disable-next-line no-restricted-globals
        const params= new URLSearchParams(location.search);
        const id= params.get("id");
      
        let formData = { 
            description: this.state.desc,
            amount:  this.state.amount,
            paid_for: this.state.paid_for
        }

        console.log(formData);

        const response= await axios(
            {url: 'http://localhost:5000/expense_logs/create/'+id,
            method:'POST', 
            data: formData,
            headers: {'access-token': cookies.get('token_splitwise') }
            }
        )
        .then(        
        
        )
        .catch(err => {
            
        })
        console.log(response)
        console.log(response.data)
    
    }
    
    async componentDidMount(){

        // eslint-disable-next-line no-restricted-globals
        const params= new URLSearchParams(location.search);
        const id= params.get("id");

        const response= await axios(
            {url: 'http://localhost:5000/group/'+id,
            method:'GET',
            headers: {'access-token': cookies.get('token_splitwise') }
            }
        )
        .then(        
        
        )
        .catch(err => {
            
        })

        console.log(response)

        this.setState({
            group_details: response.data.group_details
        })

        this.setState({
            expense_logs: response.data.expense_logs
        })

        this.setState({
            user_final_log: response.data.user_final_log
        })


        let user_list= []
                
        for(let u in response.data.group_details.members){
            
            let dict = {};
            dict["key"] = response.data.group_details.members[u]["id"];
            dict["value"] = response.data.group_details.members[u]["id"];
            // dict["label"] = response.data[u]["username"];
            dict["text"] = response.data.group_details.members[u]["username"];

            user_list.push(dict);
        }

        this.setState({
            user_list:user_list
        })

        console.log(this.state.user_list)     

    }
        
}
export default Group;