import React from 'react';
import './Testimonials.css';
import img1 from '../../../../images/Image/Ellipse 90.png';
import img2 from '../../../../images/Image/Ellipse 91.png';
import img3 from '../../../../images/Image/Ellipse 92.png';


const Testomonials = () => {
    return (
        <div className='Container mt-5'>
            <h1 className='text-center'>Testimonials</h1>
            <div  className='row '>
                <div className='col-md-4 flex-d'>
                   <div> <img src={img1} width={'64'} height={'64'} alt=""></img>   
                    </div>
                    <div>Nash Patrik <br/>
                    CEO</div>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Purus commodo ipsum duis laoreet maecenas. Feugiat </p>                
                </div>
                <div className='col-md-4'>
                <img src={img2} width={'64'} height={'64'} alt=""></img>  
                <div>Nash Patrik <br/>
                    CEO</div>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Purus commodo ipsum duis laoreet maecenas. Feugiat </p>                
                </div>

                
                <div className='col-md-4'>
                <img src={img3}width={'64'} height={'64'} alt=""></img>  
                <div>Nash Patrik <br/>
                    CEO</div>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Purus commodo ipsum duis laoreet maecenas. Feugiat </p>                
                </div>
                
                


               
            </div>
        </div>
    );
};

export default Testomonials;