from datetime import datetime

from jose import jwt

from app.config.cfg import cfg

secretKey = cfg.get('crowdToken.secretKey')
timeout = cfg.getint('crowdToken.timeout')


def encode(sub, role):
    return jwt.encode({'sub': sub, 'role': role, 'exp': int(datetime.now().timestamp())+timeout}, secretKey,
                      algorithm='HS256')


def decode(token):
    return jwt.decode(token, secretKey, algorithms=['HS256'])

