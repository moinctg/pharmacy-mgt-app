import React from 'react';
import { Link, Outlet,NavLink  } from 'react-router-dom';

const LeftSideBar = () => {
    return (
        <div>
         <div className="left-side-bar">
		<div className="brand-logo">
			<a href="#">
				<img src="vendors/images/Green.png" alt="" className="dark-logo"/>
				<img src="vendors/images/deskapp-logo-white.svg" alt="" className="light-logo"/>
			</a>
			<div className="close-sidebar" data-toggle="left-sidebar-close">
				<i className="ion-close-round"></i>
			</div>
		</div>
	
		<div className="menu-block customscroll">
			<div className="sidebar-menu">
				<ul id="accordion-menu">
				
					<li className="dropdown">
						<NavLink to  ="/home" className="dropdown-toggle">
							<span className="micon dw dw-house-1"></span>
							{/* <NavLink  to="/adddoctor">Adding Doctor</NavLink></li> */}
							<span className="mtext">Home</span>
						</NavLink>
						
					</li>
					<li className="dropdown">
						<a href="javascript:;" className="dropdown-toggle">
							<span className="micon dw dw-edit2"></span><span className="mtext">Input Forms </span>
						</a>
						<ul className="submenu">
						<li><NavLink  to="/adddoctor">Adding Doctor</NavLink></li>
						<li><NavLink  to="/addhospital">Adding Hospital</NavLink></li>
						<li><NavLink  to="/addpaitent">Adding Paitent</NavLink></li>
										{/* <Routes>
											<Route path="/" element={<Dashboard />}>
												<Route
													path="messages"
													element={<DashboardMessages />}
												/>
												<Route path="tasks" element={<DashboardTasks />} />
											</Route>
										</Routes> */}
							
						</ul>
					</li>
					<li className="dropdown">
						<a href="javascript:;" className="dropdown-toggle">
							<span className="micon dw dw-library"></span><span className="mtext">Report</span>
						</a>
						<ul className="submenu">
							<li><NavLink  to="/alldoctor">Doctor List</NavLink></li>
							<li><NavLink  to="/allhospital">Hospital  List</NavLink></li>
							<li><NavLink  to="/allpaitent">Paitent   List</NavLink></li>
							
						</ul>
					</li>
					
					
				
					<li className="dropdown">
						<a href="javascript:;" className="dropdown-toggle">
							<span className="micon dw dw-analytics-21"></span><span className="mtext">Charts</span>
						</a>
						<ul className="submenu">
							<li><a href="highchart.html">Highchart</a></li>
							<li><a href="knob-chart.html">jQuery Knob</a></li>
							<li><a href="jvectormap.html">jvectormap</a></li>
							<li><a href="apexcharts.html">Apexcharts</a></li>
						</ul>
					</li>
					<li className="dropdown">
						<a href="javascript:;" className="dropdown-toggle">
							<span className="micon dw dw-right-arrow1"></span><span className="mtext">Additional Pages</span>
						</a>
						<ul className="submenu">
							<li><a href="video-player.html">Video Player</a></li>
							<li><a href="login.html">Login</a></li>
							<li><a href="forgot-password.html">Forgot Password</a></li>
							<li><a href="reset-password.html">Reset Password</a></li>
						</ul>
					</li>
				

					
					
					<li>
						<a href="sitemap.html" className="dropdown-toggle no-arrow">
							<span className="micon dw dw-diagram"></span><span className="mtext">Sitemap</span>
						</a>
					</li>
					<li>
						<a href="chat.html" className="dropdown-toggle no-arrow">
							<span className="micon dw dw-chat3"></span><span className="mtext">Chat</span>
						</a>
					</li>
					<li>
						<a href="invoice.html" className="dropdown-toggle no-arrow">
							<span className="micon dw dw-invoice"></span><span className="mtext">Invoice</span>
						</a>
					</li>
					<li>
						<div className="dropdown-divider"></div>
					</li>
					
					
				</ul>

			</div>
		</div>
	</div>
        </div>
    );
};

export default LeftSideBar;