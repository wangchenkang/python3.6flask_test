from flask import Flask

from app.extensions.babel import babel
from app.extensions.database import db
from app.extensions.login import login_manager
from app.modules.user.views import admin_user_blueprint
from config.config import config_settings

ADMIN_BLUEPRINTS = (
    (admin_user_blueprint, "/admin"),
)


def configure_admin_blueprints(app):
    for blueprint, url_prefix in ADMIN_BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
        

def _set_allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


def create_app(config_name):
    app = Flask(__name__, template_folder='templates',
                static_folder='static')
    # 从配置文件中加载配置
    app.config.from_object(config_settings[config_name])
    # 初始化配置
    config_settings[config_name].init_app(app)
    # 初始化扩展
    configure_extensions(app)
    # 初始化蓝图
    configure_admin_blueprints(app)
        
    if app.config.get("DEBUG"):
        # 允许跨域ajax请求
        app.after_request(_set_allow_origin)
    return app


def configure_extensions(app):
    # 初始化数据库
    db.init_app(app)
    # 初始化用户登录
    login_manager.init_app(app)
    # 国际化
    config_babel(app)
    

def config_babel(app):
    """
    配置babel
    :param app:
    :return:
    """
    babel.init_app(app)
    
    from flask import request, g
    
    @babel.localeselector
    def get_locale():
        # if a user is logged in, use the locale from the user settings
        user = getattr(g, 'user', None)
        if user is not None:
            return user.locale
        # otherwise try to guess the language from the user accept
        # header the browser transmits.  We support de/fr/en in this
        # example.  The best match wins.
        # 根据浏览器头来判断返回
        # return request.accept_languages.best_match(['de', 'fr', 'en'])
        # return request.accept_languages.best_match(['zh_Hans_CN'])
        return 'zh_Hans_CN'
    
    @babel.timezoneselector
    def get_timezone():
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone
