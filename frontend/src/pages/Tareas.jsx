import { useState, useEffect } from 'react'
import axios from 'axios'

function Tareas() {
  const [tareas, setTareas] = useState([])
  const [cargando, setCargando] = useState(true)

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/tareas')
      .then((res) => {
        setTareas(res.data)
        setCargando(false)
      })
      .catch((err) => {
        console.error(err)
        setCargando(false)
      })
  }, [])

  if (cargando) return <div>Cargando tareas...</div>

  return (
    <div>
      <h2>📋 Tareas</h2>
      <table className="table">
        <thead>
          <tr>
            <th>Título</th>
            <th>Tipo</th>
            <th>Vencimiento</th>
            <th>Prioridad</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          {tareas.map((tarea) => (
            <tr key={tarea.id}>
              <td>{tarea.titulo}</td>
              <td>{tarea.tipo}</td>
              <td>{tarea.fecha_vencimiento}</td>
              <td>
                <span className={`priority-${tarea.prioridad}`}>{tarea.prioridad}</span>
              </td>
              <td>{tarea.completada ? '✅' : '⏳'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Tareas
