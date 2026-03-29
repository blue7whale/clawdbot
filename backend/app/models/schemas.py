from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


class EmpresaBase(BaseModel):
    nombre: str
    nif: str
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None


class EmpresaCreate(EmpresaBase):
    pass


class Empresa(EmpresaBase):
    id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True


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


class FacturaCreate(FacturaBase):
    empresa_id: Optional[int] = None


class Factura(FacturaBase):
    id: int
    iva_importe: float
    empresa_id: Optional[int] = None

    class Config:
        from_attributes = True


class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    tipo: str
    fecha_vencimiento: date
    prioridad: str
    completada: bool = False


class TareaCreate(TareaBase):
    pass


class Tarea(TareaBase):
    id: int
    fecha_completado: Optional[datetime] = None

    class Config:
        from_attributes = True


class ContactoBase(BaseModel):
    tipo: str
    nombre: str
    nif: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None


class ContactoCreate(ContactoBase):
    pass


class Contacto(ContactoBase):
    id: int
    fecha_alta: datetime

    class Config:
        from_attributes = True
