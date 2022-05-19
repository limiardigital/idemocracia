#
import psycopg2

from psycopg2.extras import RealDictCursor

import os

#
from chalicelib import util_resource

#
from chalicelib.v1.services import tse_candidatura_resource_service

#
RESOURCE_URL = '%(url)s%(resource)s' % {'url': os.environ["API_URL"], 'resource': util_resource.RESOURCE_URL_V1_TSE_CANDIDATURA_BEM}

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
        'id'                       , inner_query.candidatura_bem_id                              ,
        'ordem'                    , inner_query.candidatura_bem_tse_ordem                       ,
        'tipoCodigo'               , inner_query.candidatura_bem_tse_tipo_codigo                 ,
        'tipoDescricao'            , inner_query.candidatura_bem_tse_tipo_descricao              ,
        'descricao'                , inner_query.candidatura_bem_tse_descricao                   ,
        'valor'                    , inner_query.candidatura_bem_tse_valor                       ,
        'dataHoraUltimaAtualizacao', inner_query.candidatura_bem_tse_data_hora_ultima_atualizacao,
        --
        '_embedded', json_build_object
        (
            'candidatura', json_build_object
            (
                --
                '_links', json_build_object
                (
                    'self', json_build_object
                    (
                        'href', '%(_embedded_candidatura_links_self)s/' || inner_query.candidatura_bem_id_candidatura
                    )
                )
            )
        ),        
        --
        '_links', json_build_object
        (
            'self', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.candidatura_bem_id
            ) ,
            'fontes', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.candidatura_bem_id || '/%(_links_fonte_sub_resource)s'
            )
        )
    ) as json_object
--
from 
(
    --
    select distinct
        --
        candidatura_bem.id                               as candidatura_bem_id                              ,
        candidatura_bem.tse_ordem                        as candidatura_bem_tse_ordem                       ,
        candidatura_bem.tse_tipo_codigo                  as candidatura_bem_tse_tipo_codigo                 ,
        candidatura_bem.tse_tipo_descricao               as candidatura_bem_tse_tipo_descricao              ,
        candidatura_bem.tse_descricao                    as candidatura_bem_tse_descricao                   ,
        candidatura_bem.tse_valor                        as candidatura_bem_tse_valor                       ,
        candidatura_bem.tse_data_hora_ultima_atualizacao as candidatura_bem_tse_data_hora_ultima_atualizacao,
        candidatura_bem.id_candidatura                   as candidatura_bem_id_candidatura
    --
    from tse.candidatura_bem
    where 1 = 1
    %(sql_template_restriction_by_id)s
    %(sql_template_restriction_by_id_candidatura)s
    %(sql_template_order)s
    %(sql_template_restriction_pagination)s
) as inner_query
""" % {
    '_embedded_candidatura_links_self': tse_candidatura_resource_service.RESOURCE_URL,
    '_links_self': RESOURCE_URL, 
    '_links_fonte_sub_resource': util_resource.RESOURCE_V1_TSE_FONTE,
    'sql_template_restriction_by_id': '%(sql_template_restriction_by_id)s',
    'sql_template_restriction_by_id_candidatura': '%(sql_template_restriction_by_id_candidatura)s',    
    'sql_template_order': '%(sql_template_order)s',
    'sql_template_restriction_pagination': '%(sql_template_restriction_pagination)s'}

#
sql_template_postgresql_restriction_by_id = """
--
and candidatura_bem.id = %(id)s
"""

#
sql_template_postgresql_restriction_by_id_candidatura = """
--
and candidatura_bem.id_candidatura = %(id_candidatura)s
"""

#
sql_template_postgresql_order_by_id = """
--
order by candidatura_bem.id
"""

#
sql_template_postgresql_rescriction_pagination = """
--
limit %(page_size)s
offset (%(page_number)s - 1) * %(page_size)s
"""

#
class TseCandidaturaBemResourceService:

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
                'sql_template_restriction_by_id_candidatura': '',
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
            page_size=None,
            id_candidatura=None):

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
                '_links_self': (RESOURCE_URL if origin_resource_path is None else '%(url)s%(resource)s' % {'url': os.environ["API_URL"], 'resource': origin_resource_path}),
                '_links_self_page_size': page_size,
                '_links_self_page_number': page_number,
                '_links_self_page_number_previous': (page_number - 1 if (page_number - 1) > 0 else 1),
                '_links_self_page_number_next': page_number + 1,                
                'sql_template_select': sql_template_postgresql_select_json_object % { 
                'sql_template_restriction_by_id': '',
                'sql_template_restriction_by_id_candidatura': sql_template_postgresql_restriction_by_id_candidatura if (id_candidatura is not None) else '',
                'sql_template_order': sql_template_postgresql_order_by_id, 
                'sql_template_restriction_pagination': sql_template_postgresql_rescriction_pagination if ((page_number is not None) and (page_size is not None)) else ''}}

            #
            cursor.execute(sql_statement, {
                'id_candidatura': id_candidatura,                
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