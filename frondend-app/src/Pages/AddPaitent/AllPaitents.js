import React from 'react';
import { useState,useEffect } from 'react';
import AllPaitent from './AllPaitent';

const AllPaitents = () => {
    const [paitent,SetPaitent] = useState([])

    useEffect(
         ()=>{

        fetch('http://127.0.0.1:8000/api/patient/')
        .then(res=>res.json())
        .then(data=>SetPaitent(data))
         }
        ,[])
    return (
        <div>

            {
                paitent.map(paitents=><AllPaitent
                
                 key={paitents._id}
                 paitents={paitents}
                ></AllPaitent>)
            }
            
        </div>
    );
};

export default AllPaitents;