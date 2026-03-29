import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import { useState, useEffect } from 'react'
import Dashboard from './pages/Dashboard'
import Tareas from './pages/Tareas'
import Empresas from './pages/Empresas'
import Contactos from './pages/Contactos'
import { LayoutDashboard, CheckSquare, Building2, Users } from 'lucide-react'
import './App.css'

function App() {
  const [datos, setDatos] = useState(null)

  useEffect(() => {
    fetch('http://localhost:8000/api/dashboard')
      .then(res => res.json())
      .then(data => setDatos(data))
      .catch(err => console.error('Error:', err))
  }, [])

  return (
    <Router>
      <div className="app">
        <header className="header">
          <h1>🤖 Clawdbot</h1>
          <p>Gestión contable para PYME</p>
        </header>
        <nav className="nav">
          <Link to="/"><LayoutDashboard size={20} /> Dashboard</Link>
          <Link to="/tareas"><CheckSquare size={20} /> Tareas</Link>
          <Link to="/empresas"><Building2 size={20} /> Empresas</Link>
          <Link to="/contactos"><Users size={20} /> Contactos</Link>
        </nav>
        <main className="main">
          <Routes>
            <Route path="/" element={<Dashboard datos={datos} />} />
            <Route path="/tareas" element={<Tareas />} />
            <Route path="/empresas" element={<Empresas />} />
            <Route path="/contactos" element={<Contactos />} />
          </Routes>
        </main>
        <footer className="footer">
          <p>Clawdbot v1.0.0 - Gestoría Virtual</p>
        </footer>
      </div>
    </Router>
  )
}

export default App
