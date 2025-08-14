@echo off
ECHO ===============================================
ECHO   Iniciando Servidor de ¿Quien Quiere Ser Millonario?
ECHO ===============================================

:: Cambia al directorio del proyecto.
cd /d "C:\Users\LDFALCONI\OneDrive\Desktop\QQSM"

ECHO Iniciando el servidor en segundo plano...
:: Ejecuta el script VBS para lanzar el servidor en una ventana oculta
cscript //nologo run_server_hidden.vbs

ECHO Servidor iniciado. Esperando 3 segundos para que arranque...
:: Pequeña pausa para asegurar que el servidor esté listo antes de abrir el navegador
timeout /t 3 /nobreak >nul

ECHO Abriendo el juego en pantalla completa...
:: MODIFICADO: Abre Chrome en modo fullscreen. Cambia "chrome" por "msedge" si usas Edge.
start chrome --start-fullscreen http://127.0.0.1:8000/

:: El script termina aquí, y la ventana de CMD se cerrará.
exit
