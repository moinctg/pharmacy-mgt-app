import React from 'react';
import { Link, Outlet,NavLink  } from 'react-router-dom';
import { Button, Nav, Tab } from 'react-bootstrap';
import LeftSideBar from '../../../Components/LeftSideBar/LeftSideBar';
import Dashboard from '../../../Components/Dashboard/Dashboard';
import Footer from '../../../Components/Footer/Footer';
import TopBanner from '../../../Components/TopBanner/TopBanner';

// import { Link, Outlet } from 'react-router-dom';
// // import './Dashboard.css'
// import useAuth from '../../../hooks/useAuth';


const AdminDashboard = () => {
    // const { admin } = useAuth()
    // const handleSrawerToggle = () => {
    //     setMobileOpen(!mobileOpen)
    // }


    // const book = <FontAwesomeIcon icon={faShoppingCart} />
    // const singout = <FontAwesomeIcon icon={faSignOutAlt} />
    // const { user, logOut } = useAuth();
    return (
        <div>
			<TopBanner></TopBanner>
			<LeftSideBar></LeftSideBar>
			{/* <Dashboard></Dashboard> */}
            <div className="border">
			<Outlet/>
		    <Footer></Footer>

		

			</div>
            
	
	
	
    </div>
        
    );
};

export default AdminDashboard;