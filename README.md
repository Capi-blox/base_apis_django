# base_apis_django
## primeros pasos

 - 1.- cambia el nombre de la carpeta base_jwt por el de tu aplicacion.
 - 2.- las carpetas que no se deberiane eliminar son base_jwt y generate_jwt.
 - 3.- La carpeta de example solo es un ejemplo y esta se pude eliminar ya que se tenga otro funcinalidad.

## Requisitos previos

- Python 3.8+
- pip


## Instalación

1. Clonar el repositorio:
```bash/cmd
git clone https://github.com/Capi-blox/base_apis_django
cd base_apis_django

```
2. Instalar dependencias:

```bash/cmd
pip install -r requirements.txt
```

3. Crea el .env

**Linux**
```bash
cp .env.example .env
```
**En Windows (PowerShell)**
```PowerShell
Copy-Item .env.example .env
```

4.- Genera una llave nueva ejecuta el comando de abajo y copia el resultado y pegalo en el .env en la variable JWT_SECRET
```bash/cmd
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### **Cómo eliminar Git de tu proyecto**

**En Linux/macOS:**
```bash
rm -rf .git
```
**En windows:**
```cmd
rmdir /s /q .git
```

**con esto ya tendras una base donde solo usas JWT sin usar base de datos**
**En windows:**
```cmd
python manage.py runserver
``` 

## CRERA NUEVA ORGANIZACION
POST localhost:8000/api/token/
```body
{
  "admin": "AQUI VA EL USUARIO DE SIMPLE_AUTH_USERNAME",
  "pass": "Aqui va tu contraseña SIMPLE_AUTH_PASSWORD",
  "orgName": "AQUI VA EL NOMBRE DE LA ORGANIZACION"
}
```
RETURN
```
{
   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6Ikp......QYIX5ugo"
}

``` 

## NOTA:
**toda libreria que se agrege pasa el proyecto debera ser agregado a requirements.txt para facilitar el despliegue**


