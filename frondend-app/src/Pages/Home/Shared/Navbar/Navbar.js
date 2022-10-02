import 'bootstrap/dist/css/bootstrap.min.css';
import logo from '../../../../images/logo.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {  faShoppingCart, faUserCircle  } from '@fortawesome/free-solid-svg-icons';
import './Navbar.css';
import useAuth from '../../../../hooks/useAuth';
import { Nav,Button} from 'react-bootstrap';
import { Link, NavLink } from 'react-router-dom';

import React from 'react';

const Navbar = () => {

  const element = <FontAwesomeIcon icon={faShoppingCart} />
  const icon =<FontAwesomeIcon icon={faUserCircle} />

  const { user, logOut } = useAuth()
    return (
        <div className="container">
        
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
  <a className="navbar-brand"  href="#"></a>
  <img src={logo} alt="" height={'50px'} width={'100px'}></img>
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span className="navbar-toggler-icon"></span>
  </button>
  <div className="collapse navbar-collapse d-flex flex-row-reverse" id="navbarNav">
    <ul className="navbar-nav  p-3">
      <li className="nav-item active ">
        {/* <a className="nav-link" href="#">Home <span className="sr-only"></span></a> */}
        <Nav.Link  className="nav-link" as={Link} to="/home">Home</Nav.Link>
      </li>
      <li className="nav-item">
        {/* <Link className='nave-link' to="/portfolio" >Our Portfolio</Link> */}
        <Nav.Link  className="nav-link" as={Link} to="/portfolio">Portfolio</Nav.Link>
     
      </li>
      <li className="nav-item">
        {/* <Link className="nav-link" to="/ourteam">Our Team <Link/> */}
        <Nav.Link  className="nav-link" as={Link} to="/ourteam">Our Team</Nav.Link>
        </li>
      <li className="nav-item">
       
        {/* <Link className='nave-link' to="/contact" >Contact us</Link> */}
        <Nav.Link  className="nav-link" as={Link} to="/contact">Contact</Nav.Link>
      </li>
      {/* <li className="nav-item nav">
      <Nav.Link  className="nav-link" as={Link} to="/login">Login</Nav.Link>
      </li>
        */}

      <a>
            {
              user ?.email ?
               <>
               {user?.displayName} {icon} <Button onClick={ logOut }>Logout</Button>
               <li className="nav-item">
       
        {/* <Link className='nave-link' to="/contact" >Contact us</Link> */}
        <Nav.Link  className="nav-link" as={Link} to="/dashboard">Dashboard</Nav.Link>
      </li>
                </>
               
               : <Nav.Link className='nav' as={Link} to="/login">Login</Nav.Link>
            }
            
          </a>
      
    </ul>
  </div>
</nav>
          
        </div>
    );
};

export default Navbar;