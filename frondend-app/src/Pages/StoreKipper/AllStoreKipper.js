import React, { useEffect, useState } from 'react';
import SingleKipper from './SingleKipper';

const AllStoreKipper = () => {
    const [kiper,setKipper] = useState([])
    useEffect( ()=>{
        fetch("http://127.0.0.1:8000/api/storekipeer/")
        .then(res=>res.json())
        .then(data=>setKipper(data))
    }
        ,[])
    return (
        <div>
            {
                kiper.map(kipers=><SingleKipper
                key={kipers._id}
                kipers={kipers}
                ></SingleKipper>)
            }
            
        </div>
    );
};

export default AllStoreKipper;