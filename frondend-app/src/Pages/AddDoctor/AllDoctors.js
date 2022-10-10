import React, { useEffect, useState } from 'react';
import AllDoctor from './AllDoctor';

const AllDoctors = () => {
    const [doctor,setDoctor] = useState([])

    useEffect( () =>{
        fetch('http://127.0.0.1:8000/api/doctor/')
        .then(res=>res.json())
        .then(data=> setDoctor(data))

    }
        ,[])
    return (
        <div>

            {

                doctor.map(doctors=><AllDoctor
                
                 key={doctors._id}
                 doctors={doctors}
                ></AllDoctor>)
            }
            
        </div>
    );
};

export default AllDoctors;