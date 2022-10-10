import React, { useEffect, useState } from 'react';
import SingleMedine from './SingleMedine';

const AllMedicine = () => {
    const [medicine,setMidicine] = useState([])

    useEffect( ()=>{
        fetch("http://127.0.0.1:8000/api/medicine/")
        .then(res=>res.json())
        .then(data=>setMidicine(data))
    }
        ,[])
    return (
        <div>
            <h1>This is ALL Midicine List</h1>
            {
               medicine.map(medicines=><SingleMedine
               key={medicines._id}
               medicines={medicines}
               
               ></SingleMedine>)
            }
        </div>
    );
};

export default AllMedicine;