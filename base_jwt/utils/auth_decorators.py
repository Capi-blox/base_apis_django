# yourproject/utils/auth_decorators.py
from functools import wraps
from django.http import JsonResponse
from .jwt_utils import decode_jwt, JWTError

def jwt_required(get_payload=False):
    """
    Uso:
      @jwt_required()
      def my_view(request): ...

    O si quieres el payload:
      @jwt_required(get_payload=True)
      def my_view(request, payload): ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            auth = request.META.get("HTTP_AUTHORIZATION", "")
            if not auth.startswith("Bearer "):
                return JsonResponse({"detail": "Authorization header missing or invalid"}, status=401)
            token = auth.split(" ", 1)[1].strip()
            try:
                payload = decode_jwt(token)
            except JWTError as e:
                return JsonResponse({"detail": str(e)}, status=401)

            # Si quieres pasar payload a la vista:
            if get_payload:
                return view_func(request, payload, *args, **kwargs)
            # Alternativamente lo puedes anexar a request
            setattr(request, "jwt_payload", payload)
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
