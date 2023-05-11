import React, {useState, useNavigate} from 'react'
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import EventList from './components/dashboard.jsx';
import Registration from './components/registration.jsx';
import Login from './components/login.jsx';
import './App.css';
import Cookies from 'js-cookie';

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route element={<Login />} path="/" default />
          <Route element={<Registration />} path="/register" default />
          <Route element={<EventList />} path="/event" />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;