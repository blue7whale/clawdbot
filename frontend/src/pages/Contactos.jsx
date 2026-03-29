import { useState, useEffect } from 'react'
import axios from 'axios'

function Contactos() {
  const [contactos, setContactos] = useState([])
  const [cargando, setCargando] = useState(true)

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/contactos')
      .then((res) => {
        setContactos(res.data)
        setCargando(false)
      })
      .catch((err) => {
        console.error(err)
        setCargando(false)
      })
  }, [])

  if (cargando) return <div>Cargando contactos...</div>

  return (
    <div>
      <h2>👥 Contactos</h2>
      <table className="table">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Tipo</th>
            <th>NIF</th>
            <th>Email</th>
            <th>Teléfono</th>
          </tr>
        </thead>
        <tbody>
          {contactos.map((contacto) => (
            <tr key={contacto.id}>
              <td>{contacto.nombre}</td>
              <td>{contacto.tipo}</td>
              <td>{contacto.nif}</td>
              <td>{contacto.email}</td>
              <td>{contacto.telefono}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Contactos
