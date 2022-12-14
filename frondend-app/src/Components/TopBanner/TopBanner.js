import React from 'react';

const TopBanner = () => {
    return (
        <div>
            <div classNameName='conatainer'>
        <div className="pre-loader">
		<div className="pre-loader-box">
			<div className="loader-logo"><img src="vendors/images/Icon.png" alt=""/></div>
			<div className='loader-progress' id="progress_div">
				<div className='bar' id='bar1'></div>
			</div>
			<div className='percent' id='percent1'>0%</div>
			<div className="loading-text">
				Loading...
			</div>
		</div>
	</div>

	<div className="header">
		<div className="header-left">
			<div className="menu-icon dw dw-menu"></div>
			<div className="search-toggle-icon dw dw-search2" data-toggle="header_search"></div>
			<div className="header-search">
				<form>
					<div className="form-group mb-0">
						<i className="dw dw-search2 search-icon"></i>
						<input type="text" className="form-control search-input" placeholder="Search Here"/>
						<div className="dropdown">
							<a className="dropdown-toggle no-arrow" href="#" role="button" data-toggle="dropdown">
								<i className="ion-arrow-down-c"></i>
							</a>
							<div className="dropdown-menu dropdown-menu-right">
								<div className="form-group row">
									<label className="col-sm-12 col-md-2 col-form-label">From</label>
									<div className="col-sm-12 col-md-10">
										<input className="form-control form-control-sm form-control-line" type="text"/>
									</div>
								</div>
								<div className="form-group row">
									<label className="col-sm-12 col-md-2 col-form-label">To</label>
									<div className="col-sm-12 col-md-10">
										<input className="form-control form-control-sm form-control-line" type="text"/>
									</div>
								</div>
								<div className="form-group row">
									<label className="col-sm-12 col-md-2 col-form-label">Subject</label>
									<div className="col-sm-12 col-md-10">
										<input className="form-control form-control-sm form-control-line" type="text"/>
									</div>
								</div>
								<div className="text-right">
									<button className="btn btn-primary">Search</button>
								</div>
							</div>
						</div>
					</div>
				</form>
			</div>
		</div>

		
		<div className="header-right">
			<div className="dashboard-setting user-notification">
				<div className="dropdown">
					<a className="dropdown-toggle no-arrow" href="javascript:;" data-toggle="right-sidebar">
						<i className="dw dw-settings2"></i>
					</a>
				</div>
			</div>
			<div className="user-notification">
				<div className="dropdown">
					<a className="dropdown-toggle no-arrow" href="#" role="button" data-toggle="dropdown">
						<i className="icon-copy dw dw-notification"></i>
						<span className="badge notification-active"></span>
					</a>
					<div className="dropdown-menu dropdown-menu-right">
						<div className="notification-list mx-h-350 customscroll">
							<ul>
								<li>
									<a href="#">
										<img src="vendors/images/img.jpg" alt=""/>
										<h3>John Doe</h3>
										<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed...</p>
									</a>
								</li>
								<li>
									<a href="#">
										<img src="vendors/images/photo1.jpg" alt=""/>
										<h3>Lea R. Frith</h3>
										<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed...</p>
									</a>
								</li>
								<li>
									<a href="#">
										<img src="vendors/images/photo2.jpg" alt=""/>
										<h3>Erik L. Richards</h3>
										<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed...</p>
									</a>
								</li>
								<li>
									<a href="#">
										<img src="vendors/images/photo3.jpg" alt=""/>
										<h3>John Doe</h3>
										<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed...</p>
									</a>
								</li>
								<li>
									<a href="#">
										<img src="vendors/images/photo4.jpg" alt=""/>
										<h3>Renee I. Hansen</h3>
										<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed...</p>
									</a>
								</li>
								<li>
									<a href="#">
										<img src="vendors/images/img.jpg" alt=""/>
										<h3>Vicki M. Coleman</h3>
										<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed...</p>
									</a>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
			<div className="user-info-dropdown">
				<div className="dropdown">
					<a className="dropdown-toggle" href="#" role="button" data-toggle="dropdown">
						<span className="user-icon">
							<img src="vendors/images/photo1.jpg" alt=""/>
						</span>
						<span className="user-name">Ross C. Lopez</span>
					</a>
					<div className="dropdown-menu dropdown-menu-right dropdown-menu-icon-list">
						<a className="dropdown-item" href="profile.html"><i className="dw dw-user1"></i> Profile</a>
						<a className="dropdown-item" href="profile.html"><i className="dw dw-settings2"></i> Setting</a>
						<a className="dropdown-item" href="faq.html"><i className="dw dw-help"></i> Help</a>
						<a className="dropdown-item" href="login.html"><i className="dw dw-logout"></i> Log Out</a>
					</div>
				</div>
			</div>
			{/* <div className="github-link">
				<a href="https://github.com/dropways/deskapp" target="_blank"><img src="vendors/images/github.svg" alt=""/></a>
			</div> */}
		</div>
	</div>

        </div>
        </div>
        
    );
};

export default TopBanner;