# database/crear_db.py
"""
Script para crear la base de datos de Clawdbot
Sistema de gestión contable para PYME
"""
import sqlite3


def crear_base_de_datos():
    print("=" * 50)
    print("🔧 CREANDO BASE DE DATOS CLAWDBOT")
    print("=" * 50)

    conexion = sqlite3.connect("clawdbot.db")
    cursor = conexion.cursor()

    # Eliminar tablas si existen para evitar duplicados
    cursor.execute("DROP TABLE IF EXISTS contactos")
    cursor.execute("DROP TABLE IF EXISTS tareas")
    cursor.execute("DROP TABLE IF EXISTS facturas")
    cursor.execute("DROP TABLE IF EXISTS empresas")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nif TEXT UNIQUE NOT NULL,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    print("✅ Tabla 'empresas' creada")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS facturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa_id INTEGER,
            numero TEXT NOT NULL,
            tipo TEXT CHECK(tipo IN ('emision', 'recepcion')),
            cliente_proveedor TEXT,
            nif_cliente TEXT,
            fecha_emision DATE,
            fecha_vencimiento DATE,
            base_imponible DECIMAL(10,2),
            iva_porcentaje DECIMAL(5,2),
            iva_importe DECIMAL(10,2),
            total DECIMAL(10,2),
            estado TEXT CHECK(estado IN ('pendiente', 'pagada', 'vencida')),
            FOREIGN KEY (empresa_id) REFERENCES empresas(id)
        )
    """
    )
    print("✅ Tabla 'facturas' creada")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            tipo TEXT CHECK(tipo IN ('fiscal', 'contable', 'nomina', 'general')),
            fecha_vencimiento DATE,
            prioridad TEXT CHECK(prioridad IN ('alta', 'media', 'baja')),
            completada INTEGER DEFAULT 0,
            fecha_completado DATETIME,
            recordatorio INTEGER DEFAULT 1
        )
    """
    )
    print("✅ Tabla 'tareas' creada")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT CHECK(tipo IN ('cliente', 'proveedor')),
            nombre TEXT NOT NULL,
            nif TEXT,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            fecha_alta DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    print("✅ Tabla 'contactos' creada")

    conexion.commit()

    cursor.execute(
        """
        INSERT INTO empresas (nombre, nif, direccion, telefono, email)
        VALUES ('Mi Empresa SL', 'B12345678', 'Calle Ejemplo 123, Madrid', '910000000', 'info@miempresa.com')
    """
    )

    cursor.execute(
        """
        INSERT INTO tareas (titulo, descripcion, tipo, fecha_vencimiento, prioridad)
        VALUES
        ('Presentar IVA trimestral', 'Modelo 303 del Q1', 'fiscal', '2025-04-20', 'alta'),
        ('Revisar facturas pendientes', 'Ver cobros del mes', 'contable', '2025-02-28', 'media'),
        ('Enviar nóminas', 'Nóminas de febrero', 'nomina', '2025-02-28', 'alta')
    """
    )

    cursor.execute(
        """
        INSERT INTO contactos (tipo, nombre, nif, email)
        VALUES
        ('cliente', 'Cliente ABC SL', 'B87654321', 'contacto@clienteabc.com'),
        ('proveedor', 'Proveedor XYZ SA', 'A11223344', 'ventas@proveedorxyz.com')
    """
    )

    conexion.commit()
    conexion.close()

    print("\n" + "=" * 50)
    print("🎉 ¡BASE DE DATOS CREADA EXITOSAMENTE!")
    print("=" * 50)


if __name__ == "__main__":
    crear_base_de_datos()
import sqlite3
from datetime import datetime

def crear_base_de_datos():
    """Crea la base de datos SQLite para Clawdbot"""
    
    print("=" * 50)
    print("🔧 CREANDO BASE DE DATOS CLAWDBOT")
    print("=" * 50)
    
    # Conectar a la base de datos (se crea si no existe)
    conexion = sqlite3.connect('clawdbot.db')
    cursor = conexion.cursor()
    
    # ==========================================
    # TABLA 1: EMPRESAS
    # ==========================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nif TEXT UNIQUE NOT NULL,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("✅ Tabla 'empresas' creada")
    
    # ==========================================
    # TABLA 2: FACTURAS
    # ==========================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS facturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa_id INTEGER,
            numero TEXT NOT NULL,
            tipo TEXT CHECK(tipo IN ('emision', 'recepcion')),
            cliente_proveedor TEXT,
            nif_cliente TEXT,
            fecha_emision DATE,
            fecha_vencimiento DATE,
            base_imponible DECIMAL(10,2),
            iva_porcentaje DECIMAL(5,2),
            iva_importe DECIMAL(10,2),
            total DECIMAL(10,2),
            estado TEXT CHECK(estado IN ('pendiente', 'pagada', 'vencida')),
            FOREIGN KEY (empresa_id) REFERENCES empresas(id)
        )
    ''')
    print("✅ Tabla 'facturas' creada")
    
    # ==========================================
    # TABLA 3: TAREAS
    # ==========================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            tipo TEXT CHECK(tipo IN ('fiscal', 'contable', 'nomina', 'general')),
            fecha_vencimiento DATE,
            prioridad TEXT CHECK(prioridad IN ('alta', 'media', 'baja')),
            completada INTEGER DEFAULT 0,
            fecha_completado DATETIME,
            recordatorio INTEGER DEFAULT 1
        )
    ''')
    print("✅ Tabla 'tareas' creada")
    
    # ==========================================
    # TABLA 4: CONTACTOS (Clientes/Proveedores)
    # ==========================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT CHECK(tipo IN ('cliente', 'proveedor')),
            nombre TEXT NOT NULL,
            nif TEXT,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            fecha_alta DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("✅ Tabla 'contactos' creada")
    
    # ==========================================
    # GUARDAR CAMBIOS
    # ==========================================
    conexion.commit()
    
    # ==========================================
    # INSERTAR DATOS DE EJEMPLO
    # ==========================================
    print("\n📝 Insertando datos de ejemplo...")
    
    # Empresa de ejemplo
    cursor.execute('''
        INSERT OR IGNORE INTO empresas (nombre, nif, direccion, telefono, email)
        VALUES ('Mi Empresa SL', 'B12345678', 'Calle Ejemplo 123, Madrid', '910000000', 'info@miempresa.com')
    ''')
    
    # Tareas de ejemplo
    cursor.execute('''
        INSERT OR IGNORE INTO tareas (titulo, descripcion, tipo, fecha_vencimiento, prioridad)
        VALUES 
        ('Presentar IVA trimestral', 'Modelo 303 del Q1', 'fiscal', '2025-04-20', 'alta'),
        ('Revisar facturas pendientes', 'Ver cobros del mes', 'contable', '2025-02-28', 'media'),
        ('Enviar nóminas', 'Nóminas de febrero', 'nomina', '2025-02-28', 'alta')
    ''')
    
    # Contactos de ejemplo
    cursor.execute('''
        INSERT OR IGNORE INTO contactos (tipo, nombre, nif, email)
        VALUES 
        ('cliente', 'Cliente ABC SL', 'B87654321', 'contacto@clienteabc.com'),
        ('proveedor', 'Proveedor XYZ SA', 'A11223344', 'ventas@proveedorxyz.com')
    ''')
    
    conexion.commit()
    conexion.close()
    
    print("\n" + "=" * 50)
    print("🎉 ¡BASE DE DATOS CREADA EXITOSAMENTE!")
    print("=" * 50)
    print("📁 Archivo: clawdbot.db")
    print("📍 Ubicación: ~/clawdbot/database/")
    print("=" * 50)

if __name__ == "__main__":
    crear_base_de_datos()