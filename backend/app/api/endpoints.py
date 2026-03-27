from fastapi import APIRouter, HTTPException
from typing import List
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.database import get_db_connection
from models.schemas import Empresa, Factura, Tarea, Contacto

router = APIRouter()


# Endpoint: Obtener todas las empresas
@router.get("/empresas", response_model=List[Empresa])
def obtener_empresas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empresas")
    empresas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return empresas


# Endpoint: Obtener todas las facturas
@router.get("/facturas", response_model=List[Factura])
def obtener_facturas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM facturas")
    facturas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return facturas


# Endpoint: Obtener todas las tareas
@router.get("/tareas", response_model=List[Tarea])
def obtener_tareas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tareas")
    tareas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return tareas


# Endpoint: Obtener todos los contactos
@router.get("/contactos", response_model=List[Contacto])
def obtener_contactos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos")
    contactos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return contactos


# Endpoint: Dashboard resumen
@router.get("/dashboard")
def obtener_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM empresas")
    total_empresas = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM facturas")
    total_facturas = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tareas WHERE completada = 0")
    tareas_pendientes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM contactos")
    total_contactos = cursor.fetchone()[0]

    conn.close()

    return {
        "total_empresas": total_empresas,
        "total_facturas": total_facturas,
        "tareas_pendientes": tareas_pendientes,
        "total_contactos": total_contactos,
    }
