import { LayoutDashboard, CheckSquare, Building2, Users } from 'lucide-react'

function Dashboard({ datos }) {
  if (!datos) return <div>Cargando...</div>

  const cards = [
    { icon: Building2, value: datos.total_empresas, label: 'Empresas' },
    { icon: CheckSquare, value: datos.tareas_pendientes, label: 'Tareas Pendientes' },
    { icon: Users, value: datos.total_contactos, label: 'Contactos' },
    { icon: LayoutDashboard, value: datos.total_facturas, label: 'Facturas' },
  ]

  return (
    <div>
      <h2>📊 Dashboard</h2>
      <div className="cards">
        {cards.map((card, i) => {
          const Icon = card.icon
          return (
            <div key={i} className="card">
              <Icon size={40} color="#667eea" />
              <div className="card-value">{card.value}</div>
              <div className="card-label">{card.label}</div>
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default Dashboard
