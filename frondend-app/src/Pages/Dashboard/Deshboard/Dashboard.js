import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faShoppingCart, faUserCircle, faHome, faSignOutAlt } from '@fortawesome/free-solid-svg-icons';
import logo from './../../../images/logo.png';
import { Link, Outlet } from 'react-router-dom';
import './Dashboard.css'
import useAuth from '../../../hooks/useAuth';

import { Button } from 'react-bootstrap';

function Dashboard(props) {
    const { window } = props
    const [mobileOpen, setMobileOpen] = React.useState(false)
    const { admin } = useAuth()
    const handleSrawerToggle = () => {
        setMobileOpen(!mobileOpen)
    }


    const book = <FontAwesomeIcon icon={faShoppingCart} />
    const singout = <FontAwesomeIcon icon={faSignOutAlt} />
    const { user, logOut } = useAuth();



    return <div className='conatainer'>
        <div className='row'>

            <div className='col-md-3 col-lg-3'>
                <img src={logo} height={'50px'} width={'100px'} alt="" />

                <div className='sidebar-container'>

                    <ul className='text-center text '>
                        <li>
                            <Link to='/book' className='dashboard-menu' >
                                <span className='logo-style' >{book}</span>
                                Book</Link>
                        </li>
                        <li>
                            <Link to='/bookinglist' className='dashboard-menu' >
                                <span className='logo-style' >{book}</span>
                                Bookking List</Link>
                        </li>
                        <li>
                            <Link to={`/dashboard/addadmin`} className='dashboard-menu' >

                                <span className='logo-style' >{}</span>
                                Admin</Link>
                        </li>
                        <li>
                            <Link to={`/dashboard/addproduct`} className='dashboard-menu' >
                                <span className='logo-style' >{}</span>
                                addProduct</Link>
                        </li>

                        <li>
                            <Link to={`/dashboard/review`} className='dashboard-menu' >
                                <span className='logo-style' >{}</span>
                                Review</Link>
                        </li>








                    </ul>
                </div>
            </div>
            <div className='col-md-9 col-lg-9'>
                <div className='row'>
                    <div className='col-lg-6 mt-5'>
                        <h4>Service List</h4>
                        <div className='row'>
                            <div className='col-lg-6'>
                                <div class="card ">
                                    <img class="card-img-top" src="..." alt="Card image cap" />
                                    <div class="card-body">
                                        <h5 class="card-title">Card title</h5>
                                        <p class="">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                    
                                    </div>
                                </div>

                            </div>
                            <div className='col-lg-6'>
                                <div class="card">
                                    <img class="card-img-top" src="..." alt="Card image cap" />
                                    <div class="card-body">
                                        <h5 class="card-title">Card title</h5>
                                        <p class="">This card has supporting text below as a natural lead-in to additional content.</p>
                                        
                                    </div>
                                </div>

                            </div>
                        </div>
                        <div class="card-deck">



                        </div>

                    </div>
                    <div className='col-lg-6'>
                        <li>

                            <span className='logo-style' >{singout}</span>
                            <Button onClick={logOut}>LogOut</Button>

                        </li>


                    </div>
                </div>
                <Outlet></Outlet>


            </div>
        </div>
    </div>;





}

export default Dashboard;
