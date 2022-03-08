import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Signup1 from "./components/Signup1";
import Template from "./components/Template";
import Login from './components/Login';
import Logout from './components/Logout';
import Itinerary from './components/Itinerary';

function App() {
return (
	<Router>
	<Routes>

		<Route path='/Signup1' element={<Signup1/>} />
		<Route path='/login' element={<Login/>} />
		<Route path='/logout' element={<Logout/>} />
		<Route path='/itinerary' element={<Itinerary/>} />
    	<Route path='/Template' element={<Template/>} />
	</Routes>
	</Router>
);
}

export default App;
