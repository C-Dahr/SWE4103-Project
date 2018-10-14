import jwt
from flask_restful import abort
import config


class TokenHandler:
    def __init__(self):
        self.secret = config.jwt_secret

    def create_token(self, payload):
        return jwt.encode(payload=payload, key=self.secret)

    def decode_token(self, token):
        try:
            payload = jwt.decode(jwt=token, key=self.secret)
            user = payload['sub']
            if not user:
                raise RuntimeError('User not found')
            return user
        except jwt.ExpiredSignatureError:
            abort(401, error='Expired token, authentication required.', authentication=False)
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            abort(401, error='Invalid token, registration and/or authentication required.', authentitication=False)
