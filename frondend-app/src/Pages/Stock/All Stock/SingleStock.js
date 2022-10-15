import React from 'react';

const SingleStock = ( {stocks}) => {
    console.log(stocks);
    const {id,name,price,purchase_date,quntity,sub_total,waranty} = stocks;
    return (
        <div>
              <div className="table">
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Midecine Name</th>
                        <th>price</th>
                        <th>purchase_date</th>
                        <th>Quntity</th>
                        <th>sub_total</th>
                        <th>waranty</th>
                    </tr>
                    <tr>
                        <td>{id}</td>
                        
                        <td>{name}</td>
                        <td>{price}</td>
                        <td>{purchase_date}</td>
                        <td>{quntity}</td>
                        <td>{sub_total}</td>
                        <td>{waranty}</td>
                       
                    
                   
                          </tr>

                </table>
            
        </div>
        </div>
    );
};

export default SingleStock;