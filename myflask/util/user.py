from flask_login import UserMixin # base class of user
from werkzeug.security import check_password_hash
from .user_database import SysUserSQL


class User(UserMixin):
    """User class"""
    def __init__(self, user):
        self.username = user.get('name')
        self.password_hash = user.get('password')
        self.id = user.get('id')

    def verify_password(self, password):
        """verify"""
        if self.password_hash is None:
            return False

        return check_password_hash(self.password_hash, password)

    def whoami(self):
        return self.username

    def get_id(self):
        return self.id

    @staticmethod
    def get(user_id):
        """ id """
        if not user_id:
            return None

        sys_user_sql = SysUserSQL()
        u = sys_user_sql.query_user_by_id(user_id)
        if u: 
            return User(u)
        else:
            return None
