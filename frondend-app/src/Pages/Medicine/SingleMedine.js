import React from 'react';
import './medicine.css';

const SingleMedine = ({medicines} ) => {
    console.log(medicines)
    const {id,mfg,name,price,quntity,exp_date} = medicines
    return (
        <div>
            <div className="table">
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Manfacture Date</th>
                        <th>Midecine Name</th>
                        <th>price</th>
                        <th>Quntity</th>
                        
                        <th>Exp Date</th>
                    </tr>
                    <tr>
                        <td>{id}</td>
                        <td>{mfg}</td>
                        <td>{name}</td>
                        <td>{price}</td>
                        <td>{quntity}</td>
                        <td>{exp_date}</td>
                    </tr>

                </table>
             
            </div>
        </div>
    );
};

export default SingleMedine;