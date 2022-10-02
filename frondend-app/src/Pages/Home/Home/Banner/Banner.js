import React from 'react';
import './Banner.css';
import img from '../../../../images/Image/beautiful-young-asian-woman-touching-her-clean-face-with-fresh-healthy-skin-isolated-white-wall-beauty-cosmetics-facial-treatment-concept 1.png';

const Banner = () => {
    return (
        <div className='Container mt-5'>
            <div className='row '>
                <div className='col-md-6 p-5 '>
                    <h1 className='banner-head'>BEAUTY SALON <br />
                        FOR EVERY WOMEN
                    </h1>
                    <p className='pt-3'>
                        Lorem ipsum dolor sit amet, consectetur adipiscing <br/>
                       elit. Purus commodo ipsum duis laoreet maecenas. Feugiat
                    </p>
                    <div className='btn banner-button'>Get an Appointment</div>

                </div>
                <div className='col-md-6 '>
                    <img src={img} width={'484px'} height={'478px'} alt=""></img>

                </div>
            </div>

        </div>
    );
};

export default Banner;