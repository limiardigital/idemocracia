#
import psycopg2

from psycopg2.extras import RealDictCursor

import os

#
from chalicelib import util_resource

#
RESOURCE_URL = '%(url)s%(resource)s' % {'url': os.environ["API_URL"], 'resource': util_resource.RESOURCE_URL_V1_TSE_FONTE}

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
        'id'                , inner_query.fonte_referencia_id       ,
        'sigla'             , inner_query.fonte_sigla               ,
        'descricao'         , inner_query.fonte_descricao           ,
        'url'               , inner_query.fonte_url                 ,
        'urlRepositorio'    , inner_query.fonte_repositorio_url     ,
        'registro'          , inner_query.fonte_referencia_registro ,
        'dataHoraObtencao'  , inner_query.fonte_obtencao_data_hora  ,
        'dataHoraImportacao', inner_query.fonte_importacao_data_hora,
        --
        '_links', json_build_object
        (
            'self', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.fonte_referencia_id
            ) 
        )
    ) as json_object
--
from 
(
    --
    select distinct
        --
        fonte_referencia.id        as fonte_referencia_id       ,
        fonte.sigla                as fonte_sigla               ,
        fonte.descricao            as fonte_descricao           ,
        fonte.url                  as fonte_url                 ,
        fonte.repositorio_url      as fonte_repositorio_url     ,
        fonte_referencia.registro  as fonte_referencia_registro , 
        fonte.obtencao_data_hora   as fonte_obtencao_data_hora  ,
        fonte.importacao_data_hora as fonte_importacao_data_hora
    --
    from      tse.fonte_referencia
    left join tse.fonte            on fonte.id = fonte_referencia.id_fonte
    where 1 = 1
    %(sql_template_restriction_by_id)s
    %(sql_template_restriction_by_id_coligacao_partidaria)s
    %(sql_template_restriction_by_id_coligacao_partidaria_composicao)s
    %(sql_template_restriction_by_id_partido)s
    %(sql_template_restriction_by_id_pleito_geral)s
    %(sql_template_restriction_by_id_pleito_regional)s
    %(sql_template_restriction_by_id_pessoa_fisica)s
    %(sql_template_restriction_by_id_cargo)s
    %(sql_template_restriction_by_id_pais)s
    %(sql_template_restriction_by_id_unidade_federativa)s
    %(sql_template_restriction_by_id_municipio)s
    %(sql_template_restriction_by_id_candidatura)s
    %(sql_template_restriction_by_id_candidatura_bem)s
    %(sql_template_restriction_by_id_candidatura_motivo_cassacao)s
    %(sql_template_restriction_by_id_motivo_cassacao)s
    %(sql_template_restriction_by_id_pleito_geral_cargo)s
    %(sql_template_restriction_by_id_pleito_regional_cargo)s    
    %(sql_template_order)s
    %(sql_template_restriction_pagination)s
) as inner_query
""" % {
    '_links_self': RESOURCE_URL, 
    '_links_fonte_sub_resource': util_resource.RESOURCE_V1_TSE_FONTE,
    'sql_template_restriction_by_id': '%(sql_template_restriction_by_id)s',
    'sql_template_restriction_by_id_coligacao_partidaria': '%(sql_template_restriction_by_id_coligacao_partidaria)s',
    'sql_template_restriction_by_id_coligacao_partidaria_composicao': '%(sql_template_restriction_by_id_coligacao_partidaria_composicao)s',
    'sql_template_restriction_by_id_partido': '%(sql_template_restriction_by_id_partido)s',
    'sql_template_restriction_by_id_pleito_geral': '%(sql_template_restriction_by_id_pleito_geral)s',
    'sql_template_restriction_by_id_pleito_regional': '%(sql_template_restriction_by_id_pleito_regional)s',
    'sql_template_restriction_by_id_pessoa_fisica': '%(sql_template_restriction_by_id_pessoa_fisica)s',
    'sql_template_restriction_by_id_cargo': '%(sql_template_restriction_by_id_cargo)s',
    'sql_template_restriction_by_id_pais': '%(sql_template_restriction_by_id_pais)s',
    'sql_template_restriction_by_id_unidade_federativa': '%(sql_template_restriction_by_id_unidade_federativa)s',
    'sql_template_restriction_by_id_municipio': '%(sql_template_restriction_by_id_municipio)s',
    'sql_template_restriction_by_id_candidatura': '%(sql_template_restriction_by_id_candidatura)s',
    'sql_template_restriction_by_id_candidatura_bem': '%(sql_template_restriction_by_id_candidatura_bem)s',
    'sql_template_restriction_by_id_candidatura_motivo_cassacao': '%(sql_template_restriction_by_id_candidatura_motivo_cassacao)s',
    'sql_template_restriction_by_id_motivo_cassacao': '%(sql_template_restriction_by_id_motivo_cassacao)s',
    'sql_template_restriction_by_id_pleito_geral_cargo': '%(sql_template_restriction_by_id_pleito_geral_cargo)s',
    'sql_template_restriction_by_id_pleito_regional_cargo': '%(sql_template_restriction_by_id_pleito_regional_cargo)s',
    'sql_template_order': '%(sql_template_order)s',
    'sql_template_restriction_pagination': '%(sql_template_restriction_pagination)s'}

#
sql_template_postgresql_restriction_by_id = """
--
and fonte_referencia.id = %(id)s
"""

#
sql_template_postgresql_restriction_by_id_coligacao_partidaria = """
--
and fonte_referencia.id_coligacao_partidaria = %(id_coligacao_partidaria)s
"""

#
sql_template_postgresql_restriction_by_id_coligacao_partidaria_composicao = """
--
and fonte_referencia.id_coligacao_partidaria_composicao = %(id_coligacao_partidaria_composicao)s
"""

#
sql_template_postgresql_restriction_by_id_partido = """
--
and fonte_referencia.id_partido = %(id_partido)s
"""

#
sql_template_postgresql_restriction_by_id_pleito_geral = """
--
and fonte_referencia.id_pleito_geral = %(id_pleito_geral)s
"""

#
sql_template_postgresql_restriction_by_id_pleito_regional = """
--
and fonte_referencia.id_pleito_regional = %(id_pleito_regional)s
"""

#
sql_template_postgresql_restriction_by_id_pessoa_fisica = """
--
and fonte_referencia.id_pessoa_fisica = %(id_pessoa_fisica)s
"""

#
sql_template_postgresql_restriction_by_id_cargo = """
--
and fonte_referencia.id_cargo = %(id_cargo)s
"""

#
sql_template_postgresql_restriction_by_id_pais = """
--
and fonte_referencia.id_pais = %(id_pais)s
"""

#
sql_template_postgresql_restriction_by_id_unidade_federativa = """
--
and fonte_referencia.id_unidade_federativa = %(id_unidade_federativa)s
"""

#
sql_template_postgresql_restriction_by_id_municipio = """
--
and fonte_referencia.id_municipio = %(id_municipio)s
"""

#
sql_template_postgresql_restriction_by_id_candidatura = """
--
and fonte_referencia.id_candidatura = %(id_candidatura)s
"""

#
sql_template_postgresql_restriction_by_id_candidatura_bem = """
--
and fonte_referencia.id_candidatura_bem = %(id_candidatura_bem)s
"""

#
sql_template_postgresql_restriction_by_id_candidatura_motivo_cassacao = """
--
and fonte_referencia.id_candidatura_motivo_cassacao = %(id_candidatura_motivo_cassacao)s
"""

#
sql_template_postgresql_restriction_by_id_motivo_cassacao = """
--
and fonte_referencia.id_motivo_cassacao = %(id_motivo_cassacao)s
"""

#
sql_template_postgresql_restriction_by_id_pleito_geral_cargo = """
--
and fonte_referencia.id_pleito_geral_cargo = %(id_pleito_geral_cargo)s
"""

#
sql_template_postgresql_restriction_by_id_pleito_regional_cargo = """
--
and fonte_referencia.id_pleito_regional_cargo = %(id_pleito_regional_cargo)s
"""

#
sql_template_postgresql_order_by_id = """
--
order by fonte_referencia.id
"""

#
sql_template_postgresql_rescriction_pagination = """
--
limit %(page_size)s
offset (%(page_number)s - 1) * %(page_size)s
"""

#
class TseFonteResourceService:

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
                'sql_template_restriction_by_id_coligacao_partidaria_composicao': '',
                'sql_template_restriction_by_id_partido': '',
                'sql_template_restriction_by_id_pleito_geral': '',
                'sql_template_restriction_by_id_pleito_regional': '',
                'sql_template_restriction_by_id_pessoa_fisica': '',
                'sql_template_restriction_by_id_cargo': '',
                'sql_template_restriction_by_id_pais': '',
                'sql_template_restriction_by_id_unidade_federativa': '',
                'sql_template_restriction_by_id_municipio': '',
                'sql_template_restriction_by_id_candidatura': '',
                'sql_template_restriction_by_id_candidatura_bem': '',
                'sql_template_restriction_by_id_candidatura_motivo_cassacao': '',
                'sql_template_restriction_by_id_motivo_cassacao': '',
                'sql_template_restriction_by_id_pleito_geral_cargo': '',
                'sql_template_restriction_by_id_pleito_regional_cargo': '',
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
            id_coligacao_partidaria=None,
            id_coligacao_partidaria_composicao=None,
            id_partido=None, 
            id_pleito_geral=None,
            id_pleito_regional=None,
            id_pessoa_fisica=None,
            id_cargo=None, 
            id_pais=None,
            id_unidade_federativa=None,
            id_municipio=None,
            id_candidatura=None,
            id_candidatura_bem=None,
            id_candidatura_motivo_cassacao=None,
            id_motivo_cassacao=None,
            id_pleito_geral_cargo=None,
            id_pleito_regional_cargo=None):

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
                'sql_template_restriction_by_id_coligacao_partidaria': sql_template_postgresql_restriction_by_id_coligacao_partidaria if (id_coligacao_partidaria is not None) else '',
                'sql_template_restriction_by_id_coligacao_partidaria_composicao': sql_template_postgresql_restriction_by_id_coligacao_partidaria_composicao if (id_coligacao_partidaria_composicao is not None) else '',
                'sql_template_restriction_by_id_partido': sql_template_postgresql_restriction_by_id_partido if (id_partido is not None) else '',
                'sql_template_restriction_by_id_pleito_geral': sql_template_postgresql_restriction_by_id_pleito_geral if (id_pleito_geral is not None) else '',
                'sql_template_restriction_by_id_pleito_regional': sql_template_postgresql_restriction_by_id_pleito_regional if (id_pleito_regional is not None) else '',
                'sql_template_restriction_by_id_pessoa_fisica': sql_template_postgresql_restriction_by_id_pessoa_fisica if (id_pessoa_fisica is not None) else '',
                'sql_template_restriction_by_id_cargo': sql_template_postgresql_restriction_by_id_cargo if (id_cargo is not None) else '',
                'sql_template_restriction_by_id_pais': sql_template_postgresql_restriction_by_id_pais if (id_pais is not None) else '',
                'sql_template_restriction_by_id_unidade_federativa': sql_template_postgresql_restriction_by_id_unidade_federativa if (id_unidade_federativa is not None) else '',
                'sql_template_restriction_by_id_municipio': sql_template_postgresql_restriction_by_id_municipio if (id_municipio is not None) else '',
                'sql_template_restriction_by_id_candidatura': sql_template_postgresql_restriction_by_id_candidatura if (id_candidatura is not None) else '',
                'sql_template_restriction_by_id_candidatura_bem': sql_template_postgresql_restriction_by_id_candidatura_bem if (id_candidatura_bem is not None) else '',
                'sql_template_restriction_by_id_candidatura_motivo_cassacao': sql_template_postgresql_restriction_by_id_candidatura_motivo_cassacao if (id_candidatura_motivo_cassacao is not None) else '',
                'sql_template_restriction_by_id_motivo_cassacao': sql_template_postgresql_restriction_by_id_motivo_cassacao if (id_motivo_cassacao is not None) else '',
                'sql_template_restriction_by_id_pleito_geral_cargo': sql_template_postgresql_restriction_by_id_pleito_geral_cargo if (id_pleito_geral_cargo is not None) else '',
                'sql_template_restriction_by_id_pleito_regional_cargo': sql_template_postgresql_restriction_by_id_pleito_regional_cargo if (id_pleito_regional_cargo is not None) else '',                 
                'sql_template_order': sql_template_postgresql_order_by_id, 
                'sql_template_restriction_pagination': sql_template_postgresql_rescriction_pagination if ((page_number is not None) and (page_size is not None)) else ''}}


            #
            cursor.execute(sql_statement, {
                'id_coligacao_partidaria': id_coligacao_partidaria,
                'id_coligacao_partidaria_composicao': id_coligacao_partidaria_composicao,
                'id_partido': id_partido,
                'id_pleito_geral': id_pleito_geral,
                'id_pleito_regional': id_pleito_regional,
                'id_pessoa_fisica': id_pessoa_fisica,
                'id_cargo': id_cargo,
                'id_pais': id_pais,
                'id_unidade_federativa': id_unidade_federativa,
                'id_municipio': id_municipio,
                'id_candidatura': id_candidatura,
                'id_candidatura_bem': id_candidatura_bem,
                'id_candidatura_motivo_cassacao': id_candidatura_motivo_cassacao,
                'id_motivo_cassacao': id_motivo_cassacao,
                'id_pleito_geral_cargo': id_pleito_geral_cargo,
                'id_pleito_regional_cargo': id_pleito_regional_cargo,
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