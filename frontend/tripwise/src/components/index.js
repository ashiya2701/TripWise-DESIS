import React from "react";
import './navBar.css';
import { Link } from 'react-router-dom';
const HomeBody = () => {
return (
	<div>

		<div className="navbar">
		<h3>TripWise </h3>
			<Link to={'/home'} className="link">
			Home
			</Link>
					<Link to={'/login'} className="link">
			Login
			</Link>
			<Link to={'/signup'} className="link">
			SignUp
			</Link>
		</div>

		

		
	</div>
	
);
}

export default HomeBody;
