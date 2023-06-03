#
import psycopg2

from psycopg2.extras import RealDictCursor

import os

#
from chalicelib import util_resource

#
from chalicelib.v1.services import tse_pleito_geral_resource_service

#
RESOURCE_URL = '%(url)s%(resource)s' % {'url': os.environ["API_URL"], 'resource': util_resource.RESOURCE_URL_V1_TSE_PLEITO_REGIONAL}

#
DATABASE_CONNECTION_URL = 'host=%(host)s port=%(port)s dbname=%(dbname)s user=%(user)s password=%(password)s' % {'host': os.environ["DB_HOST"], 'port': os.environ["DB_PORT"], 'dbname': os.environ["DB_NAME"], 'user': os.environ["DB_USER"], 'password': os.environ["DB_PASSWORD"]}

#
sql_template_postgresql_select_json_object = """
--
select
    --
    json_build_object
    (
        --
        'id'                      , inner_query.pleito_regional_id                           ,
        'codigo'                  , inner_query.pleito_regional_tse_codigo                   ,
        'descricao'               , inner_query.pleito_regional_tse_descricao                ,
		'abrangenciaTipoDescricao', inner_query.pleito_regional_tse_abragencia_tipo_descricao,
		'turno'                   , inner_query.pleito_regional_tse_turno                    ,
		'dataHora'                , inner_query.pleito_regional_tse_data_hora                ,
		'tipoCodigo'              , inner_query.pleito_regional_tse_tipo_codigo              ,
		'tipoDescricao'           , inner_query.pleito_regional_tse_tipo_descricao           ,
		--
		'_embedded', json_build_object
		(
			'pleitoGeral', json_build_object
			(
				--
				'_links', json_build_object
                (
					'self', json_build_object
					(
						'href', '%(_embedded_pleito_geral_links_self)s/' || pleito_regional_id_pleito_geral
					)
				)
			)
		),
        --
        '_links', json_build_object
        (
            'self', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.pleito_regional_id
            ),
            'candidaturas', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.pleito_regional_id || '/%(_links_candidatura_sub_resource)s'
            ),            
            'fontes', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.pleito_regional_id || '/%(_links_fonte_sub_resource)s'
            )
        )
    ) as json_object
--
from 
(
    --
    select distinct
        --
        pleito_regional.id                            as pleito_regional_id                           ,
        pleito_regional.tse_codigo                    as pleito_regional_tse_codigo                   ,
        pleito_regional.tse_descricao                 as pleito_regional_tse_descricao                ,
        pleito_regional.tse_abragencia_tipo_descricao as pleito_regional_tse_abragencia_tipo_descricao,
        pleito_regional.tse_turno                     as pleito_regional_tse_turno                    ,
        pleito_regional.tse_data_hora                 as pleito_regional_tse_data_hora                ,
        pleito_regional.tse_tipo_codigo               as pleito_regional_tse_tipo_codigo              ,
        pleito_regional.tse_tipo_descricao            as pleito_regional_tse_tipo_descricao           ,
        pleito_regional.id_pleito_geral               as pleito_regional_id_pleito_geral
    --
    from tse.pleito_regional
    where 1 = 1
    %(sql_template_restriction_by_id)s
    %(sql_template_order)s
    %(sql_template_restriction_pagination)s
) as inner_query
""" % {
    '_embedded_pleito_geral_links_self': tse_pleito_geral_resource_service.RESOURCE_URL,    
    '_links_self': RESOURCE_URL, 
    '_links_candidatura_sub_resource': util_resource.RESOURCE_V1_TSE_CANDIDATURA,     
    '_links_fonte_sub_resource': util_resource.RESOURCE_V1_TSE_FONTE,
    'sql_template_restriction_by_id': '%(sql_template_restriction_by_id)s',
    'sql_template_order': '%(sql_template_order)s',
    'sql_template_restriction_pagination': '%(sql_template_restriction_pagination)s'}

#
sql_template_postgresql_restriction_by_id = """
--
and pleito_regional.id = %(id)s
"""

#
sql_template_postgresql_order_by_id = """
--
order by pleito_regional.id
"""

#
sql_template_postgresql_rescriction_pagination = """
--
limit %(page_size)s
offset (%(page_number)s - 1) * %(page_size)s
"""

#
class TsePleitoRegionalResourceService:

    #
    def find_by_id(self, id):

        #
        connection = None

        #
        try:

            #
            connection = psycopg2.connect(DATABASE_CONNECTION_URL)

            #
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            #
            sql_statement = """
            %(sql_template_select)s
            """  % {
                'sql_template_select': sql_template_postgresql_select_json_object % { 
                'sql_template_restriction_by_id': sql_template_postgresql_restriction_by_id,
                'sql_template_order': sql_template_postgresql_order_by_id,
                'sql_template_restriction_pagination': ''}}

            #
            cursor.execute(sql_statement, {'id': id})

            #
            result = cursor.fetchone()

            #
            if result is not None:

                #
                return result['json_object']

            else:

                #
                return None

        #
        except Exception as e:

            #
            raise e

        #
        finally:
            
            #
            if connection is not None:
                
                #
                connection.close()

    #
    def find_all_by(
            self,
            origin_resource_path=None,            
            page_number=None,
            page_size=None):

        #
        connection = None

        #
        try:

            #
            connection = psycopg2.connect(DATABASE_CONNECTION_URL)

            #
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            #
            sql_statement = """
            --
            select 
            json_build_object
            (
            --
            '_metadata', json_build_object
            (
                'page_number', %(page_number)s,
                'page_size', %(page_size)s,
                '_links', json_build_object
                (
                    'self', json_build_object
                    (
                        'href', '%(_links_self)s?page_size=%(_links_self_page_size)s&page_number=%(_links_self_page_number)s'
                    ),
                    'previous', json_build_object
                    (
                        'href', '%(_links_self)s?page_size=%(_links_self_page_size)s&page_number=%(_links_self_page_number_previous)s'
                    ),
                    'next', json_build_object
                    (
                        'href', '%(_links_self)s?page_size=%(_links_self_page_size)s&page_number=%(_links_self_page_number_next)s'
                    )
                )
            ),
            --
            'data', coalesce(json_agg(main_query.json_object), json_build_array())) as json_object_list
            from 
            (           
                %(sql_template_select)s
            ) as main_query           
            """  % {
                'page_number': page_number,
                'page_size': page_size,
                '_links_self': (RESOURCE_URL if origin_resource_path is None else '%(url)s%(resource)s' % {'url': os.environ["API_URL_ROOT"], 'resource': origin_resource_path}),
                '_links_self_page_size': page_size,
                '_links_self_page_number': page_number,
                '_links_self_page_number_previous': (page_number - 1 if (page_number - 1) > 0 else 1),
                '_links_self_page_number_next': page_number + 1,                
                'sql_template_select': sql_template_postgresql_select_json_object % { 
                'sql_template_restriction_by_id': '',
                'sql_template_order': sql_template_postgresql_order_by_id, 
                'sql_template_restriction_pagination': sql_template_postgresql_rescriction_pagination if ((page_number is not None) and (page_size is not None)) else ''}}

            #
            cursor.execute(sql_statement, {
                'page_number': page_number,
                'page_size': page_size})

            #
            result = cursor.fetchone()

            #
            if result is not None:

                #
                return result['json_object_list']

            else:

                #
                return None

        #
        except Exception as e:

            #
            raise e

        #
        finally:

            #
            if connection is not None:

                #
                connection.close()