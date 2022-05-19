#
import psycopg2

from psycopg2.extras import RealDictCursor

import os

#
from chalicelib import util_resource

#
RESOURCE_URL = '%(url)s%(resource)s' % {'url': os.environ["API_URL"], 'resource': util_resource.RESOURCE_URL_V1_TSE_PARTIDO}

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
        'id'    , inner_query.partido_id        ,
        'numero', inner_query.partido_tse_numero,
        'sigla' , inner_query.partido_tse_sigla ,
        'nome'  , inner_query.partido_tse_nome  ,
        --
        '_links', json_build_object
        (
            'self', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.partido_id
            ),
            'coligacoesPartidarias', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.partido_id || '/%(_links_coligacao_partidaria_sub_resource)s'
            ),
            'candidaturas', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.partido_id || '/%(_links_candidatura_sub_resource)s'
            ),              
            'fontes', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.partido_id || '/%(_links_fonte_sub_resource)s'
            )
        )
    ) as json_object
--
from 
(
	--
	select distinct
		partido.id         as partido_id        ,
		partido.tse_numero as partido_tse_numero,
		partido.tse_sigla  as partido_tse_sigla ,
		partido.tse_nome   as partido_tse_nome  
    --
	from      tse.partido
	left join tse.coligacao_partidaria_partido on coligacao_partidaria_partido.id_partido = partido.id
	where 1 = 1
    %(sql_template_restriction_by_id)s
    %(sql_template_restriction_by_id_coligacao_partidaria)s
    %(sql_template_order)s
    %(sql_template_restriction_pagination)s    
) as inner_query
""" % {
    '_links_self': RESOURCE_URL, 
    '_links_coligacao_partidaria_sub_resource': util_resource.RESOURCE_V1_TSE_COLIGACAO_PARTIDARIA, 
    '_links_candidatura_sub_resource': util_resource.RESOURCE_V1_TSE_CANDIDATURA,     
    '_links_fonte_sub_resource': util_resource.RESOURCE_V1_TSE_FONTE,
    'sql_template_restriction_by_id': '%(sql_template_restriction_by_id)s',
    'sql_template_restriction_by_id_coligacao_partidaria': '%(sql_template_restriction_by_id_coligacao_partidaria)s',
    'sql_template_order': '%(sql_template_order)s',
    'sql_template_restriction_pagination': '%(sql_template_restriction_pagination)s'}

#
sql_template_postgresql_restriction_by_id = """
--
and partido.id = %(id)s
"""

#
sql_template_postgresql_restriction_by_id_coligacao_partidaria = """
--
and coligacao_partidaria_partido.id_coligacao_partidaria = %(id_coligacao_partidaria)s
"""

#
sql_template_postgresql_order_by_id = """
--
order by partido.id
"""

#
sql_template_postgresql_rescriction_pagination = """
--
limit %(page_size)s
offset (%(page_number)s - 1) * %(page_size)s
"""

#
class TsePartidoResourceService:

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
                'sql_template_restriction_by_id_coligacao_partidaria': '',
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
            id_coligacao_partidaria=None):

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
                'sql_template_restriction_by_id_coligacao_partidaria': sql_template_postgresql_restriction_by_id_coligacao_partidaria if (id_coligacao_partidaria is not None) else '',                
                'sql_template_order': sql_template_postgresql_order_by_id, 
                'sql_template_restriction_pagination': sql_template_postgresql_rescriction_pagination if ((page_number is not None) and (page_size is not None)) else ''}}

            #
            cursor.execute(sql_statement, {
                'id_coligacao_partidaria': id_coligacao_partidaria,
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