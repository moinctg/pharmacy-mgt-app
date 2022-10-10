

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
// import Dashboard from './Pages/Dashboard/Deshboard/Dashboard';
// import Dashboard from './Pages/Dashboard/Deshboard/AdminDashboard';

import AllHospitals from "./Pages/AllHospitals/AllHospitals";
import AllDoctors from "./Pages/AddDoctor/AllDoctors";
import AllPaitents from "./Pages/AddPaitent/AllPaitents";
import AddPaitent from "./Pages/AddPaitent/AddPaitent";
import AddDoctor from "./Pages/AddDoctor/AddDoctor";
import AddHospital from "./Pages/AddHospital/AddHospital";
import AllMedicine from "./Pages/Medicine/AllMedicine";
import AddMedicine from "./Pages/Medicine/AddMedicine";
import AllStock from "./Pages/Stock/AllStock";
import AddStock from "./Pages/Stock/AddStock";
import AllStoreKipper from "./Pages/StoreKipper/AllStoreKipper";
import AddStoreKipper from "./Pages/StoreKipper/AddStoreKipper";
import AllStore from "./Pages/Store/AllStore";
import AddStore from "./Pages/Store/AddStore";
import AdminDashboard from "./Pages/Dashboard/Deshboard/AdminDashboard";
function App() {
  return (
    
      <AuthProvider>
     <Router>
       <Navber></Navber>

      <Routes>
        <Route path="/" element={<Home></Home>} />
        <Route path="/home" element={<Home></Home>} />
        <Route path="/contact" element={<Contact></Contact>} />
        {/* <Route path="/register" element={<Register></Register>} />
        <Route path="/login" element={<Login></Login>} /> */}
       
        <Route path="/allhospital" element={<AllHospitals></AllHospitals>} />
        <Route path="/addhospital" element={<AddHospital></AddHospital>} />
        <Route path="/alldoctor" element={<AllDoctors></AllDoctors>} />
        <Route path="/adddoctor" element={<AddDoctor></AddDoctor>} />
        <Route path="/allpaitent" element={<AllPaitents></AllPaitents>} />
        <Route path="/addpaitent" element={<AddPaitent></AddPaitent>} />
        <Route path="/allmedicine" element={<AllMedicine></AllMedicine>} />
        <Route path="/addmedicine" element={<AddMedicine></AddMedicine>} />
        <Route path="/addstock" element={<AddStock></AddStock>} />
        <Route path="/allstock" element={<AllStock></AllStock>} />
        <Route path="/allstorekipper" element={<AllStoreKipper></AllStoreKipper>} />
        <Route path="/addstorekipper" element={<AddStoreKipper></AddStoreKipper>} />
        <Route path="/allstore" element={<AllStore></AllStore>} />
        <Route path="/addstore" element={<AddStore></AddStore>} />
        
        <Route path="/dashboard" element={<AdminDashboard></AdminDashboard>} />
       
       
      </Routes>
      </Router>
    </AuthProvider>
      
    
  );
}

export default App;
