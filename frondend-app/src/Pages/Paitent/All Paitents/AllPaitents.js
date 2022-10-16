import React from 'react';
import { useState, useEffect } from 'react';
import AllPaitent from '../All Paitent/AllPaitent';

const AllPaitents = () => {
    const [paitent, SetPaitent] = useState([])

    useEffect(
        () => {

            fetch('http://127.0.0.1:8000/api/patient/')
                .then(res => res.json())
                .then(data => SetPaitent(data))
        }
        , [])
    return (

        <div className='main-container'>
            <div className="card-box mb-30">
                <h2 className="h4 pd-20 text-center"> ALL Paitents Information </h2>
                

                  {
                
                paitent.map(paitents=><AllPaitent
                
                 key={paitents._id}
                 paitents={paitents}
                ></AllPaitent>)
            } 

                    {/* {
                        paitent?.map(pd=>
                       <
                    } */}





               
            </div>
        </div>

    );
};

export default AllPaitents;