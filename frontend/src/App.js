// App.js
import * as React from 'react';
import SignInSide from './components/SignInSide';
import LoginDetails from './components/LoginDetails'; // Import the LoginDetails component
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<SignInSide />} />
        <Route path="/login/details" element={<LoginDetails />} /> {/* Add this route */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;
