import React from 'react';
import './AllDoctor.css'

const AllDoctor = ( {doctors}) => {

    console.log(doctors)
    const {id,name,address,contact,hospital_id} = doctors
    
    return (
      
            <div className="container">
            <div className="table">
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Address</th>
                        <th>Contact</th>
                        <th>Hospital </th>
                    </tr>
                    <tr>
                        <td>{id}</td>
                        <td>{name}</td>
                        <td>{address}</td>
                        <td>{contact}</td>
                        <td>{hospital_id}</td>
                    </tr>

                </table>
             
            </div>

            
        </div>
    );
};

export default AllDoctor;