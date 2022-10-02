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
        <form className="form" onSubmit={handleLoginSubmit} >
            <div className='main-form p-3'>
                <h2>Login With </h2>
                
                <div className='form-group'>
                    <label htmlFor="email">Email:</label>
                    <input 
                    type="email"
                     name="email"
                     className="form-control input"
                     
                      id="inputEmail3"
                       onBlur={handleOnBlur}  label="email" 
                       required/>
                </div>
                <div className='form-group'>
                    <label htmlFor="password">Password:</label>
                    <input
                     className="form-control input"
                     type="password" 
                     name='password' 
                     id="inputPassword3"
                     onBlur={handleOnBlur } label='password'
                     required />
                </div>
               
                <input className="input" type="submit" value='LOGIN' /> <br/>
                  <p className="text-center">--------Or--------</p>
                <button className="" onClick={handleGoogleSignIn}><img style={{width:'30px', marginLeft:'30px'}} src={google} alt="" /></button>
                
                    <NavLink as={Link} to='/register' >Don't have account? create an account</NavLink>
                   
                
            </div>
        </form>
        </div>
    );
};

export default Login;