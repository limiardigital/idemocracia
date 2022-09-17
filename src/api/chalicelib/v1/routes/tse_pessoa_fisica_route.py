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
from chalicelib.v1.services import tse_pessoa_fisica_resource_service
from chalicelib.v1.services import tse_candidatura_resource_service
from chalicelib.v1.services import tse_fonte_resource_service

#
v1_tse_pessoa_fisica_routes = Blueprint(__name__)

#
service = tse_pessoa_fisica_resource_service.TsePessoaFisicaResourceService()
candidatura_service = tse_candidatura_resource_service.TseCandidaturaResourceService()
fonte_service = tse_fonte_resource_service.TseFonteResourceService()

#
@v1_tse_pessoa_fisica_routes.route('%(resource)s/{id}' % {'resource': util_resource.RESOURCE_URL_V1_TSE_PESSOA_FISICA}, methods=['GET'], cors=True)
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
@v1_tse_pessoa_fisica_routes.route('%(resource)s' % {'resource': util_resource.RESOURCE_URL_V1_TSE_PESSOA_FISICA}, methods=['GET'], cors=True)
def get_all():

    #
    try:

        #
        query_param_page_number = None
        query_param_page_size = None
        query_param_pessoa_fisica_nome = None
        query_param_pessoa_fisica_nome_social = None

        #
        try:

            #
            query_param_page_number = util_param.process_query_param_integer(app.app.current_request.query_params, util_param.QUERY_PARAM_PAGE_NUMBER, False, 1, sys.maxsize, util_param.QUERY_PARAM_PAGE_NUMBER_DEFAULT_VALUE)
            query_param_page_size = util_param.process_query_param_integer(app.app.current_request.query_params, util_param.QUERY_PARAM_PAGE_SIZE, False, 1, util_param.QUERY_PARAM_PAGE_SIZE_DEFAULT_VALUE, util_param.QUERY_PARAM_PAGE_SIZE_DEFAULT_VALUE) 
            query_param_pessoa_fisica_nome = util_param.process_query_param_string(app.app.current_request.query_params, util_param.QUERY_PARAM_PESSOA_FISICA_NOME, False) 
            query_param_pessoa_fisica_nome_social = util_param.process_query_param_string(app.app.current_request.query_params, util_param.QUERY_PARAM_PESSOA_FISICA_NOME_SOCIAL, False) 
            
        #
        except Exception as e:

            #
            return Response(body={'code' : 'bad_request', 'message': str(e)}, status_code=400, headers={'Content-Type': 'application/json'})

        #
        result = service.find_all_by(
            origin_resource_path=app.app.current_request.context['path'],            
            page_number=query_param_page_number,
            page_size=query_param_page_size,
            pessoa_fisica_nome=query_param_pessoa_fisica_nome,
            pessoa_fisica_nome_social=query_param_pessoa_fisica_nome_social)

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
@v1_tse_pessoa_fisica_routes.route('%(resource)s/{id}/%(sub_resource_fonte)s' % {'resource': util_resource.RESOURCE_URL_V1_TSE_PESSOA_FISICA, 'sub_resource_fonte': util_resource.RESOURCE_V1_TSE_CANDIDATURA}, methods=['GET'], cors=True)
def get_all_candidatura(id):

    #
    try:

        #
        path_param_id = None

        #
        query_param_page_number = None
        query_param_page_size = None

        #
        try:

            #
            path_param_id = util_param.process_path_param_uuid(util_param.PATH_PARAM_TSE_ID, id)

            #
            query_param_page_number = util_param.process_query_param_integer(app.app.current_request.query_params, util_param.QUERY_PARAM_PAGE_NUMBER, False, 1, sys.maxsize, util_param.QUERY_PARAM_PAGE_NUMBER_DEFAULT_VALUE)
            query_param_page_size = util_param.process_query_param_integer(app.app.current_request.query_params, util_param.QUERY_PARAM_PAGE_SIZE, False, 1, util_param.QUERY_PARAM_PAGE_SIZE_DEFAULT_VALUE, util_param.QUERY_PARAM_PAGE_SIZE_DEFAULT_VALUE) 

        #
        except Exception as e:

            #
            return Response(body={'code' : 'bad_request', 'message': str(e)}, status_code=400, headers={'Content-Type': 'application/json'})

        #
        result = candidatura_service.find_all_by(
            origin_resource_path=app.app.current_request.context['path'],            
            page_number=query_param_page_number,
            page_size=query_param_page_size,
            id_pessoa_fisica=path_param_id)

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
@v1_tse_pessoa_fisica_routes.route('%(resource)s/{id}/%(sub_resource_fonte)s' % {'resource': util_resource.RESOURCE_URL_V1_TSE_PESSOA_FISICA, 'sub_resource_fonte': util_resource.RESOURCE_V1_TSE_FONTE}, methods=['GET'], cors=True)
def get_all_fonte(id):

    #
    try:

        #
        path_param_id = None

        #
        query_param_page_number = None
        query_param_page_size = None

        #
        try:

            #
            path_param_id = util_param.process_path_param_uuid(util_param.PATH_PARAM_TSE_ID, id)

            #
            query_param_page_number = util_param.process_query_param_integer(app.app.current_request.query_params, util_param.QUERY_PARAM_PAGE_NUMBER, False, 1, sys.maxsize, util_param.QUERY_PARAM_PAGE_NUMBER_DEFAULT_VALUE)
            query_param_page_size = util_param.process_query_param_integer(app.app.current_request.query_params, util_param.QUERY_PARAM_PAGE_SIZE, False, 1, util_param.QUERY_PARAM_PAGE_SIZE_DEFAULT_VALUE, util_param.QUERY_PARAM_PAGE_SIZE_DEFAULT_VALUE) 

        #
        except Exception as e:

            #
            return Response(body={'code' : 'bad_request', 'message': str(e)}, status_code=400, headers={'Content-Type': 'application/json'})

        #
        result = fonte_service.find_all_by(
            origin_resource_path=app.app.current_request.context['path'],            
            page_number=query_param_page_number,
            page_size=query_param_page_size,
            id_pessoa_fisica=path_param_id)

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