import React from 'react';
import './App.css';
import Navbar from './components';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Home from './pages';
import Login from './pages/login';
import SignUp from './pages/signup';
import HomeBody from './components';

function App() {
return (
	<Router>
    <HomeBody/>
	<Routes>
	<Route path='/' element={<Home/>} />

	<Route path='/home' element={<Home/>} />
		<Route path='/login' element={<Login/>} />
		<Route path='/signup' element={<SignUp/>} />
	</Routes>
	</Router>
);
}

export default App;
