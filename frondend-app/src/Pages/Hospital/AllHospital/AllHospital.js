import React from 'react';
import './Allhospital.css'
const AllHospital = ( { hospital } ) => {

     console.log(hospital);
     const { id, name, address,location} = hospital;
    return (
         <div>
            <table className="data-table table nowrap">
                <thead>
                    <tr>
                        <th className="table-plus datatable-nosort"></th>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Address</th>
                        <th>Locations</th>
                        <th className="datatable-nosort">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td className="table-plus">
                            {/* <img src="vendors/images/product-1.jpg" width="70" height="70" alt=""/> */}
                        </td>
                        <td>
                            <h5 className="font-16">
                                  {id}
                            </h5>
                            
                        </td>
                        <td>{id}</td>
                        <td>{name}</td>
                        <td>{address}</td>
                        <td>{location}</td>
                        <td>
                            <div className="dropdown">
                                <a className="btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle" href="#" role="button" data-toggle="dropdown">
                                    <i className="dw dw-more"></i>
                                </a>
                                <div className="dropdown-menu dropdown-menu-right dropdown-menu-icon-list">
                                    <a className="dropdown-item" href="#"><i className="dw dw-eye"></i> View</a>
                                    <a className="dropdown-item" href="#"><i className="dw dw-edit2"></i> Edit</a>
                                    <a className="dropdown-item" href="#"><i className="dw dw-delete-3"></i> Delete</a>
                                </div>
                            </div>
                        </td>
                    </tr>
                 
                </tbody>
            </table>
       


            </div>
        
    );
};

export default AllHospital;