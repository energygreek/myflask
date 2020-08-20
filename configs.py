import os


# 基础配置，其它配置类都继承它
class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    TEMPLATES_AUTO_RELOAD = True


# 开发环境配置
class DevelopmentConfig(BaseConfig):
    PROJECT_ROOT = os.getcwd()
    DEBUG = True
    # Set the secret key to some random bytes. Keep this really secret!
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    BOOTSTRAP_SERVE_LOCAL = True

    SQLALCHEMY_USER_DATABASE_URI = 'sqlite:////%s'%(
        os.path.join(PROJECT_ROOT,'userdb.db'))
    SQLALCHEMY_BLOG_DATABASE_URI = 'sqlite:////%s'%(
        os.path.join(PROJECT_ROOT,'blog.db'))

# 生产环境配置
class ProductionConfig(BaseConfig):
    ...


# configs 这个字典通过键值对的形式分别对应不同环境下的配置
# 修改配置只需要修改键即可
configs = {
    'dev': DevelopmentConfig,
    'production': ProductionConfig
}