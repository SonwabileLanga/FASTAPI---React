from fastapi_users.authentication import JWTAuthentication

SECRET = "your_secret_key"
jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)
