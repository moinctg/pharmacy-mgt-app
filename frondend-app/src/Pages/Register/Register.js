import React, { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import { Button, Modal, NavLink } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './Register.css';
import useAuth from '../../hooks/useAuth';

const Register = () => {
    const [registerFromData ,  setRegisterFromData] = useState({})
    const {  isLoading, authError ,registerUser, modal, setModal, user } = useAuth();

    const handleOnChange = e => {
        const field = e.target.name
        const value = e.target.value
        const newLogindata = {...registerFromData}
        newLogindata[field] = value
        console.log(newLogindata)
        setRegisterFromData(newLogindata)
    }
    const handleRegisterSubmit = e => {
        e.preventDefault()
        registerUser(registerFromData.email,registerFromData.password,registerFromData.name,useNavigate)
        console.log(registerUser)
    }
    return (
        <div className='Container mt-5'>
            <Modal show={modal}>
        <Modal.Header>
          <Modal.Title>Registration Successful !</Modal.Title>
        </Modal.Header>
        <Modal.Body>Hello Mr./Ms. {user?.displayName} You have successfully registered !</Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={ ()=>setModal(false)}>
            <Link style={{color:'white',textDecoration:'none'}} to="/">Go To Home</Link>
          </Button>
        </Modal.Footer>
      </Modal>
     
	<div class="login-header box-shadow">
		<div class="container-fluid d-flex justify-content-between align-items-center">
			<div class="brand-logo">
				<a href="login.html">
					<img src="vendors/images/deskapp-logo.svg" alt=""/>
				</a>
			</div>
			<div class="login-menu">
				<ul>
					<li><a href="login.html">Login</a></li>
				</ul>
			</div>
		</div>
	</div>
	<div class="register-page-wrap d-flex align-items-center flex-wrap justify-content-center">
		<div class="container">
			<div class="row align-items-center">
				<div class="col-md-6 col-lg-7">
					<img src="vendors/images/register-page-img.png" alt=""/>
				</div>
				<div class="col-md-6 col-lg-5">
					<div class="register-box bg-white box-shadow border-radius-10">
						<div class="wizard-content">
							<form class="tab-wizard2 wizard-circle wizard">
								<h5>Basic Account Credentials</h5>
								<section>
									<div class="form-wrap max-width-600 mx-auto">
										<div class="form-group row">
											<label class="col-sm-4 col-form-label">Email Address*</label>
											<div class="col-sm-8">
												<input type="email" class="form-control"/>
											</div>
										</div>
										<div class="form-group row">
											<label class="col-sm-4 col-form-label">Username*</label>
											<div class="col-sm-8">
												<input type="text" class="form-control"/>
											</div>
										</div>
										<div class="form-group row">
											<label class="col-sm-4 col-form-label">Password*</label>
											<div class="col-sm-8">
												<input type="password" class="form-control"/>
											</div>
										</div>
										<div class="form-group row">
											<label class="col-sm-4 col-form-label">Confirm Password*</label>
											<div class="col-sm-8">
												<input type="password" class="form-control"/>
											</div>
										</div>
									</div>
								</section>
								{/* <!-- Step 2 --> */}
								<h5>Personal Information</h5>
								<section>
									<div class="form-wrap max-width-600 mx-auto">
										<div class="form-group row">
											<label class="col-sm-4 col-form-label">Full Name*</label>
											<div class="col-sm-8">
												<input type="text" class="form-control"/>
											</div>
										</div>
										<div class="form-group row align-items-center">
											<label class="col-sm-4 col-form-label">Gender*</label>
											<div class="col-sm-8">
												<div class="custom-control custom-radio custom-control-inline pb-0">
													<input type="radio" id="male" name="gender" class="custom-control-input"/>
													<label class="custom-control-label" for="male">Male</label>
												</div>
												<div class="custom-control custom-radio custom-control-inline pb-0">
													<input type="radio" id="female" name="gender" class="custom-control-input"/>
													<label class="custom-control-label" for="female">Female</label>
												</div>
											</div>
										</div>
										<div class="form-group row">
											<label class="col-sm-4 col-form-label">City</label>
											<div class="col-sm-8">
												<input type="text" class="form-control"/>
											</div>
										</div>
										<div class="form-group row">
											<label class="col-sm-4 col-form-label">State</label>
											<div class="col-sm-8">
												<input type="text" class="form-control"/>
											</div>
										</div>
									</div>
								</section>
								<div class="row">
								<div class="col-sm-12">
									<div class="input-group mb-0">
									
											<input class="btn btn-primary btn-lg btn-block" type="submit" value="Sign In"/>
									
										{/* <a class="btn btn-primary btn-lg btn-block" href="index.html">Sign In</a> */}
									</div>
									</div>
									

								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	


      <form className='form' onSubmit={handleRegisterSubmit} > 
    <div className='main-form p-3'>
      <h2>Create an Account</h2>
      <div className='form-group p-3'>
          <label htmlFor="name">First Name:</label>
          <input
           type="text"
            name='first'
            className="form-control input" 
             id='first'
             onBlur={handleOnChange}
             required
            />
      </div>
      <div className='form-group p-3'>
          <label htmlFor="name">Last Name:</label>
          <input
           type="text"
            name='last'
            className="form-control input" 
             id='last'
             onBlur={handleOnChange}
             required
            />
      </div>
      <div className='form-group p-3'>
          <label htmlFor="email">Username or Email:</label>
          <input
           onBlur={handleOnChange} 
            type="email"
             name='email'
             id="inputEmail3"
              className="form-control input"
               required />
      </div>
      <div className='form-group p-3'>
          <label htmlFor="password">Password:</label>
          <input
           onBlur={handleOnChange} 
           className="form-control input"
           type="password"
            name='password'
            id="inputPassword3"
             
              required />
      </div>
      <div className='form-group p-3'>
          <label htmlFor="password">Re-Type-Password:</label>
          <input
           onBlur={handleOnChange} 
           className="form-control input"
           type="password"
            name='password'
            id="inputPassword3"
              required />
      </div>
      
      <input  type="submit" value='Create an Account' />
      <NavLink as={Link} to='/login'  >Already Have Account ? Login </NavLink>
      {/* <button type="button" class="btn btn-button btn-lg btn-block">Block level button</button>   */}
  </div>
</form>
 <p className=' text-center'>-----------Or--------</p>
<div className='text-center'>
    <p className='  border-right-3 rounded-circle'><a href="#" class="fa fa-facebook"></a> Continue with Facebook</p>

  <p className=' border-right-0 rounded-circle'><a href="#" class="fa fa-google"></a> Continue with Google </p>
</div>
            
            
            
            
        </div>
    );
};

export default Register;