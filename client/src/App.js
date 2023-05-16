import React, {useState, useNavigate} from 'react'
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import EventList from './components/dashboard.jsx';
import Registration from './components/registration.jsx';
import Login from './components/login.jsx';
import './App.css';
import Cookies from 'js-cookie';
import CreateEvent from './components/createEvent.jsx';
import EventDisplay from './components/displayEvent.jsx';
import EditEvent from './components/editEvent';

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route element={<Login />} path="/" default />
          <Route element={<Registration />} path="/register" default />
          <Route element={<EventList />} path="/dashboard" />
          <Route element={<CreateEvent/>} path="/event/create" />
          <Route element={<EventDisplay/>} path="/event/:id" />
          <Route element={<EditEvent/>} path="/event/update/:id" />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;