import React, { useState } from 'react';
import { Button, Modal, NavLink } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './Register.css';
import useAuth from '../../hooks/useAuth';

const Register = () => {
    const [registerFromData ,  setRegisterFromData] = useState({})
    const history = useHistory();
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
        registerUser(registerFromData.email,registerFromData.password,registerFromData.name,history)
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