import React from 'react';
import './Allhospital.css'
const AllHospital = ( { hospital } ) => {

     console.log(hospital);
     const { id, name, address,location} = hospital;
    return (
        <div className="container">
            <div className="table">
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Address</th>
                        <th>Locations</th>
                    </tr>
                    <tr>
                        <td>{id}</td>
                        <td>{name}</td>
                        <td>{address}</td>
                        <td>{location}</td>
                    </tr>

                </table>
             
            </div>


            </div>
        
    );
};

export default AllHospital;