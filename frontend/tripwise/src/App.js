import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';

import Group from './components/group';
import Hotels from './components/hotels'
import Planner from './components/planner';

// /home/ishu/Desktop/desis/project/TripWise-DESIS/frontend/tripwise/src/components/Signup1.js
import Landing from './components/Landing';
import TripPLanning from './components/TripPlanning';
import Splitwise from './components/Splitwise';
import LoginSignUp from './components/LoginSignUp';

function App() {
return (
	<Router>
	<Routes>

		
		<Route path='/generate_plan' element={<Planner/>} />
		<Route path='/' element={<Landing/>}/>
		<Route path='/TripPlanning' element={<TripPLanning/>}/>
		<Route path='/Splitwise' element={<Splitwise/>}/>
		<Route path='/LoginSignUp' element={<LoginSignUp/>}/>
		<Route path='/Group' element={<Group/>}/>
	</Routes>
	</Router>
);
}

export default App;