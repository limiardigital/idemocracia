#
import psycopg2

from psycopg2.extras import RealDictCursor

import os

#
from chalicelib import util_resource

#
from chalicelib.v1.services import tse_pais_resource_service
from chalicelib.v1.services import tse_unidade_federativa_resource_service
from chalicelib.v1.services import tse_municipio_resource_service

#
RESOURCE_URL = '%(url)s%(resource)s' % {'url': os.environ["API_URL"], 'resource': util_resource.RESOURCE_URL_V1_TSE_PESSOA_FISICA}

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
		'id'                , inner_query.pessoa_fisica_id                         ,
        'nome'              , inner_query.pessoa_fisica_tse_nome                   ,
		'nomeSocial'        , inner_query.pessoa_fisica_tse_nome_social            ,
		'nascimentoDataHora', inner_query.pessoa_fisica_tse_data_hora_nascimento   ,
        'cpf'               , inner_query.pessoa_fisica_tse_cpf                    ,
		'tituloEleitoral'   , inner_query.pessoa_fisica_tse_numero_titulo_eleitoral,
		--
		'_embedded', json_build_object
		(
			'nascimentoPais', json_build_object
			(
				--
				'id'    , inner_query.pais_id       ,
				'sigla' , inner_query.pais_tse_sigla,
				'nome'  , inner_query.pais_tse_nome ,
				--
				'_links', json_build_object
                (
					'self', json_build_object
					(
						'href', '%(_embedded_pais_nascimento_links_self)s/' || inner_query.pessoa_fisica_id_pais_nascimento
					)
				)
			),
			'nascimentoUnidadeFederativa', json_build_object
			(
				--
				'id'    , inner_query.unidade_federativa_id       ,
				'sigla' , inner_query.unidade_federativa_tse_sigla,
				'nome'  , inner_query.unidade_federativa_tse_nome ,
				--
				'_links', json_build_object
                (
					'self', json_build_object
					(
						'href', '%(_embedded_unidade_federativa_nascimento_links_self)s/' || inner_query.pessoa_fisica_id_unidade_federativa_nascimento
					)
				)
			),
			'nascimentoMunicipio', json_build_object
			(
				--
				'id'    , inner_query.municipio_id       ,
				'sigla' , inner_query.municipio_tse_sigla,
				'nome'  , inner_query.municipio_tse_nome ,
				--
				'_links', json_build_object
                (
					'self', json_build_object
					(
						'href', '%(_embedded_municipio_nascimento_links_self)s/' || inner_query.pessoa_fisica_id_municipio_nascimento
					)
				)
			)
		),
		--
        '_links', json_build_object
        (
            'self', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.pessoa_fisica_id
            ),
            'candidaturas', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.pessoa_fisica_id || '/%(_links_candidatura_sub_resource)s'
            ),            
            'fontes', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.pessoa_fisica_id || '/%(_links_fonte_sub_resource)s'
            )
        )
    ) as json_object
--
from 
(
    --
    select
        --
        pessoa_fisica.id                               as pessoa_fisica_id                              ,
        pessoa_fisica.tse_nome                         as pessoa_fisica_tse_nome                        ,
        pessoa_fisica.tse_nome_social                  as pessoa_fisica_tse_nome_social                 ,
        pessoa_fisica.tse_data_hora_nascimento         as pessoa_fisica_tse_data_hora_nascimento        ,
        pessoa_fisica.tse_cpf                          as pessoa_fisica_tse_cpf                         ,
        pessoa_fisica.tse_numero_titulo_eleitoral      as pessoa_fisica_tse_numero_titulo_eleitoral     ,
        pessoa_fisica.id_pais_nascimento               as pessoa_fisica_id_pais_nascimento              ,
        pais.id                                        as pais_id                                       ,
        pais.tse_sigla                                 as pais_tse_sigla                                ,
        pais.tse_nome                                  as pais_tse_nome                                 ,
        pessoa_fisica.id_unidade_federativa_nascimento as pessoa_fisica_id_unidade_federativa_nascimento,
        unidade_federativa.id                          as unidade_federativa_id                         ,
        unidade_federativa.tse_sigla                   as unidade_federativa_tse_sigla                  ,
        unidade_federativa.tse_nome                    as unidade_federativa_tse_nome                   ,
        pessoa_fisica.id_municipio_nascimento          as pessoa_fisica_id_municipio_nascimento         ,
        municipio.id                                   as municipio_id                                  ,
        municipio.tse_sigla                            as municipio_tse_sigla                           ,
        municipio.tse_nome                             as municipio_tse_nome                            
    --
    from      tse.pessoa_fisica
    left join tse.pais               on pais.id               = pessoa_fisica.id_pais_nascimento
    left join tse.unidade_federativa on unidade_federativa.id = pessoa_fisica.id_unidade_federativa_nascimento
    left join tse.municipio          on municipio.id          = pessoa_fisica.id_municipio_nascimento
    where 1 = 1
    %(sql_template_restriction_by_id)s
    %(sql_template_order)s
    %(sql_template_restriction_pagination)s
) as inner_query
""" % {
    '_embedded_pais_nascimento_links_self': tse_pais_resource_service.RESOURCE_URL,
    '_embedded_unidade_federativa_nascimento_links_self': tse_unidade_federativa_resource_service.RESOURCE_URL,
    '_embedded_municipio_nascimento_links_self': tse_municipio_resource_service.RESOURCE_URL,    
    '_links_self': RESOURCE_URL, 
    '_links_candidatura_sub_resource': util_resource.RESOURCE_V1_TSE_CANDIDATURA,    
    '_links_fonte_sub_resource': util_resource.RESOURCE_V1_TSE_FONTE,
    'sql_template_restriction_by_id': '%(sql_template_restriction_by_id)s',
    'sql_template_order': '%(sql_template_order)s',
    'sql_template_restriction_pagination': '%(sql_template_restriction_pagination)s'}

#
sql_template_postgresql_restriction_by_id = """
--
and pessoa_fisica.id = %(id)s
"""

#
sql_template_postgresql_order_by_id = """
--
order by pessoa_fisica.id
"""

#
sql_template_postgresql_rescriction_pagination = """
--
limit %(page_size)s
offset (%(page_number)s - 1) * %(page_size)s
"""

#
class TsePessoaFisicaResourceService:

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
                '_links_self': (RESOURCE_URL if origin_resource_path is None else '%(url)s%(resource)s' % {'url': os.environ["API_URL"], 'resource': origin_resource_path}),
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