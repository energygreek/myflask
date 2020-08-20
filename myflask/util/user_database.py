from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# concret class
class SysUser(Base):
    __tablename__ = 'sys_user'
    # set id column as primary key
    id = Column(String(32), primary_key=True)
    # specify name to name column
    name = Column(String(32))
    password = Column(String(32))


class SysUserSQL:

    def __init__(self):
        self._engine = create_engine(
            current_app.config['SQLALCHEMY_USER_DATABASE_URI'], echo=True)
        # create table
        Base.metadata.create_all(self._engine)

    def add_user(self, user: SysUser):
        Session = sessionmaker(bind=self._engine)
        session = Session()
        session.add(user)
        session.commit()
        session.close()

    def query_user_by_id(self, user_id):
        Session = sessionmaker(bind=self._engine)
        session = Session()
        # fetch only one record use where
        try:
            u = session.query(SysUser).filter(SysUser.id == user_id).one()
            user = {'id':u.id, 'name':u.name, 'password':u.password}
            # fetch all
            # uall = session.query(SysUser).all()
            # for user_re in uall:
            #    print('name -->', user_re.name)
            session.commit()
            session.close()
        except Exception as e:
            print('Exception:',e)
            return None
        return user

    def query_user_by_name(self, user_name):
        Session = sessionmaker(bind=self._engine)
        session = Session()
        # fetch only one record use where
        try:
            u = session.query(SysUser).filter(SysUser.name == user_name).one()
            user = {'id':u.id, 'name':u.name, 'password':u.password}
        except Exception as e:
            print('execption',e)
            return None

        session.commit()
        session.close()
        return user

    def update_user(self, user: SysUser):
        Session = sessionmaker(bind=self._engine)
        session = Session()
        u = session.query(SysUser).filter(SysUser.id == user.id).one()

        print('old user is ', u.name)
        u.name = user.name
        u.password = user.password
        session.commit()
        print('new user is ', u.name)

    def delete_user(self, user: SysUser):
        Session = sessionmaker(bind=self._engine)
        session = Session()
        u = session.query(SysUser).filter(SysUser.id == user.id).one()

        session.delete(u)
        session.commit()

# su = SysUser(id=2,name='John',password='123')
# add_user(su)
