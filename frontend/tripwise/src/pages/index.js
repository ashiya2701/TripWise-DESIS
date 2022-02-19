import React from 'react';
import './style.css';
const Home = () => {
return (
	<div>
	<div>
	<h1 className='heading'>Wanna plan a trip?<br/>
	Let we help you !
	</h1></div>
	<div className="row">
			<div className="column1">
				<h2>Column 1</h2>
				<img src="https://th.bing.com/th/id/OIP.ulnhmjk6rTHgxaS_qBJbPQHaHa?pid=ImgDet&rs=1"/>
			</div>
			<div className="column2" >
				<div className = "first">
				<div className = "second">TripWise</div>
				<div className = "second">Suggestions</div>
				<div className = "second">Itenary</div>
				<div className = "second">SplitWise</div>
				</div>
			</div>
		</div>
	</div>
);
};

export default Home;

// import React from "react";
// // import { Nav, NavLink, NavMenu }
// // 	from "./NavbarElements";
// import './navBar.css';
// import { Link } from 'react-router-dom';
// const Navbar = () => {
// return (
// 	<div>
	
// 		<div className="navbar">
// 			<Link to={'/home'} className="link">
// 			Home
// 			</Link>
// 					<Link to={'/login'} className="link">
// 			Login
// 			</Link>
// 			<Link to={'/signup'} className="link">
// 			SignUp
// 			</Link>
// 		</div>

// 		<div className="row">
// 			<div className="column">
// 				<h2>Column 1</h2>
// 				<p>Some text..</p>
// 			</div>
// 			<div className="column" >
// 				<div className = "first">
// 				<div className = "second">First</div>
// 				<div className = "second">second</div>
// 				<div className = "second">third</div>
// 				<div className = "second">four</div>
// 				<div className = "second">five</div>
// 				</div>
// 			</div>
// 		</div>

		
// 	</div>
	
// );
// };

// export default Navbar;

