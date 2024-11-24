// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Notebooks from './components/Notebooks';
import Workflow from './components/Workflow';
import Clusters from './components/Clusters';
import './styles/App.css';

function App() {
    return (
        <Router>
            <div className="App">
                <header>
                    <h1>DataHarbor</h1>
                </header>
                <main>
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/notebooks" element={<Notebooks />} />
                        <Route path="/workflow" element={<Workflow />} />
                        <Route path="/clusters" element={<Clusters />} />
                    </Routes>
                </main>
            </div>
        </Router>
    );
}

export default App;
