import React from 'react';
import Dashboard from '../../Components/Dashboard/Dashboard';
import Footer from '../../Components/Footer/Footer';
import LeftSideBar from '../../Components/LeftSideBar/LeftSideBar';
import TopBanner from '../../Components/TopBanner/TopBanner';

const Home = () => {
    return (
        <div>
            <TopBanner/>
            <LeftSideBar></LeftSideBar>
            <Dashboard></Dashboard>
            <Footer></Footer>
        </div>
    );
};

export default Home;