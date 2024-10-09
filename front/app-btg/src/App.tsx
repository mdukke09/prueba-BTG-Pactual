import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Subscribe from './pages/Subscribe';
import Cancel from './pages/Cancel';
import History from './pages/History';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/subscribe/:fundId" element={<Subscribe />} />
        <Route path="/cancel/:fundId" element={<Cancel />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </Router>
  );
};

export default App;