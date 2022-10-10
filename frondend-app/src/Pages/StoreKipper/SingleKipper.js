import React from 'react';

const SingleKipper = ({ kipers }) => {
    console.log(kipers)
    const { id, name, address, contact, nid, join_date, Salary } = kipers;
    return (
        <div>
            <div className="table">
                <table>
                    <tr>
                        <th>ID</th>
                        <th> Name</th>
                        <th>Address</th>
                        <th>Contact</th>
                        <th>NID</th>
                        <th>Join Date</th>
                        <th>Salary</th>
                    </tr>
                    <tr>
                        <td>{id}</td>
                        <td>{name}</td>
                        <td>{address}</td>
                        <td>{contact}</td>
                        <td>{nid}</td>
                        <td>{join_date}</td>
                        <td>{Salary}</td>
                     
                    </tr>

                </table>

            </div>
        </div>
    );
};

export default SingleKipper;