
#
from chalice import Chalice

#
from chalicelib.v1.routes.tse_fonte_route import v1_tse_fonte_routes

#
from chalicelib.v1.routes.tse_pais_route import v1_tse_pais_routes
from chalicelib.v1.routes.tse_unidade_federativa_route import v1_tse_unidade_federativa_routes
from chalicelib.v1.routes.tse_municipio_route import v1_tse_municipio_routes
from chalicelib.v1.routes.tse_pessoa_fisica_route import v1_tse_pessoa_fisica_routes
from chalicelib.v1.routes.tse_partido_route import v1_tse_partido_routes
from chalicelib.v1.routes.tse_coligacao_partidaria_route import v1_tse_coligacao_partidaria_routes
from chalicelib.v1.routes.tse_cargo_route import v1_tse_cargo_routes
from chalicelib.v1.routes.tse_pleito_geral_route import v1_tse_pleito_geral_routes
from chalicelib.v1.routes.tse_pleito_regional_route import v1_tse_pleito_regional_routes
from chalicelib.v1.routes.tse_candidatura_route import v1_tse_candidatura_routes
from chalicelib.v1.routes.tse_candidatura_bem_route import v1_tse_candidatura_bem_routes

#
import os

#
DATABASE_CONNECTION_URL = 'host=%(host)s port=%(port)s dbname=%(dbname)s user=%(user)s password=%(password)s' % {'host': os.environ["DB_HOST"], 'port': os.environ["DB_PORT"], 'dbname': os.environ["DB_NAME"], 'user': os.environ["DB_USER"], 'password': os.environ["DB_PASSWORD"]}

#
app = Chalice(app_name='api-idemocracia')

# V1

#
app.register_blueprint(v1_tse_fonte_routes)

#
app.register_blueprint(v1_tse_pais_routes)
app.register_blueprint(v1_tse_unidade_federativa_routes)
app.register_blueprint(v1_tse_municipio_routes)
app.register_blueprint(v1_tse_pessoa_fisica_routes)
app.register_blueprint(v1_tse_partido_routes)
app.register_blueprint(v1_tse_coligacao_partidaria_routes)
app.register_blueprint(v1_tse_cargo_routes)
app.register_blueprint(v1_tse_pleito_geral_routes)
app.register_blueprint(v1_tse_pleito_regional_routes)
app.register_blueprint(v1_tse_candidatura_routes)
app.register_blueprint(v1_tse_candidatura_bem_routes)

#
#app.debug = True

#
@app.route('/')
def index():

    #
    return {'version': os.environ["VERSION"]}