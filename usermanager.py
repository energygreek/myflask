from werkzeug.security import generate_password_hash
import uuid
from user_database import SysUser, SysUserSQL
from user import User


# ...
def create_user(user_name, password):
    """创建一个用户"""
    su = SysUser(id=str(uuid.uuid4()), name=user_name,
                 password=generate_password_hash(password))
    SysUserSQL().add_user(su)


def get_user(user_name):
    """根据用户名获得用户记录"""
    sql = SysUserSQL()
    u = sql.query_user_by_name(user_name)
    if u:
        return User(u)
    else:
        print('not found')
        return None
