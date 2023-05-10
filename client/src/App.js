import React, {useState} from 'react'
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import EventList from './components/dashboard.jsx';
import LoginRegistrationPage from './components/loginAndRegistration.jsx';
import './App.css';
import Cookies from 'js-cookie';

function App() {
  const [key, setKey] = useState(0);

  function handleEventRoute() {
    setKey(key + 1);
    window.location.reload();
  }

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route element={<LoginRegistrationPage />} path="/" default />
          {Cookies.get('id') ? (
            <Route element={<EventList key={key} onEnter={handleEventRoute} />} path="/event" />
          ) : (
            <Route element={<Navigate to="/" />} />
          )}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;