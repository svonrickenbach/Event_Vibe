import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import EventList from './components/dashboard.jsx';
import './App.css';

function App() {
  
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route element={<EventList/>} path="/event" default/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
