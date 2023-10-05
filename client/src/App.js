// App.js is the entry point for a react app. It serves as the starting point for the component hierarchy. It can be a place to integrate other libraries, set up routing, handle global state management, ect. 
import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom';
// Each component needs to be imported for the BrowserRouter to have access to it.
import EventList from './components/dashboard.jsx';
import Registration from './components/registration.jsx';
import Login from './components/login.jsx';
import './App.css';
import CreateEvent from './components/createEvent.jsx';
import EventDisplay from './components/displayEvent.jsx';
import EditEvent from './components/editEvent';

function App() {

  return (
    <div className="App">
      {/* BrowserRouter enables client-side routing */}
      <BrowserRouter>
        <Routes>
          {/* The route element calls on the component required. The path is the HTTP path that the browswer registers. */}
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