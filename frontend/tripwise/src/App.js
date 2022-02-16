import React from 'react';
import './App.css';
import Navbar from './components';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
// import Home from './pages';
// import Login from './pages/login';
import SignUp1 from './pages/Signup1';
// import HomeBody from './components';

function App() {
return (
	<Router>
	<Routes>

		<Route path='/Signup1' element={<SignUp1/>} />
	</Routes>
	</Router>
);
}

export default App;
