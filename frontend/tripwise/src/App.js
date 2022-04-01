import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Signup1 from "./components/Signup1";
import Template from "./components/Template";
import Planner from './components/planner';

// /home/ishu/Desktop/desis/project/TripWise-DESIS/frontend/tripwise/src/components/Signup1.js

function App() {
return (
	<Router>
	<Routes>

		<Route path='/Signup1' element={<Signup1/>} />
    	<Route path='/Template' element={<Template/>} />
		<Route path='/generate_plan' element={<Planner/>} />
	</Routes>
	</Router>
);
}

export default App;
