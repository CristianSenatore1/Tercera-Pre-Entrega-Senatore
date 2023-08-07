# Nombre del Proyecto: Trabajo Practico n°3 !!! Cristian Senatore

Este trabajo consiste en una pagina web, de un concesionario de autos

## Descripción

Esta pagina web se realiza para un consecionario de autos, en la cual, el objetivo es visibilizar los autos en stock, los clientes que ya han adquirido sus autos en el consecionario, la posibilidad de ingresar autos al stock, buscar clientes y tambien buscar autos.

## Requisitos

Para poder ver esta pagina, deberas contar con un navegador de interner (tales como Chrome, Explorer, Opera, etc..)
Tener insatala en tu Pc: Python, Django y podras aceder a la base de datos desde DB Browser for SQLite.

## Instalación y Configuración

Para un correcto funcionamiento, deberas seguir los siguientes pasos:

1. Clona el repositorio desde GitHub: git clone <https://github.com/CristianSenatore1/Tercera-Pre-Entrega-Senatore.git>
2. Crea y activa un entorno virtual (se recomienda usar `venv`).
3. Desde la terminal, deberas ejecutar el servidor: python manage.py runserver, para poder visualizar la pagina desde tu web.
4. Deben tener instalado también lo que está en requirements.txt, En el caso de que estes usando entornos virtuales debes activarlo primero para ejecutar el comando, en caso de que no, no hay problema

## Modo de Uso

Podras optar por 2 modos de usar la pagina, ya sea como cliente o como administrador (2da opcion solo valida para tutor con usuario y contraseña).
desde el modo usuario, tendras a disposicion las siguientes rutas/urls:
a- <http://localhost:8000/admin/> desde aqui, tendras acceso al panel de administrador, y podras hacer las modificaciones que quieras en el sistema, ya sea de clientes, stock, vendedores y de hasta otros usuarios tambien

b- <http://localhost:8000/aplicacion/> desde la cual, accederas a la interfaz de inicio de la pagina.
desde aqui, se desprenden las siguientes urls:
aplicacion/ vendedores/ => acceso directo a la base de datos de vendedores activos actualmente
aplicacion/ autos/ => acceso directo a la base de datos de vendedores activos actualmente
aplicacion/ clientes/ => acceso directo a la base de datos de clientes que compraron su vehiculo en la agencia
aplicacion/ autoForm2/ => acceso directo a la carga de autos al stock
aplicacion/ buscarMarca/ => acceso directo al buscador de autos en stock, filtrados por marca
aplicacion/ buscarClientes/ => acceso directo al buscador de clientes en la base de datos

## Créditos

Esta pagina web, fue creada gracias a la colaboracion de profesor(Norman) y tutor(Emanuel Tevez) de coderhouse

## Contacto

En el caso de tener preguntas, problemas o sugerencias, podras comunicarte conmigo a <crsenatore.cs@gmail.com> o bien al whatsapp +549 3513784849 de lunes a sabados de 09 a 19 hrs .

Este proyecto se encuentra en su fase de desarrollo.

## Proyecto propiedad de

Cristian Senatore
