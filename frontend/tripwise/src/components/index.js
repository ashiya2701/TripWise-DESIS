// import React from 'react';
// import ReactDOM from 'react-dom';
// // import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';
// import 'semantic-ui-css/semantic.min.css';

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
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