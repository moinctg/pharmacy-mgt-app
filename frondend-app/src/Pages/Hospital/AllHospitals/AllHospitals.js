import React, { useEffect, useState } from 'react';
import AllHospital from '../AllHospital/AllHospital';

const AllHospitals = () => {
    const [hospitals,setHospitals] = useState([])

    useEffect(()=>{
        fetch('http://127.0.0.1:8000/api/hospital/')
        .then(res=> res.json())
        .then(data => setHospitals(data))


    },[])
    return (
        <div>
            {
                
                hospitals.map(hospital=> <AllHospital

                key={hospital._id}
                hospital={hospital}
                

    
                
                
                ></AllHospital>)
            }
            
        </div>
    );
};

export default AllHospitals;