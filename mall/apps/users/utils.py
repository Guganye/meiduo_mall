from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mall import settings

def generic_email_verify_token(user_id):
    serializer = Serializer(secret_key=settings.SECRET_KEY, expires_in=1800)
    data = serializer.dumps({'user_id': user_id})
    return data.decode()

if __name__ == '__main__':
    generic_email_verify_token(123)