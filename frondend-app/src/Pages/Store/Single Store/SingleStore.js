import React from 'react';

const SingleStore = ( {stores}) => {
    console.log(stores)
    const {id,name,address,contact,location,store_kiper}= stores;
    return (
        <div>
            <div className="table">
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Branch Name</th>
                        <th>Address</th>
                        <th>Contact</th>
                        <th>Locations</th>
                        <th>Store Officer</th>
                     
                    </tr>
                    <tr>
                        <td>{id}</td>
                        
                        <td>{name}</td>
                  
                        <td>{address}</td>
                        <td>{contact}</td>
                        <td>{location}</td>
                        <td>{store_kiper}</td>
                       
                    
                   
                          </tr>

                </table>
                </div>
            
            
        </div>
    );
};

export default SingleStore;