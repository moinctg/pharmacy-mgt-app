import React, { useState, useEffect } from 'react';
import SingleStock from './SingleStock';

const AllStock = () => {
    const [stock,setStock] = useState([])

   useEffect( ()=>{

      fetch('http://127.0.0.1:8000/api/stock/')
      .then(res=>res.json())
      .then(data=>setStock(data))

   }
    ,[])

    return (
        <div>
            {
                stock.map(stocks=><SingleStock
                    key={stocks._id}
                    stocks={stocks}
                ></SingleStock>)
            }
        </div>
    );
};

export default AllStock;