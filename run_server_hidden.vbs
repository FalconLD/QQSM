' run_server_hidden.vbs

' ¡¡IMPORTANTE!! Reemplaza estas dos rutas con las rutas absolutas de tu proyecto.
Dim pythonPath
pythonPath = "C:\Users\LDFALCONI\OneDrive\Desktop\QQSM\.venv\Scripts\python.exe"

Dim scriptPath
scriptPath = "C:\Users\LDFALCONI\OneDrive\Desktop\QQSM\manage.py"

' Comando a ejecutar: "ruta\a\python.exe" "ruta\a\manage.py" runserver
Dim command
command = """" & pythonPath & """ """ & scriptPath & """ runserver"

' Crea un objeto Shell para ejecutar comandos
Dim shell
Set shell = CreateObject("WScript.Shell")

' Ejecuta el comando en una ventana oculta (el '0') y no espera a que termine (el 'false')
shell.Run command, 0, false