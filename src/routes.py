from src.blueprints.list_users_endpoint import blueprint_list_users as ListUsers
from src.blueprints.login_endpoint import blueprint_login as Login
from src.blueprints.health_chech_endpoint import blueprint_health_check as HealthCheck
from src.blueprints.register_endpoint import blueprint_register as Register

def initalize_routes(api):
    api.register_blueprint(HealthCheck,url_prefix= '/api/v1/health_check')
    api.register_blueprint(Register, url_prefix='/api/v1/register')
    api.register_blueprint(Login,url_prefix= '/api/v1/login')
    api.register_blueprint(ListUsers,url_prefix= '/api/v1/list_users')