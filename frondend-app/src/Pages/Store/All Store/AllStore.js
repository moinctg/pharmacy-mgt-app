import React, { useEffect, useState } from 'react';
import SingleStore from './SingleStore';

const AllStore = () => {
  const [store,setStore] = useState([])

    useEffect ( ()=>{
        fetch('http://127.0.0.1:8000/api/store/')
        .then(res=>res.json())
        .then(data=>setStore(data))
    }
        ,[])
     return (
        <div>
            {
                store.map(stores=><SingleStore
                key={stores._id}
                stores={stores}
                ></SingleStore>)
            }
            
        </div>
    );
};

export default AllStore;