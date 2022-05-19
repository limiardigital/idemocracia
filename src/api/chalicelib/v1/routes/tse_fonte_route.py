#
from chalice import Blueprint, Response

#
import app

#
import sys

#
from chalicelib import util_param
from chalicelib import util_resource

#
from chalicelib.v1.services import tse_fonte_resource_service

#
v1_tse_fonte_routes = Blueprint(__name__)

#
service = tse_fonte_resource_service.TseFonteResourceService()

#
@v1_tse_fonte_routes.route('%(resource)s/{id}' % {'resource': util_resource.RESOURCE_URL_V1_TSE_FONTE}, methods=['GET'], cors=True)
def get_by_id(id):

    #
    try:

        #
        path_param_id = None

        try:

            #
            path_param_id = util_param.process_path_param_uuid(util_param.PATH_PARAM_TSE_ID, id)
   
        except Exception as e:

            #
            return Response(body={'code' : 'bad_request', 'message': str(e)}, status_code=400, headers={'Content-Type': 'application/json'})

        #
        result = service.find_by_id(id = path_param_id)

        #
        if result is not None:

            #
            return Response(body=result, status_code=200, headers={'Content-Type': 'application/json'})

        else:

            #
            return Response(body={'code' : 'not_found', 'message': id}, status_code=404, headers={'Content-Type': 'application/json'})

    #
    except Exception as e:

        #
        return Response(body={'code' : 'internal_server_error', 'message': str(e)}, status_code=500, headers={'Content-Type': 'application/json'})

#
@v1_tse_fonte_routes.route('%(resource)s' % {'resource': util_resource.RESOURCE_URL_V1_TSE_FONTE}, methods=['GET'], cors=True)
def get_all():

    #
    try:

        #
        query_param_page_number = None
        query_param_page_size = None
        
        #
        query_param_id_coligacao_partidaria = None
        query_param_id_coligacao_partidaria_composicao = None
        query_param_id_partido = None
        query_param_id_pleito_geral = None
        query_param_id_pleito_regional = None
        query_param_id_pessoa_fisica = None
        query_param_id_cargo = None
        query_param_id_pais = None
        query_param_id_unidade_federativa = None
        query_param_id_municipio = None
        query_param_id_candidatura = None
        query_param_id_candidatura_bem = None
        query_param_id_candidatura_motivo_cassacao = None
        query_param_id_motivo_cassacao = None
        query_param_id_pleito_geral_cargo = None
        query_param_id_pleito_regional_cargo = None

        #
        try:

            #
            query_param_page_number = util_param.process_query_param_integer(app.app.current_request.query_params, util_param.QUERY_PARAM_PAGE_NUMBER, False, 1, sys.maxsize, util_param.QUERY_PARAM_PAGE_NUMBER_DEFAULT_VALUE)
            query_param_page_size = util_param.process_query_param_integer(app.app.current_request.query_params, util_param.QUERY_PARAM_PAGE_SIZE, False, 1, 100, util_param.QUERY_PARAM_PAGE_SIZE_DEFAULT_VALUE) 

            #
            query_param_id_coligacao_partidaria = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_COLIGACAO_PARTIDARIA, False) 
            query_param_id_coligacao_partidaria_composicao = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_COLIGACAO_PARTIDARIA_COMPOSICAO, False) 
            query_param_id_partido = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_PARTIDO, False) 
            query_param_id_pleito_geral = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_PLEITO_GERAL, False) 
            query_param_id_pleito_regional = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_PLEITO_REGIONAL, False) 
            query_param_id_pessoa_fisica = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_PESSOA_FISICA, False) 
            query_param_id_cargo = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_CARGO, False) 
            query_param_id_pais = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_PAIS, False) 
            query_param_id_unidade_federativa = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_UNIDADE_FEDERATIVA, False) 
            query_param_id_municipio = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_MUNICIPIO, False) 
            query_param_id_candidatura = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_CANDIDATURA, False) 
            query_param_id_candidatura_bem = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_CANDIDATURA_BEM, False) 
            query_param_id_candidatura_motivo_cassacao = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_CANDIDATURA_MOTIVO_CASSACAO, False) 
            query_param_id_motivo_cassacao = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_MOTIVO_CASSACAO, False) 
            query_param_id_pleito_geral_cargo = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_PLEITO_GERAL_CARGO, False) 
            query_param_id_pleito_regional_cargo = util_param.process_query_param_uuid(app.app.current_request.query_params, util_param.QUERY_PARAM_TSE_ID_PLEITO_REGIONAL_CARGO, False) 

        #
        except Exception as e:

            #
            return Response(body={'code' : 'bad_request', 'message': str(e)}, status_code=400, headers={'Content-Type': 'application/json'})

        #
        result = service.find_all_by(
            origin_resource_path=app.app.current_request.context['path'],            
            page_number=query_param_page_number,
            page_size=query_param_page_size,
            id_coligacao_partidaria=query_param_id_coligacao_partidaria,
            id_coligacao_partidaria_composicao=query_param_id_coligacao_partidaria_composicao,
            id_partido=query_param_id_partido,
            id_pleito_geral=query_param_id_pleito_geral,
            id_pleito_regional=query_param_id_pleito_regional,
            id_pessoa_fisica=query_param_id_pessoa_fisica,
            id_cargo=query_param_id_cargo,
            id_pais=query_param_id_pais,
            id_unidade_federativa=query_param_id_unidade_federativa,
            id_municipio=query_param_id_municipio,
            id_candidatura=query_param_id_candidatura,
            id_candidatura_bem=query_param_id_candidatura_bem,
            id_candidatura_motivo_cassacao=query_param_id_candidatura_motivo_cassacao,
            id_motivo_cassacao=query_param_id_motivo_cassacao,
            id_pleito_geral_cargo=query_param_id_pleito_geral_cargo,
            id_pleito_regional_cargo=query_param_id_pleito_regional_cargo)

        #
        if result is not None:

            #
            return Response(body=result, status_code=200, headers={'Content-Type': 'application/json'})

        else:

            #
            return Response(body={'code' : 'not_found', 'message': id}, status_code=404, headers={'Content-Type': 'application/json'})

    #
    except Exception as e:

        #
        return Response(body={'code' : 'internal_server_error', 'message': str(e)}, status_code=500, headers={'Content-Type': 'application/json'})