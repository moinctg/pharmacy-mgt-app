

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import * as React from "react";
import AuthProvider from './context/AuthProvider';


import AllHospitals from "./Pages/Hospital/AllHospitals/AllHospitals";
import AllDoctors from "./Pages/Doctor/All Doctors/AllDoctors";
import AllPaitents from "./Pages/Paitent/All Paitents/AllPaitents";
import AddPaitent from "./Pages/Paitent/Add Paitent/AddPaitent";
import AddDoctor from "./Pages/Doctor/Add Doctor/AddDoctor";
import AddHospital from "./Pages/Hospital/Add Hospital/AddHospital";
// import AllMedicine from "./Pages/Medicine/AllMedicine";
// import AddMedicine from "./Pages/Medicine/AddMedicine";
// import AllStock from "./Pages/Stock/AllStock";
// import AddStock from "./Pages/Stock/AddStock";
// import AllStoreKipper from "./Pages/StoreKipper/AllStoreKipper";
// import AddStoreKipper from "./Pages/StoreKipper/AddStoreKipper";
// import AllStore from "./Pages/Store/AllStore";
// import AddStore from "./Pages/Store/AddStore";
import AdminDashboard from "./Pages/Dashboard/Deshboard/AdminDashboard";
import Login from "./Pages/Login/Login";

import Dashboard from "./Components/Dashboard/Dashboard";
function App() {
  return (

    <AuthProvider>
      <Router>
        {/* <Navber></Navber> */}

        <Routes>

          <Route path="/" element={<AdminDashboard></AdminDashboard>} >
          <Route path="/home" element={<Dashboard></Dashboard>} />
          <Route path="/allhospital" element={<AllHospitals></AllHospitals>} />
          <Route path="/addhospital" element={<AddHospital></AddHospital>} />
          <Route path="/alldoctor" element={<AllDoctors></AllDoctors>} />
          <Route path="/adddoctor" element={<AddDoctor></AddDoctor>} />
          <Route path="/allpaitent" element={<AllPaitents></AllPaitents>} />
          <Route path="/addpaitent" element={<AddPaitent></AddPaitent>} />
          </Route>


          
          {/* <Route path="/allmedicine" element={<AllMedicine></AllMedicine>} />
        <Route path="/addmedicine" element={<AddMedicine></AddMedicine>} />
        <Route path="/addstock" element={<AddStock></AddStock>} />
        <Route path="/allstock" element={<AllStock></AllStock>} />
        <Route path="/allstorekipper" element={<AllStoreKipper></AllStoreKipper>} />
        <Route path="/addstorekipper" element={<AddStoreKipper></AddStoreKipper>} />
        <Route path="/allstore" element={<AllStore></AllStore>} />
        <Route path="/addstore" element={<AddStore></AddStore>} /> */}

         
          <Route path="/login" element={<Login></Login>} />
          {/* <Route path="/register" element={<Register></Register>} /> */}
         


        </Routes>
      </Router>
    </AuthProvider>


  );
}

export default App;
