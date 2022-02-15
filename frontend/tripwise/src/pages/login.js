import React from "react";
import { useState } from "react";
import ReactDOM from "react-dom";
import './style.css';
const Login = () => {
	const [userRegistration,setuserRegistration]=useState({
		username:"",
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
	<label className='formfield' htmlFor='username'>Username</label>
	<input className='formvalue' type="text" name="username"  id="username"
	value={userRegistration.username} onChange={HandleInput}/>
	</div>
	<div>
	<label className='formfield' htmlFor='password'>Password</label>
	<input className='formvalue' type="password" name="password"  id="password"
	value={userRegistration.password} onChange={HandleInput}/>
	</div>
	<button className='button' type='submit'>Submit</button>
	</form>
	</div>
);
};

export default Login;
