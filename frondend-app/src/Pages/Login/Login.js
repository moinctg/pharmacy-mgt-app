import React, { useState } from 'react';
import {  Button, Modal, NavLink, } from 'react-bootstrap';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Link, useNavigate } from 'react-router-dom';
import google from '../../images/google.png';
import './Login.css'
import { useLocation } from 'react-router-dom';
import useAuth from '../../hooks/useAuth';

const Login = () => {
    const [loginFromData ,  setLoginFromData] = useState({})
    const {user, loginUser, signInWithGoogle, isLoading, authError, modal, setModal } = useAuth()
    console.log(signInWithGoogle);
    const location = useLocation();
    const navigator = useNavigate();
    // const history = useHistory();

    const handleOnBlur = e => {
        const field = e.target.name
        const value = e.target.value
        const newLogindata = {...loginFromData}
        newLogindata[field] = value
        setLoginFromData(newLogindata)
    }

    const handleLoginSubmit = e => {
      loginUser(loginFromData.email, loginFromData.password, location, navigator);
      e.preventDefault();
  }

  const handleGoogleSignIn = () => {
    signInWithGoogle(location, navigator)
}

    return (
        <div className='container mt-5'>
           <Modal show={modal}>
        <Modal.Header>
          <Modal.Title>Login Successful !</Modal.Title>
        </Modal.Header>
        <Modal.Body>Hello Mr./Ms. {user?.displayName} You have successfully logged in !</Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={ ()=>setModal(false)}>
            <Link style={{color:'white',textDecoration:'none'}} to="/">Go To Home</Link>
          </Button>
        </Modal.Footer>
      </Modal>


      <div class="login-header box-shadow">
		<div class="container-fluid d-flex justify-content-between align-items-center">
			<div class="brand-logo">
				<Link to  ="/login">
					<img src="images/Green.png" alt=""/>
				</Link>
			</div>
			<div class="login-menu">
				<ul>
					{/* <li><Link to ="/register">Register</Link></li> */}
				</ul>
			</div>
		</div>
	</div>
	<div class="login-wrap d-flex align-items-center flex-wrap justify-content-center">
		<div class="container">
			<div class="row align-items-center">
				<div class="col-md-6 col-lg-7">
					<img src="vendors/images/login-page-img.png" alt=""/>
				</div>
				<div class="col-md-6 col-lg-5">
					<div class="login-box bg-white box-shadow border-radius-10">
						<div class="login-title">
							<h2 class="text-center text-primary">Login To Green Pharmacy App</h2>
						</div>
						<form onSubmit={handleLoginSubmit}>
							<div class="select-role">
								<div class="btn-group btn-group-toggle" data-toggle="buttons">
									<label class="btn active">
										<input type="radio" name="options" id="admin"/>
										<div class="icon"><img src="vendors/images/briefcase.svg" class="svg" alt=""/></div>
										<span>I'm</span>
										Manager
									</label>
									<label class="btn">
										<input type="radio" name="options" id="user"/>
										<div class="icon"><img src="vendors/images/person.svg" class="svg" alt=""/></div>
										<span>I'm</span>
										Employee
									</label>
								</div>
							</div>
							<div class="input-group custom">
								<input type="email" class="form-control form-control-lg" placeholder="Email "/>
								<div class="input-group-append custom"  name="email" id="inputEmail3"
                       onBlur={handleOnBlur}  required>
									<span class="input-group-text"><i class="icon-copy dw dw-user1"></i></span>
								</div>
							</div>
							<div class="input-group custom">
								<input type="password" class="form-control form-control-lg" placeholder="**********"/>
								<div class="input-group-append custom"  name='password' 
                     id="inputPassword3"
                     onBlur={handleOnBlur }
                     required >
									<span class="input-group-text"><i class="dw dw-padlock1"></i></span>
								</div>
							</div>
							<div class="row pb-30">
								<div class="col-6">
									<div class="custom-control custom-checkbox">
										<input type="checkbox" class="custom-control-input" id="customCheck1"/>
										<label class="custom-control-label" for="customCheck1">Remember</label>
									</div>
								</div>
								<div class="col-6">
									<div class="forgot-password"><a href="forgot-password.html">Forgot Password</a></div>
								</div>
							</div>
							<div class="row">
								<div class="col-sm-12">
									<div class="input-group mb-0">
									
											<input class="btn btn-primary btn-lg btn-block" type="submit" value="Sign In"/>
									
										{/* <a class="btn btn-primary btn-lg btn-block" href="index.html">Sign In</a> */}
									</div>
									{/* <div class="font-16 weight-600 pt-10 pb-10 text-center" data-color="#707373">OR</div>
									<div class="input-group mb-0">
										<Link  class="btn btn-outline-primary btn-lg btn-block"  to ="/register">Register To Create Account</Link>
									</div> */}
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
       </div>
      
       
    );
};

export default Login;