# 🤖 Clawdbot - Gestoría Virtual para PYME

[![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow)](https://github.com/blue7whale/clawdbot)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19+-blue.svg)](https://react.dev/)

Sistema de gestión contable y fiscal automatizado para pequeñas y medianas empresas. Clawdbot actúa como una gestoría virtual que ayuda con facturas, impuestos, nóminas y tareas administrativas.

## 📸 Capturas

![Dashboard](docs/screenshots/dashboard.png)
![Tareas](docs/screenshots/tareas.png)

> Añade las imágenes en `docs/screenshots/` o actualiza las rutas anteriores.

## ✨ Características

- 📊 **Dashboard** — Vista general de tu empresa con métricas en tiempo real
- 📋 **Gestión de tareas** — Control de vencimientos fiscales y contables
- 🏢 **Empresas** — Administración de datos de tu PYME
- 👥 **Contactos** — Clientes y proveedores organizados
- 📄 **Facturas** — Emisión y recepción de facturas con cálculo automático de IVA (API)
- 🤖 **Asistente IA** — Consultas naturales sobre contabilidad y fiscalidad (próximamente)

## 🛠️ Stack tecnológico

| Capa | Tecnología |
|------|------------|
| **Backend** | Python 3.11+, FastAPI 0.109 |
| **Frontend** | React 19 + Vite |
| **Base de datos** | SQLite |
| **IA** | Qwen 2.5 Coder (OpenRouter) |
| **Documentación API** | Swagger UI en `/docs` |

## 📁 Estructura del proyecto

```
clawdbot/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints.py      # Rutas API
│   │   ├── models/
│   │   │   └── schemas.py        # Modelos Pydantic
│   │   ├── services/
│   │   │   └── database.py       # Conexión SQLite
│   │   └── utils/
│   ├── main.py                   # Punto de entrada
│   ├── requirements.txt
│   └── venv/
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Tareas.jsx
│   │   │   ├── Empresas.jsx
│   │   │   └── Contactos.jsx
│   │   ├── App.jsx
│   │   └── App.css
│   ├── package.json
│   └── vite.config.js
├── database/
│   ├── crear_db.py               # Script creación BD
│   ├── verificar_db.py           # Script verificación
│   └── clawdbot.db               # Base de datos SQLite (generada / local)
├── docs/
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.11 o superior
- Node.js 18+ y npm
- Git

### Backend

```bash
# Clonar repositorio
git clone https://github.com/blue7whale/clawdbot.git
cd clawdbot

# Entorno virtual
cd backend
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
# o: venv\Scripts\activate  # Windows

# Dependencias
pip install -r requirements.txt

# Base de datos
cd ../database
python3 crear_db.py

# Servidor API (http://localhost:8000 — documentación en /docs)
cd ../backend
python3 main.py
```

### Frontend

En otra terminal, con el backend en marcha:

```bash
cd frontend
npm install
npm run dev
```

La aplicación Vite suele quedar en `http://localhost:5173`. El backend debe permitir ese origen en CORS (ya configurado para `localhost:5173` y `localhost:3000`).

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

- **GitHub:** [@blue7whale](https://github.com/blue7whale)
- **Repositorio:** [github.com/blue7whale/clawdbot](https://github.com/blue7whale/clawdbot)

## 🙏 Agradecimientos

- [FastAPI](https://fastapi.tiangolo.com/) — Framework backend
- [React](https://react.dev/) — Framework frontend
- [Vite](https://vite.dev/) — Build tool y dev server
- [Qwen](https://github.com/QwenLM/Qwen) — Modelos para asistente IA
