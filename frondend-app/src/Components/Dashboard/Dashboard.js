import React from 'react';

const Dashboard = () => {
    return (
        <div>
        <div className="mobile-menu-overlay"></div>

<div className="main-container">
    <div className="pd-ltr-20">
        <div className="card-box pd-20 height-100-p mb-30">
            <div className="row align-items-center">
                <div className="col-md-4">
                    <img src="vendors/images/banner-img.png" alt=""/>
                </div>
                <div className="col-md-8">
                    <h4 className="font-20 weight-500 mb-10 text-capitalize">
                        Welcome back <div className="weight-600 font-30 text-blue">Johnny Brown!</div>
                    </h4>
                    <p className="font-18 max-width-600">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde hic non repellendus debitis iure, doloremque assumenda. Autem modi, corrupti, nobis ea iure fugiat, veniam non quaerat mollitia animi error corporis.</p>
                </div>
            </div>
        </div>
        <div className="row">
            <div className="col-xl-3 mb-30">
                <div className="card-box height-100-p widget-style1">
                    <div className="d-flex flex-wrap align-items-center">
                        <div className="progress-data">
                            <div id="chart"></div>
                        </div>
                        <div className="widget-data">
                            <div className="h4 mb-0">2020</div>
                            <div className="weight-600 font-14">Contact</div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="col-xl-3 mb-30">
                <div className="card-box height-100-p widget-style1">
                    <div className="d-flex flex-wrap align-items-center">
                        <div className="progress-data">
                            <div id="chart2"></div>
                        </div>
                        <div className="widget-data">
                            <div className="h4 mb-0">400</div>
                            <div className="weight-600 font-14">Deals</div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="col-xl-3 mb-30">
                <div className="card-box height-100-p widget-style1">
                    <div className="d-flex flex-wrap align-items-center">
                        <div className="progress-data">
                            <div id="chart3"></div>
                        </div>
                        <div className="widget-data">
                            <div className="h4 mb-0">350</div>
                            <div className="weight-600 font-14">Campaign</div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="col-xl-3 mb-30">
                <div className="card-box height-100-p widget-style1">
                    <div className="d-flex flex-wrap align-items-center">
                        <div className="progress-data">
                            <div id="chart4"></div>
                        </div>
                        <div className="widget-data">
                            <div className="h4 mb-0">$6060</div>
                            <div className="weight-600 font-14">Worth</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div className="row">
            <div className="col-xl-8 mb-30">
                <div className="card-box height-100-p pd-20">
                    <h2 className="h4 mb-20">Activity</h2>
                    <div id="chart5"></div>
                </div>
            </div>
            <div className="col-xl-4 mb-30">
                <div className="card-box height-100-p pd-20">
                    <h2 className="h4 mb-20">Lead Target</h2>
                    <div id="chart6"></div>
                </div>
            </div>
        </div>
        <div className="card-box mb-30">
            <h2 className="h4 pd-20">Best Selling Products</h2>
            <table className="data-table table nowrap">
                <thead>
                    <tr>
                        <th className="table-plus datatable-nosort">Product</th>
                        <th>Name</th>
                        <th>Color</th>
                        <th>Size</th>
                        <th>Price</th>
                        <th>Oty</th>
                        <th className="datatable-nosort">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td className="table-plus">
                            <img src="vendors/images/product-1.jpg" width="70" height="70" alt=""/>
                        </td>
                        <td>
                            <h5 className="font-16">Shirt</h5>
                            by John Doe
                        </td>
                        <td>Black</td>
                        <td>M</td>
                        <td>$1000</td>
                        <td>1</td>
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
                    <tr>
                        <td className="table-plus">
                            <img src="vendors/images/product-2.jpg" width="70" height="70" alt=""/>
                        </td>
                        <td>
                            <h5 className="font-16">Boots</h5>
                            by Lea R. Frith
                        </td>
                        <td>brown</td>
                        <td>9UK</td>
                        <td>$900</td>
                        <td>1</td>
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
                    <tr>
                        <td className="table-plus">
                            <img src="vendors/images/product-3.jpg" width="70" height="70" alt=""/>
                        </td>
                        <td>
                            <h5 className="font-16">Hat</h5>
                            by Erik L. Richards
                        </td>
                        <td>Orange</td>
                        <td>M</td>
                        <td>$100</td>
                        <td>4</td>
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
                    <tr>
                        <td className="table-plus">
                            <img src="vendors/images/product-4.jpg" width="70" height="70" alt=""/>
                        </td>
                        <td>
                            <h5 className="font-16">Long Dress</h5>
                            by Renee I. Hansen
                        </td>
                        <td>Gray</td>
                        <td>L</td>
                        <td>$1000</td>
                        <td>1</td>
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
                    <tr>
                        <td className="table-plus">
                            <img src="vendors/images/product-5.jpg" width="70" height="70" alt=""/>
                        </td>
                        <td>
                            <h5 className="font-16">Blazer</h5>
                            by Vicki M. Coleman
                        </td>
                        <td>Blue</td>
                        <td>M</td>
                        <td>$1000</td>
                        <td>1</td>
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
        
    </div>
</div>
        </div>
    );
};

export default Dashboard;