import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Signup1 from "./components/Signup1";
import HotelSuggestion from "./components/HotelSuggestion";

// /home/ishu/Desktop/desis/project/TripWise-DESIS/frontend/tripwise/src/components/Signup1.js

function App() {
return (
	<Router>
	<Routes>

		<Route path='/Signup1' element={<Signup1/>} />
    <Route path='/HotelSuggestion' element={<HotelSuggestion/>} />
	</Routes>
	</Router>
);
}

export default App;
