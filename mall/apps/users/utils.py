from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mall import settings

def generic_email_verify_token(user_id):
    serializer = Serializer(secret_key=settings.SECRET_KEY, expires_in=1800)
    data = serializer.dumps({'user_id': user_id})
    print(data.decode())
    return data.decode()

def check_verify_token(token):
    serializer = Serializer(secret_key=settings.SECRET_KEY, expires_in=1800)
    try:
        result=serializer.loads(token)
    except Exception as e:
        return None
    return result.get('user_id')

def address_to_dict(address):
    address_dict = {
        'id': address.id,
        'title': address.title,
        'user': address.user.username,
        'receiver': address.receiver,
        'province': address.province.name,
        'city': address.city.name,
        'district': address.district.name,
        'place': address.place,
        'mobile': address.mobile,
        'tel': address.tel,
        'email': address.email
    }
    return address_dict

if __name__ == '__main__':
    token=generic_email_verify_token(123)
    print(token)
    response=check_verify_token('eyJhbGciOiJIUzUxMiIsImlhdCI6MTc1NTQzNDgyMSwiZXhwIjoxNzU1NDM2NjIxfQ.eyJ1c2VyX2lkIjoxMjN9.KyiV0WCKdC0rLnv-ZgIU7DkV4Jokf78tEKJMGPCQktCpgM4MA6Pnjf0WYGrehonfkTpreOvPLQJpOSeIKSr8dg')
    print(response)