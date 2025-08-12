from django.http import JsonResponse
from base_jwt.utils.auth_decorators import jwt_required

@jwt_required(get_payload=True)
def example(request, payload):
    return JsonResponse({"ok": True, "payload": payload})