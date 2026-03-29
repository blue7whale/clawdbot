import { useState, useEffect } from 'react'
import axios from 'axios'

function Empresas() {
  const [empresas, setEmpresas] = useState([])
  const [cargando, setCargando] = useState(true)

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/empresas')
      .then((res) => {
        setEmpresas(res.data)
        setCargando(false)
      })
      .catch((err) => {
        console.error(err)
        setCargando(false)
      })
  }, [])

  if (cargando) return <div>Cargando empresas...</div>

  return (
    <div>
      <h2>🏢 Empresas</h2>
      <table className="table">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>NIF</th>
            <th>Email</th>
            <th>Teléfono</th>
          </tr>
        </thead>
        <tbody>
          {empresas.map((empresa) => (
            <tr key={empresa.id}>
              <td>{empresa.nombre}</td>
              <td>{empresa.nif}</td>
              <td>{empresa.email}</td>
              <td>{empresa.telefono}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Empresas
