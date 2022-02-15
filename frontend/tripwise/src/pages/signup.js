import React from 'react';
import { useState } from "react";
import ReactDOM from "react-dom";
import './style.css';
const SignUp = () => {

	const [userRegistration,setuserRegistration]=useState({
 
		Name:"",
		email:"",
		state:"",
		username:"",
		phone:"",
		password:"",
	});
	const [records,setRecords]=useState([]);
	const HandleInput=(e)=>{
   const name=e.target.name;
   const value=e.target.value;
   console.log(name,value);
   setuserRegistration({ ...userRegistration,[name]:value});

	}

	const handleSubmit=(e)=>{
		e.preventDefault();
		const newRecord={...userRegistration,id:new Date().getTime().toString()}
		console.log(records);
		setRecords([...records,newRecord]);
		console.log(records);

	}
return (
	<div>
	<form className='form' action="" onSubmit={handleSubmit}>
	<div>
	<label className='formfield' htmlFor='Name'>Name</label>
	<input className='formvalue' type="text" name="Name"  id="Name"
	value={userRegistration.Name} onChange={HandleInput}/>
	</div>
	<div>
	<label className='formfield' htmlFor='email'>Email</label>
	<input className='formvalue' type="email" name="email"  id="email"
	 value={userRegistration.email} onChange={HandleInput}/>
	</div>
	<div>
	<label className='formfield' htmlFor='state'>State</label>
	<input className='formvalue' type="text" name="state"  id="state"
	value={userRegistration.state} onChange={HandleInput}/>
	</div>
	<div>
	<label className='formfield' htmlFor='username'>Username</label>
	<input className='formvalue' type="text" name="username"  id="username"
	value={userRegistration.username} onChange={HandleInput}/>
	</div>


	<div>
	<label className='formfield' htmlFor='phone'>Phone No</label>
	<input className='formvalue' type="text" name="phone"  id="phone"
	value={userRegistration.phone} onChange={HandleInput}/>
	</div>
	<div>
	<label className='formfield' htmlFor='password'>Password</label>
	<input className='formvalue' type="password" name="password"  id="password"
	value={userRegistration.password} onChange={HandleInput}/>
	</div>
	<button className='button' type='submit'>Submit
	
	</button>
	</form>

	
</div>
	
	
);
};

export default SignUp;

