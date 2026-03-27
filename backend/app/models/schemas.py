from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


# Empresa
class EmpresaBase(BaseModel):
    nombre: str
    nif: str
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None


class Empresa(EmpresaBase):
    id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True


# Factura
class FacturaBase(BaseModel):
    numero: str
    tipo: str
    cliente_proveedor: str
    nif_cliente: str
    fecha_emision: date
    fecha_vencimiento: date
    base_imponible: float
    iva_porcentaje: float
    total: float
    estado: str = "pendiente"


class Factura(FacturaBase):
    id: int
    iva_importe: float

    class Config:
        from_attributes = True


# Tarea
class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    tipo: str
    fecha_vencimiento: date
    prioridad: str
    completada: bool = False


class Tarea(TareaBase):
    id: int
    fecha_completado: Optional[datetime] = None

    class Config:
        from_attributes = True


# Contacto
class ContactoBase(BaseModel):
    tipo: str
    nombre: str
    nif: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None


class Contacto(ContactoBase):
    id: int
    fecha_alta: datetime

    class Config:
        from_attributes = True
