import React, { useEffect, useState } from 'react';
import AllDoctor from '../All Doctor/AllDoctor';

const AllDoctors = () => {
    const [doctor,setDoctor] = useState([])

    useEffect( () =>{
        fetch('http://127.0.0.1:8000/api/doctor/')
        .then(res=>res.json())
        .then(data=> setDoctor(data))

    }
        ,[])
    return (
        <div className='main-container'>
            
             
            
        <div className="card-box mb-30">
        <h2 className="h4 pd-20"> ALL Doctors Information </h2>
       
            {

                doctor.map(doctors=><AllDoctor
                
                 key={doctors._id}
                 doctors={doctors}
                ></AllDoctor>)
            }
           
        </div>
        </div>
      
        
    );
};

export default AllDoctors;