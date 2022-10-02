import React from 'react';
import Banner from './Banner/Banner';
import Service from './Services/Services';
import Testimonials from './Testimonials/Testomonials';
import ProductBanner from './ProductBanner/ProductBanner';
import Contact from './Contact/Contact';
import Footer from './Footer/Footer';

const Home = () => {
    return (
        <div>
            <Banner> </Banner>
            <Service></Service>
            <ProductBanner></ProductBanner>
            <Testimonials></Testimonials>
            <Contact></Contact>
            <Footer></Footer>
        </div>
    );
};

export default Home;