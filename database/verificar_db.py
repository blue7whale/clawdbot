import sqlite3


def verificar():
    print("=" * 50)
    print("📊 VERIFICANDO BASE DE DATOS")
    print("=" * 50)

    conexion = sqlite3.connect("clawdbot.db")
    cursor = conexion.cursor()

    print("\n🏢 EMPRESAS REGISTRADAS:")
    cursor.execute("SELECT * FROM empresas")
    empresas = cursor.fetchall()
    print(f"   Total: {len(empresas)}")
    for emp in empresas:
        print(f"   - {emp[1]} (NIF: {emp[2]})")

    print("\n📋 TAREAS REGISTRADAS:")
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    print(f"   Total: {len(tareas)}")
    for tarea in tareas:
        print(f"   - {tarea[1]} (Prioridad: {tarea[5]})")

    print("\n👥 CONTACTOS REGISTRADOS:")
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    print(f"   Total: {len(contactos)}")
    for contacto in contactos:
        print(f"   - {contacto[2]} ({contacto[1]})")

    conexion.close()
    print("\n" + "=" * 50)
    print("✅ VERIFICACIÓN COMPLETADA")
    print("=" * 50)


if __name__ == "__main__":
    verificar()
