

import {  BrowserRouter as Router, Route, Routes  } from "react-router-dom";
import * as React from "react";
import AuthProvider from './context/AuthProvider';
import Navber from './Pages/Home/Shared/Navbar/Navbar';
import Home from './Pages/Home/Home/Home';
import Contact from './Pages/Home/Home/Contact/Contact';
import Register from './Pages/Register/Register';
import Login from './Pages/Login/Login';
import Portfolio from './Pages/Portfolio/Portfolio';
import OurTeam from './Pages/OurTeam/OurTeam';
import Dashboard from './Pages/Dashboard/Deshboard/Dashboard';
function App() {
  return (
    
      <AuthProvider>
     <Router>
       <Navber></Navber>

      <Routes>
        <Route path="/" element={<Home></Home>} />
        <Route path="/home" element={<Home></Home>} />
        <Route path="/contact" element={<Contact></Contact>} />
        <Route path="/register" element={<Register></Register>} />
        <Route path="/login" element={<Login></Login>} />
        <Route path="/portfolio" element={<Portfolio></Portfolio>} />
        <Route path="/ourteam" element={<OurTeam></OurTeam>} />
        <Route path="/dashboard" element={<Dashboard></Dashboard>} />
       
       
      </Routes>
      </Router>
    </AuthProvider>
      
    
  );
}

export default App;
