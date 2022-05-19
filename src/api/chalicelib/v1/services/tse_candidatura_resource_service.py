#
import psycopg2

from psycopg2.extras import RealDictCursor

import os

#
from chalicelib import util_resource

#
from chalicelib.v1.services import tse_pleito_geral_resource_service
from chalicelib.v1.services import tse_pleito_regional_resource_service
from chalicelib.v1.services import tse_pessoa_fisica_resource_service
from chalicelib.v1.services import tse_cargo_resource_service
from chalicelib.v1.services import tse_pais_resource_service
from chalicelib.v1.services import tse_unidade_federativa_resource_service
from chalicelib.v1.services import tse_municipio_resource_service
from chalicelib.v1.services import tse_partido_resource_service
from chalicelib.v1.services import tse_coligacao_partidaria_resource_service

#
RESOURCE_URL = '%(url)s%(resource)s' % {'url': os.environ["API_URL"], 'resource': util_resource.RESOURCE_URL_V1_TSE_CANDIDATURA}

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
        'id'                    , inner_query.candidatura_id                                ,
        'candidatoSequencial'   , inner_query.candidatura_tse_candidato_sequencial          ,
        'candidatoNumero'       , inner_query.candidatura_tse_candidato_numero              ,
		'candidatoNomeUrna'     , inner_query.candidatura_tse_candidato_nome_urna           ,
		'situacaoCodigo'        , inner_query.candidatura_tse_candidatura_situacao_codigo   ,
		'situacaoDescricao'     , inner_query.candidatura_tse_candidatura_situacao_descricao,
		'protocolo'             , inner_query.candidatura_tse_candidatura_protocolo         ,
		'processoNumero'        , inner_query.candidatura_tse_processo_numero               ,
		'ocupacaoCodigo'        , inner_query.candidatura_tse_ocupacao_codigo               ,
		'ocupacaoDescricao'     , inner_query.candidatura_tse_ocupacao_descricao            ,
		'generoCodigo'          , inner_query.candidatura_tse_genero_codigo                 ,
		'generoDescricao'       , inner_query.candidatura_tse_genero_descricao              ,
		'grauInstrucaoCodigo'   , inner_query.candidatura_tse_grau_instrucao_codigo         ,
		'grauInstrucaoDescricao', inner_query.candidatura_tse_grau_instrucao_descricao      ,
		'estadoCivilCodigo'     , inner_query.candidatura_tse_estado_civil_codigo           ,
		'estadoCivilDescricao'  , inner_query.candidatura_tse_estado_civil_descricao        ,
		'corRacaCodigo'         , inner_query.candidatura_tse_cor_raca_codigo               ,
		'corRacaDescricao'      , inner_query.candidatura_tse_cor_raca_descricao            ,
		'nacionalidadeCodigo'   , inner_query.candidatura_tse_nacionalidade_codigo          ,
		'nacionalidadeDescricao', inner_query.candidatura_tse_nacionalidade_descricao       ,
		'situacaoTurnoCodigo'   , inner_query.candidatura_tse_situacao_turno_codigo         ,
		'situacaoTurnoDescricao', inner_query.candidatura_tse_situacao_turno_descricao      ,
		'reeleicao'             , inner_query.candidatura_tse_reeleicao                     ,
		'bensDeclarar'          , inner_query.candidatura_tse_bens_declarar                 ,
		'email'                 , inner_query.candidatura_tse_email                         ,
		--
		'_embedded', json_build_object
		(
			'pleitoGeral', json_build_object
			(
				--
				'id'           , inner_query.pleito_geral_id                ,
				'codigo'       , inner_query.pleito_geral_tse_codigo        ,
				'descricao'    , inner_query.pleito_geral_tse_descricao     ,
				'turno'        , inner_query.pleito_geral_tse_turno         ,
				'dataHora'     , inner_query.pleito_geral_tse_data_hora     ,
				'tipoCodigo'   , inner_query.pleito_geral_tse_tipo_codigo   ,
				'tipoDescricao', inner_query.pleito_geral_tse_tipo_descricao,
				--
				'_links', json_build_object
				(
					'self', json_build_object
					(
						'href', '%(_embedded_pleito_geral_links_self)s/' || inner_query.candidatura_id_pleito_geral
					)
				)
			),
			'pleitoRegional', json_build_object
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
				'_links', json_build_object
				(
					'self', json_build_object
					(
						'href', '%(_embedded_pleito_regional_links_self)s/' || inner_query.candidatura_id_pleito_regional
					)
				)
			),
			'pessoaFisica', json_build_object
			(
				--
				'id'                , inner_query.pessoa_fisica_id                         ,
				'nome'              , inner_query.pessoa_fisica_tse_nome                   ,
				'nomeSocial'        , inner_query.pessoa_fisica_tse_nome_social            ,
				'nascimentoDataHora', inner_query.pessoa_fisica_tse_data_hora_nascimento   ,
				'cpf'               , inner_query.pessoa_fisica_tse_cpf                    ,
				'tituloEleitoral'   , inner_query.pessoa_fisica_tse_numero_titulo_eleitoral,
				--
				'_links', json_build_object
				(
					'self', json_build_object
					(
						'href', '%(_embedded_pessoa_fisica_links_self)s/' || inner_query.candidatura_id_pessoa_fisica
					)
				)
			),
			'cargo', json_build_object
			(
				--
				'id'       , inner_query.cargo_id           ,
				'sigla'    , inner_query.cargo_tse_codigo   ,
				'descricao', inner_query.cargo_tse_descricao,
				--
				'_links', json_build_object
				(
					'self', json_build_object
					(
						'href', '%(_embedded_cargo_links_self)s/' || inner_query.candidatura_id_cargo
					)
				)
			),			
			'pais', json_build_object
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
						'href', '%(_embedded_pais_links_self)s/' || inner_query.candidatura_id_pais
					)
				)
			),
			'unidadeFederativa', json_build_object
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
						'href', '%(_embedded_unidade_federativa_links_self)s/' || inner_query.candidatura_id_unidade_federativa
					)
				)
			),
			'municipio', json_build_object
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
						'href', '%(_embedded_municipio_links_self)s/' || inner_query.candidatura_id_municipio
					)
				)
			),
			'partido', json_build_object
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
						'href', '%(_embedded_partido_links_self)s/' || inner_query.candidatura_id_partido
					)
				)
			),
			'coligacaoPartidaria', json_build_object
			(
				--
				'id'           , inner_query.coligacao_partidaria_id                      ,
				'sequencial'   , inner_query.coligacao_partidaria_tse_sequencial_coligacao,
				'nome'         , inner_query.coligacao_partidaria_tse_nome                ,
				'tipoDescricao', inner_query.coligacao_partidaria_tse_tipo_descricao      ,
				--
				'_links', json_build_object
				(
					'self', json_build_object
					(
						'href', '%(_embedded_coligacao_partidaria_links_self)s/' || inner_query.candidatura_id_coligacao_partidaria
					)
				)
			)
		),        
        --
        '_links', json_build_object
		(
            'self', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.candidatura_id
            ),
            'bens', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.candidatura_id || '/%(_links_candidatura_bem_sub_resource)s'
            ),
            'fontes', json_build_object
            (
                'href', '%(_links_self)s/' || inner_query.candidatura_id || '/%(_links_fonte_sub_resource)s'
            )
        )
    ) as json_object
--
from 
(
	--
	select distinct
		--
		candidatura.id                                 as candidatura_id                                ,
		candidatura.tse_candidato_sequencial           as candidatura_tse_candidato_sequencial          ,
		candidatura.tse_candidato_numero               as candidatura_tse_candidato_numero              ,
		candidatura.tse_candidato_nome_urna            as candidatura_tse_candidato_nome_urna           ,
		candidatura.tse_candidatura_situacao_codigo    as candidatura_tse_candidatura_situacao_codigo   ,
		candidatura.tse_candidatura_situacao_descricao as candidatura_tse_candidatura_situacao_descricao,
		candidatura.tse_candidatura_protocolo          as candidatura_tse_candidatura_protocolo         ,
		candidatura.tse_processo_numero                as candidatura_tse_processo_numero               ,
		candidatura.tse_ocupacao_codigo                as candidatura_tse_ocupacao_codigo               ,
		candidatura.tse_ocupacao_descricao             as candidatura_tse_ocupacao_descricao            ,
		candidatura.tse_genero_codigo                  as candidatura_tse_genero_codigo                 ,
		candidatura.tse_genero_descricao               as candidatura_tse_genero_descricao              ,
		candidatura.tse_grau_instrucao_codigo          as candidatura_tse_grau_instrucao_codigo         ,
		candidatura.tse_grau_instrucao_descricao       as candidatura_tse_grau_instrucao_descricao      ,
		candidatura.tse_estado_civil_codigo            as candidatura_tse_estado_civil_codigo           ,
		candidatura.tse_estado_civil_descricao         as candidatura_tse_estado_civil_descricao        ,
		candidatura.tse_cor_raca_codigo                as candidatura_tse_cor_raca_codigo               ,
		candidatura.tse_cor_raca_descricao             as candidatura_tse_cor_raca_descricao            ,
		candidatura.tse_nacionalidade_codigo           as candidatura_tse_nacionalidade_codigo          ,
		candidatura.tse_nacionalidade_descricao        as candidatura_tse_nacionalidade_descricao       ,
		candidatura.tse_situacao_turno_codigo          as candidatura_tse_situacao_turno_codigo         ,
		candidatura.tse_situacao_turno_descricao       as candidatura_tse_situacao_turno_descricao      ,
		candidatura.tse_reeleicao                      as candidatura_tse_reeleicao                     ,
		candidatura.tse_bens_declarar                  as candidatura_tse_bens_declarar                 ,
		candidatura.tse_email                          as candidatura_tse_email                         ,
		candidatura.id_pleito_geral                    as candidatura_id_pleito_geral                   ,
		pleito_geral.id                                as pleito_geral_id                               ,
		pleito_geral.tse_codigo                        as pleito_geral_tse_codigo                       ,
		pleito_geral.tse_descricao                     as pleito_geral_tse_descricao                    ,
		pleito_geral.tse_turno                         as pleito_geral_tse_turno                        ,
		pleito_geral.tse_data_hora                     as pleito_geral_tse_data_hora                    ,
		pleito_geral.tse_tipo_codigo                   as pleito_geral_tse_tipo_codigo                  ,
		pleito_geral.tse_tipo_descricao                as pleito_geral_tse_tipo_descricao               ,
		candidatura.id_pleito_regional                 as candidatura_id_pleito_regional                ,
		pleito_regional.id                             as pleito_regional_id                            ,
		pleito_regional.tse_codigo                     as pleito_regional_tse_codigo                    ,
		pleito_regional.tse_descricao                  as pleito_regional_tse_descricao                 ,
		pleito_regional.tse_abragencia_tipo_descricao  as pleito_regional_tse_abragencia_tipo_descricao ,
		pleito_regional.tse_turno                      as pleito_regional_tse_turno                     ,
		pleito_regional.tse_data_hora                  as pleito_regional_tse_data_hora                 ,
		pleito_regional.tse_tipo_codigo                as pleito_regional_tse_tipo_codigo               ,
		pleito_regional.tse_tipo_descricao             as pleito_regional_tse_tipo_descricao            ,
		candidatura.id_pessoa_fisica                   as candidatura_id_pessoa_fisica                  ,
		pessoa_fisica.id                               as pessoa_fisica_id                              ,
		pessoa_fisica.tse_nome                         as pessoa_fisica_tse_nome                        ,
		pessoa_fisica.tse_nome_social                  as pessoa_fisica_tse_nome_social                 ,
		pessoa_fisica.tse_data_hora_nascimento         as pessoa_fisica_tse_data_hora_nascimento        ,
		pessoa_fisica.tse_cpf                          as pessoa_fisica_tse_cpf                         ,
		pessoa_fisica.tse_numero_titulo_eleitoral      as pessoa_fisica_tse_numero_titulo_eleitoral     ,
		candidatura.id_cargo                           as candidatura_id_cargo                          ,
		cargo.id                                       as cargo_id                                      ,
		cargo.tse_codigo                               as cargo_tse_codigo                              ,
		cargo.tse_descricao                            as cargo_tse_descricao                           ,
		candidatura.id_pais                            as candidatura_id_pais                           ,
		pais.id                                        as pais_id                                       ,
		pais.tse_sigla                                 as pais_tse_sigla                                ,
		pais.tse_nome                                  as pais_tse_nome                                 ,
		candidatura.id_unidade_federativa              as candidatura_id_unidade_federativa             ,
		unidade_federativa.id                          as unidade_federativa_id                         ,
		unidade_federativa.tse_sigla                   as unidade_federativa_tse_sigla                  ,
		unidade_federativa.tse_nome                    as unidade_federativa_tse_nome                   ,
		candidatura.id_municipio                       as candidatura_id_municipio                      ,
		municipio.id                                   as municipio_id                                  ,
		municipio.tse_sigla                            as municipio_tse_sigla                           ,
		municipio.tse_nome                             as municipio_tse_nome                            ,
		candidatura.id_partido                         as candidatura_id_partido                        ,
		partido.id                                     as partido_id                                    ,
		partido.tse_numero                             as partido_tse_numero                            ,
		partido.tse_sigla                              as partido_tse_sigla                             ,
		partido.tse_nome                               as partido_tse_nome                              ,
		candidatura.id_coligacao_partidaria            as candidatura_id_coligacao_partidaria           ,
		coligacao_partidaria.id                        as coligacao_partidaria_id                       ,
		coligacao_partidaria.tse_sequencial_coligacao  as coligacao_partidaria_tse_sequencial_coligacao ,
		coligacao_partidaria.tse_nome                  as coligacao_partidaria_tse_nome                 ,
		coligacao_partidaria.tse_tipo_descricao        as coligacao_partidaria_tse_tipo_descricao      
	--
	from      tse.candidatura
	left join tse.pleito_geral         on pleito_geral.id         = candidatura.id_pleito_geral
	left join tse.pleito_regional      on pleito_regional.id      = candidatura.id_pleito_regional
	left join tse.pessoa_fisica        on pessoa_fisica.id        = candidatura.id_pessoa_fisica
	left join tse.cargo                on cargo.id                = candidatura.id_cargo
	left join tse.pais                 on pais.id                 = candidatura.id_pais
	left join tse.unidade_federativa   on unidade_federativa.id   = candidatura.id_unidade_federativa
	left join tse.municipio            on municipio.id            = candidatura.id_municipio
	left join tse.partido              on partido.id              = candidatura.id_partido
	left join tse.coligacao_partidaria on coligacao_partidaria.id = candidatura.id_coligacao_partidaria
	where 1 = 1
    %(sql_template_restriction_by_id)s
    %(sql_template_restriction_by_id_pleito_geral)s
    %(sql_template_restriction_by_id_pleito_regional)s
    %(sql_template_restriction_by_id_pessoa_fisica)s
    %(sql_template_restriction_by_id_cargo)s
    %(sql_template_restriction_by_id_pais)s
    %(sql_template_restriction_by_id_unidade_federativa)s
    %(sql_template_restriction_by_id_municipio)s
    %(sql_template_restriction_by_id_partido)s
    %(sql_template_restriction_by_id_coligacao_partidaria)s					
    %(sql_template_order)s
    %(sql_template_restriction_pagination)s
) as inner_query
""" % {
    '_embedded_pleito_geral_links_self': tse_pleito_geral_resource_service.RESOURCE_URL,
    '_embedded_pleito_regional_links_self': tse_pleito_regional_resource_service.RESOURCE_URL,
    '_embedded_pessoa_fisica_links_self': tse_pessoa_fisica_resource_service.RESOURCE_URL,
    '_embedded_cargo_links_self': tse_cargo_resource_service.RESOURCE_URL,
    '_embedded_pais_links_self': tse_pais_resource_service.RESOURCE_URL,
    '_embedded_unidade_federativa_links_self': tse_unidade_federativa_resource_service.RESOURCE_URL,
    '_embedded_municipio_links_self': tse_municipio_resource_service.RESOURCE_URL,
    '_embedded_partido_links_self': tse_partido_resource_service.RESOURCE_URL,
    '_embedded_coligacao_partidaria_links_self': tse_coligacao_partidaria_resource_service.RESOURCE_URL,
    '_links_self': RESOURCE_URL, 
	'_links_candidatura_bem_sub_resource': util_resource.RESOURCE_V1_TSE_CANDIDATURA_BEM,
    '_links_fonte_sub_resource': util_resource.RESOURCE_V1_TSE_FONTE,
    'sql_template_restriction_by_id': '%(sql_template_restriction_by_id)s',
	'sql_template_restriction_by_id_pleito_geral': '%(sql_template_restriction_by_id_pleito_geral)s',
	'sql_template_restriction_by_id_pleito_regional': '%(sql_template_restriction_by_id_pleito_regional)s',
	'sql_template_restriction_by_id_pessoa_fisica': '%(sql_template_restriction_by_id_pessoa_fisica)s',
	'sql_template_restriction_by_id_cargo': '%(sql_template_restriction_by_id_cargo)s',
	'sql_template_restriction_by_id_pais': '%(sql_template_restriction_by_id_pais)s',
	'sql_template_restriction_by_id_unidade_federativa': '%(sql_template_restriction_by_id_unidade_federativa)s',
	'sql_template_restriction_by_id_municipio': '%(sql_template_restriction_by_id_municipio)s',
	'sql_template_restriction_by_id_partido': '%(sql_template_restriction_by_id_partido)s',
	'sql_template_restriction_by_id_coligacao_partidaria': '%(sql_template_restriction_by_id_coligacao_partidaria)s',
    'sql_template_order': '%(sql_template_order)s',
    'sql_template_restriction_pagination': '%(sql_template_restriction_pagination)s'}

#
sql_template_postgresql_restriction_by_id = """
--
and candidatura.id = %(id)s
"""

#
sql_template_postgresql_restriction_by_id_pleito_geral = """
--
and candidatura.id_pleito_geral = %(id_pleito_geral)s
"""

#
sql_template_postgresql_restriction_by_id_pleito_regional = """
--
and candidatura.id_pleito_regional = %(id_pleito_regional)s
"""

#
sql_template_postgresql_restriction_by_id_pessoa_fisica = """
--
and candidatura.id_pessoa_fisica = %(id_pessoa_fisica)s
"""

#
sql_template_postgresql_restriction_by_id_cargo = """
--
and candidatura.id_cargo = %(id_cargo)s
"""

#
sql_template_postgresql_restriction_by_id_pais = """
--
and candidatura.id_pais = %(id_pais)s
"""

#
sql_template_postgresql_restriction_by_id_unidade_federativa = """
--
and candidatura.id_unidade_federativa = %(id_unidade_federativa)s
"""

#
sql_template_postgresql_restriction_by_id_municipio = """
--
and candidatura.id_municipio = %(id_municipio)s
"""

#
sql_template_postgresql_restriction_by_id_partido = """
--
and candidatura.id_partido = %(id_partido)s
"""

#
sql_template_postgresql_restriction_by_id_coligacao_partidaria = """
--
and candidatura.id_coligacao_partidaria = %(id_coligacao_partidaria)s
"""

#
sql_template_postgresql_order_by_id = """
--
order by candidatura.id
"""

#
sql_template_postgresql_rescriction_pagination = """
--
limit %(page_size)s
offset (%(page_number)s - 1) * %(page_size)s
"""

#
class TseCandidaturaResourceService:

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
                'sql_template_restriction_by_id_pleito_geral': '',
                'sql_template_restriction_by_id_pleito_regional': '',
                'sql_template_restriction_by_id_pessoa_fisica': '',
                'sql_template_restriction_by_id_cargo': '',
                'sql_template_restriction_by_id_pais': '',
                'sql_template_restriction_by_id_unidade_federativa': '',
                'sql_template_restriction_by_id_municipio': '',
                'sql_template_restriction_by_id_partido': '',
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
			id_pleito_geral=None,
			id_pleito_regional=None,
            id_pessoa_fisica=None,
			id_cargo=None,
			id_pais=None,
			id_unidade_federativa=None,
			id_municipio=None,
			id_partido=None,
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
                'sql_template_restriction_by_id_pleito_geral': sql_template_postgresql_restriction_by_id_pleito_geral if (id_pleito_geral is not None) else '',
				'sql_template_restriction_by_id_pleito_regional': sql_template_postgresql_restriction_by_id_pleito_regional if (id_pleito_regional is not None) else '',
                'sql_template_restriction_by_id_pessoa_fisica': sql_template_postgresql_restriction_by_id_pessoa_fisica if (id_pessoa_fisica is not None) else '',
                'sql_template_restriction_by_id_cargo': sql_template_postgresql_restriction_by_id_cargo if (id_cargo is not None) else '',
                'sql_template_restriction_by_id_pais': sql_template_postgresql_restriction_by_id_pais if (id_pais is not None) else '',
                'sql_template_restriction_by_id_unidade_federativa': sql_template_postgresql_restriction_by_id_unidade_federativa if (id_unidade_federativa is not None) else '',
                'sql_template_restriction_by_id_municipio': sql_template_postgresql_restriction_by_id_municipio if (id_municipio is not None) else '',
                'sql_template_restriction_by_id_partido': sql_template_postgresql_restriction_by_id_partido if (id_partido is not None) else '',
                'sql_template_restriction_by_id_coligacao_partidaria': sql_template_postgresql_restriction_by_id_coligacao_partidaria if (id_coligacao_partidaria is not None) else '',
                'sql_template_order': sql_template_postgresql_order_by_id, 
                'sql_template_restriction_pagination': sql_template_postgresql_rescriction_pagination if ((page_number is not None) and (page_size is not None)) else ''}}

            #
            cursor.execute(sql_statement, {
				'id_pleito_geral': id_pleito_geral,
				'id_pleito_regional': id_pleito_regional,
                'id_pessoa_fisica': id_pessoa_fisica,
				'id_cargo': id_cargo,
				'id_pais': id_pais,
				'id_unidade_federativa': id_unidade_federativa,
				'id_municipio': id_municipio,
				'id_partido': id_partido,
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