# backend
backend

Backend desarrollado en Django y Api rest Full

- Primera version de Tablas a usar
- Se agrego Token Autenticacion


## AUTENTICACION

```html
EJEMPLOS:
https://www.youtube.com/watch?v=ilRSzcJfVVg&t=194s
https://michaelwashburnjr.com/django-user-authentication/
``` 
{"username": "luismi" ,"password1":"luismi123" ,"password2": "luismi123","email":"jai..........@gmail.com"}

6a4e76a7a45d73a3d97ab5a5f1f8a0e066450a4b

{"username": "luismi" ,"password":"luismi123"}

{
    "username": "luismi",
    "email": "",
    "password": "luismi123"
}


   backend
    ├── app
    │   ├── migrations
    │   ├── static
    │   └── templates
    └── mysite
    
    En tu fichero `blog/static/css/blog.css` deberías añadir el siguiente código:

```css
    h1 a {
        color: #FCA205;
    }
```    


Ahora tu fichero debería tener este aspecto:

```html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>

    </html>
```    
