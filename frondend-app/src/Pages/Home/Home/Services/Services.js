import React from 'react';
import './Service.css';
import img1 from '../../../../images/Icon/Group 1373.png';
import img2 from '../../../../images/Icon/Group 1372.png';
import img3 from '../../../../images/Icon/Group 1374.png';

const Services = () => {
    return (
        <div className='Container mt-6'>
            <div className='row mt-4'>
                <h3 className='text-center'>Our Awesome  <span className='header'>Services</span> </h3>
                <div className='col-md-4 mt-4'>

                    <div class="card">
                        <img class=" img" src={img1} height={'42px'} width={'42'} alt="Card image cap" />
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                        </div>

                    </div>
                </div>
                <div className='col-md-4 mt-4'>


                    <div class="card">
                        <img class="img " src={img2} height={'42px'} width={'42'} alt="Card image cap" />
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                        </div>

                    </div>
                </div>
                <div className='col-md-4 mt-4'>


                    <div class="card">
                        <img class="img " src={img3} height={'42px'} width={'42'} alt="Card image cap" />
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                        </div>

                    </div>




                </div>


            </div>
            <div className='btn  button mt-5'>Explore More</div>








        </div>
    );
};

export default Services;