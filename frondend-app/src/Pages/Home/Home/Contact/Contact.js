import React from 'react';

const Contact = () => {
    return (
        <div className='Container mt-5'>
            <h1 className='text-center'>Let us handle your <br/> 
project, professionally.</h1>
<div class="row g-3 h-50">
  <div class="col-md-6">
    <input type="text" class="form-control" placeholder="First name" aria-label="First name"/>
  </div>
  <div class="col-md-6">
    <input type="text" class="form-control" placeholder="Last name" aria-label="Last name"/>
  </div>
  <div class="row g-3">
  <div class="col-md-6">
    <input type="text" class="form-control" placeholder="Email" aria-label="Email "/>
  </div>
  <div class="col-md-6">
    <input type="text" class="form-control" placeholder="phone" aria-label="phone"/>
  </div>
  </div>
  <div class="row g-3">
  <div class="col-md-12">
    <input type="text" class="form-control" placeholder="phone" aria-label="address"/>
  </div>
  </div>
</div>


        </div>
    );
};

export default Contact;