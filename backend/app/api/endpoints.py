from fastapi import APIRouter, HTTPException, status
from typing import List
from ..services.database import get_db_connection
from ..models.schemas import (
    Empresa,
    EmpresaCreate,
    Factura,
    FacturaCreate,
    Tarea,
    TareaCreate,
    Contacto,
    ContactoCreate,
)

router = APIRouter()


@router.get("/empresas", response_model=List[Empresa])
def obtener_empresas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empresas")
    empresas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return empresas


@router.post("/empresas", response_model=Empresa, status_code=status.HTTP_201_CREATED)
def crear_empresa(empresa: EmpresaCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO empresas (nombre, nif, direccion, telefono, email) VALUES (?, ?, ?, ?, ?)",
        (empresa.nombre, empresa.nif, empresa.direccion, empresa.telefono, empresa.email),
    )
    conn.commit()
    empresa_id = cursor.lastrowid
    cursor.execute("SELECT * FROM empresas WHERE id = ?", (empresa_id,))
    nueva_empresa = dict(cursor.fetchone())
    conn.close()
    return nueva_empresa


@router.get("/facturas", response_model=List[Factura])
def obtener_facturas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM facturas")
    facturas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return facturas


@router.post("/facturas", response_model=Factura, status_code=status.HTTP_201_CREATED)
def crear_factura(factura: FacturaCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    iva_importe = factura.base_imponible * (factura.iva_porcentaje / 100)
    cursor.execute(
        "INSERT INTO facturas (numero, tipo, cliente_proveedor, nif_cliente, fecha_emision, fecha_vencimiento, base_imponible, iva_porcentaje, iva_importe, total, estado, empresa_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            factura.numero,
            factura.tipo,
            factura.cliente_proveedor,
            factura.nif_cliente,
            factura.fecha_emision,
            factura.fecha_vencimiento,
            factura.base_imponible,
            factura.iva_porcentaje,
            iva_importe,
            factura.total,
            factura.estado,
            factura.empresa_id,
        ),
    )
    conn.commit()
    factura_id = cursor.lastrowid
    cursor.execute("SELECT * FROM facturas WHERE id = ?", (factura_id,))
    nueva_factura = dict(cursor.fetchone())
    conn.close()
    return nueva_factura


@router.get("/tareas", response_model=List[Tarea])
def obtener_tareas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tareas")
    tareas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return tareas


@router.post("/tareas", response_model=Tarea, status_code=status.HTTP_201_CREATED)
def crear_tarea(tarea: TareaCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tareas (titulo, descripcion, tipo, fecha_vencimiento, prioridad, completada) VALUES (?, ?, ?, ?, ?, ?)",
        (
            tarea.titulo,
            tarea.descripcion,
            tarea.tipo,
            tarea.fecha_vencimiento,
            tarea.prioridad,
            int(tarea.completada),
        ),
    )
    conn.commit()
    tarea_id = cursor.lastrowid
    cursor.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,))
    nueva_tarea = dict(cursor.fetchone())
    conn.close()
    return nueva_tarea


@router.put("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, tarea: TareaCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tareas SET titulo=?, descripcion=?, tipo=?, fecha_vencimiento=?, prioridad=?, completada=? WHERE id=?",
        (
            tarea.titulo,
            tarea.descripcion,
            tarea.tipo,
            tarea.fecha_vencimiento,
            tarea.prioridad,
            int(tarea.completada),
            tarea_id,
        ),
    )
    conn.commit()
    cursor.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,))
    tarea_actualizada = dict(cursor.fetchone())
    conn.close()
    return tarea_actualizada


@router.delete("/tareas/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(tarea_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
    conn.commit()
    conn.close()
    return None


@router.get("/contactos", response_model=List[Contacto])
def obtener_contactos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos")
    contactos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return contactos


@router.post("/contactos", response_model=Contacto, status_code=status.HTTP_201_CREATED)
def crear_contacto(contacto: ContactoCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contactos (tipo, nombre, nif, direccion, telefono, email) VALUES (?, ?, ?, ?, ?, ?)",
        (contacto.tipo, contacto.nombre, contacto.nif, contacto.direccion, contacto.telefono, contacto.email),
    )
    conn.commit()
    contacto_id = cursor.lastrowid
    cursor.execute("SELECT * FROM contactos WHERE id = ?", (contacto_id,))
    nuevo_contacto = dict(cursor.fetchone())
    conn.close()
    return nuevo_contacto


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
    cursor.execute("SELECT SUM(total) FROM facturas WHERE estado = 'pagada'")
    ingresos = cursor.fetchone()[0] or 0
    conn.close()
    return {
        "total_empresas": total_empresas,
        "total_facturas": total_facturas,
        "tareas_pendientes": tareas_pendientes,
        "total_contactos": total_contactos,
        "ingresos": ingresos,
    }
