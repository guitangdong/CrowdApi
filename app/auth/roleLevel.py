from enum import Enum


class RoleLevel(Enum):
    guest = 'guest'
    user = 'user'
    admin = 'admin'
    
    @staticmethod
    def check(source, target):
        if target == RoleLevel.guest:
            return True
        elif source == RoleLevel.admin:
            return True
        elif source == target:
            return True
        else:
            return False
