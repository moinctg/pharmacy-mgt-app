import React from 'react';


const AllPaitent = ( {paitents}) => {
    console.log(paitents)

    const {id,name,address,contact,details,gender,doctor_id} = paitents;
    return (
        <div className="container  position-absolute top-50 start-50 ">
            <div className="table">
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Address</th>
                        <th>Contact</th>
                        <th>Gender </th>
                        <th>Details </th>
                        <th>Doctor ID </th>
                    </tr>
                    <tr>
                        <td>{id}</td>
                        <td>{name}</td>
                        <td>{address}</td>
                        <td>{contact}</td>
                        <td>{gender}</td>
                        <td>{details}</td>
                        <td>{doctor_id}</td>
                    </tr>

                </table>
             
            </div>

            
        </div>
    );
};

export default AllPaitent;