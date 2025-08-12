import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from base_jwt.utils.jwt_utils import create_jwt

@csrf_exempt
def token_obtain(request):

    if request.method != "POST":
        return HttpResponseBadRequest("Only POST")

    try:
        body = json.loads(request.body)
    except Exception:
        return HttpResponseBadRequest("JSON inválido")

    name = body.get("admin")
    password = body.get("pass")
    orgName = body.get("orgName")

    # Autenticación sin DB: compara con valores en settings
    if name == settings.SIMPLE_AUTH_USERNAME and password == settings.SIMPLE_AUTH_PASSWORD:
        payload = {
            "sub": orgName,
        }
        token = create_jwt(payload)
        return JsonResponse({"token": token})
    else:
        return JsonResponse({"detail": "Credenciales inválidas"}, status=401)