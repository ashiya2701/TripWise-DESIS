import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Signup1 from "./components/Signup1";
import Template from "./components/Template";
import Login from './components/Login';
import Logout from './components/Logout';
import Itinerary from './components/Itinerary';
import CreateGroup from './components/create_group'
import ListGroups from './components/list_groups'
import Group from './components/group';
import Hotels from './components/hotels'
import Landing from './components/Landing';
import TripPLanning from './components/TripPlanning'

function App() {
return (
	<Router>
	<Routes>
		<Route path='/' element={<Landing/>} />
		<Route path='/TripPlanning' element={<TripPLanning/>}/>
		<Route path='/Signup1' element={<Signup1/>} />
		<Route path='/login' element={<Login/>} />
		<Route path='/logout' element={<Logout/>} />
		<Route path='/itinerary' element={<Itinerary/>} />
    	<Route path='/Template' element={<Template/>} />
		<Route path='/CreateGroup' element={<CreateGroup/>} />
		<Route path='/ListGroups' element={<ListGroups/>} />
		<Route path='/group' element={<Group/>} />
		<Route path='/hotel' element={<Hotels/>} />
	</Routes>
	</Router>
);
}

export default App;
