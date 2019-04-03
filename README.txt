

Hola ! Al correr el server y hacer un:

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
  http://localhost:8000/api/token/

http://localhost:8000/api/token/ retorna:

* 405 Method Not Allowed
{
    "detail": "Method \"GET\" not allowed."
}

Mientras que http://http://localhost:8000 retorna:

HTTP 401 Unauthorized:
{
    "detail": "Authentication credentials were not provided."
}


¿Puede que el decorator @action, que responde a GET requests, en la clase SnippetViewSet no este funcionando?



Al crear un superuser:

AttributeError: type object 'Token' has no attribute 'objects'



Al des-comentar la linea 'rest_framework.authtoken' en INSTALLED_APPS

devuelve AttributeError: module 'rest_framework' has no attribute 'authtokendjoser'