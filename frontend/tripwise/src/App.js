import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Signup1 from "./components/Signup1";
import Template from "./components/Template";
import Login from './components/Login';
import Logout from './components/Logout';

// /home/ishu/Desktop/desis/project/TripWise-DESIS/frontend/tripwise/src/components/Signup1.js

function App() {
return (
	<Router>
	<Routes>

		<Route path='/Signup1' element={<Signup1/>} />
		<Route path='/login' element={<Login/>} />
		<Route path='/logout' element={<Logout/>} />
    	<Route path='/Template' element={<Template/>} />
	</Routes>
	</Router>
);
}

export default App;
