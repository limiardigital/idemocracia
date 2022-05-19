# -*- coding: utf-8 -*-

#
import sys

#
import logging

#
import datetime

#
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, Column, Integer

#
import pandas as pd

#
from tqdm import tqdm

#
import unidecode

#
logging.basicConfig(filename=("_script_candidaturas_%s.log" % datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%s')), level=logging.INFO)

#
repositorio_remoto = True

#
banco_dados_remoto = True;

#
producao = True

#
gui = True

#
obtencao_data_fonte = datetime.date(2022, 1, 27)

# DIRETORIO PRINCIPAL

diretorio_principal = 'https://idemocracia-tse-2016-candidatos-2022-01-27.s3.amazonaws.com' if repositorio_remoto else '/'

# LEGENDA

#
diretorio_consulta_coligacao = diretorio_principal + '/consulta_coligacao_2016/'

#
if(producao):

	#
	lista_arquivos_consulta_coligacao = ['consulta_coligacao_2016_AC.csv', 'consulta_coligacao_2016_AL.csv', 'consulta_coligacao_2016_AM.csv', 'consulta_coligacao_2016_AP.csv', 'consulta_coligacao_2016_BA.csv', 'consulta_coligacao_2016_CE.csv', 'consulta_coligacao_2016_ES.csv', 'consulta_coligacao_2016_GO.csv', 'consulta_coligacao_2016_MA.csv', 'consulta_coligacao_2016_MG.csv', 'consulta_coligacao_2016_MS.csv', 'consulta_coligacao_2016_MT.csv', 'consulta_coligacao_2016_PA.csv', 'consulta_coligacao_2016_PB.csv', 'consulta_coligacao_2016_PE.csv', 'consulta_coligacao_2016_PI.csv', 'consulta_coligacao_2016_PR.csv', 'consulta_coligacao_2016_RJ.csv', 'consulta_coligacao_2016_RN.csv', 'consulta_coligacao_2016_RO.csv', 'consulta_coligacao_2016_RR.csv', 'consulta_coligacao_2016_RS.csv', 'consulta_coligacao_2016_SC.csv', 'consulta_coligacao_2016_SE.csv', 'consulta_coligacao_2016_SP.csv', 'consulta_coligacao_2016_TO.csv']

else:

	#
	lista_arquivos_consulta_coligacao = ['consulta_coligacao_2016_AC.csv']

# CANDIDATO

#
diretorio_consulta_candidato = diretorio_principal + '/consulta_cand_2016/'

#
if(producao):

	#
	lista_arquivos_consulta_candidato = ['consulta_cand_2016_AC.csv', 'consulta_cand_2016_AL.csv', 'consulta_cand_2016_AM.csv', 'consulta_cand_2016_AP.csv', 'consulta_cand_2016_BA.csv', 'consulta_cand_2016_CE.csv', 'consulta_cand_2016_ES.csv', 'consulta_cand_2016_GO.csv', 'consulta_cand_2016_MA.csv', 'consulta_cand_2016_MG.csv', 'consulta_cand_2016_MS.csv', 'consulta_cand_2016_MT.csv', 'consulta_cand_2016_PA.csv', 'consulta_cand_2016_PB.csv', 'consulta_cand_2016_PE.csv', 'consulta_cand_2016_PI.csv', 'consulta_cand_2016_PR.csv', 'consulta_cand_2016_RJ.csv', 'consulta_cand_2016_RN.csv','consulta_cand_2016_RO.csv', 'consulta_cand_2016_RR.csv', 'consulta_cand_2016_RS.csv', 'consulta_cand_2016_SC.csv', 'consulta_cand_2016_SE.csv', 'consulta_cand_2016_SP.csv', 'consulta_cand_2016_TO.csv']

else:

	#
	lista_arquivos_consulta_candidato = ['consulta_cand_2016_AC.csv']

# BEM CANDIDATO

#
diretorio_consulta_bem_candidato = diretorio_principal + '/bem_candidato_2016/'

#
if(producao):

	#
	lista_arquivos_consulta_bem_candidato = ['bem_candidato_2016_AC.csv', 'bem_candidato_2016_AL.csv', 'bem_candidato_2016_AM.csv', 'bem_candidato_2016_AP.csv', 'bem_candidato_2016_BA.csv', 'bem_candidato_2016_CE.csv', 'bem_candidato_2016_ES.csv', 'bem_candidato_2016_GO.csv', 'bem_candidato_2016_MA.csv', 'bem_candidato_2016_MG.csv', 'bem_candidato_2016_MS.csv', 'bem_candidato_2016_MT.csv', 'bem_candidato_2016_PA.csv', 'bem_candidato_2016_PB.csv', 'bem_candidato_2016_PE.csv', 'bem_candidato_2016_PI.csv', 'bem_candidato_2016_PR.csv', 'bem_candidato_2016_RJ.csv', 'bem_candidato_2016_RN.csv', 'bem_candidato_2016_RO.csv', 'bem_candidato_2016_RR.csv', 'bem_candidato_2016_RS.csv', 'bem_candidato_2016_SC.csv', 'bem_candidato_2016_SE.csv', 'bem_candidato_2016_SP.csv', 'bem_candidato_2016_TO.csv']

else:

	#
	lista_arquivos_consulta_bem_candidato = ['bem_candidato_2016_AC.csv']

# MOTIVO CASSACAO

#
diretorio_consulta_motivo_cassacao = diretorio_principal + '/motivo_cassacao_2016/'

#
if(producao):

	#
	lista_arquivos_consulta_motivo_cassacao = ['motivo_cassacao_2016_AC.csv', 'motivo_cassacao_2016_AL.csv', 'motivo_cassacao_2016_AM.csv', 'motivo_cassacao_2016_AP.csv', 'motivo_cassacao_2016_BA.csv', 'motivo_cassacao_2016_CE.csv', 'motivo_cassacao_2016_ES.csv', 'motivo_cassacao_2016_GO.csv', 'motivo_cassacao_2016_MA.csv', 'motivo_cassacao_2016_MG.csv', 'motivo_cassacao_2016_MS.csv', 'motivo_cassacao_2016_MT.csv', 'motivo_cassacao_2016_PA.csv', 'motivo_cassacao_2016_PB.csv', 'motivo_cassacao_2016_PE.csv', 'motivo_cassacao_2016_PI.csv', 'motivo_cassacao_2016_PR.csv', 'motivo_cassacao_2016_RJ.csv', 'motivo_cassacao_2016_RN.csv', 'motivo_cassacao_2016_RO.csv', 'motivo_cassacao_2016_RR.csv', 'motivo_cassacao_2016_RS.csv', 'motivo_cassacao_2016_SC.csv', 'motivo_cassacao_2016_SE.csv', 'motivo_cassacao_2016_SP.csv', 'motivo_cassacao_2016_TO.csv']

else:

	#
	lista_arquivos_consulta_motivo_cassacao = ['motivo_cassacao_2016_AC.csv']

# VAGAS

#
diretorio_consulta_vagas = diretorio_principal + '/consulta_vagas_2016/'

#
if(producao):

	#
	lista_arquivos_consulta_vagas = ['consulta_vagas_2016_AC.csv', 'consulta_vagas_2016_AL.csv', 'consulta_vagas_2016_AM.csv', 'consulta_vagas_2016_AP.csv', 'consulta_vagas_2016_BA.csv', 'consulta_vagas_2016_CE.csv', 'consulta_vagas_2016_ES.csv', 'consulta_vagas_2016_GO.csv', 'consulta_vagas_2016_MA.csv', 'consulta_vagas_2016_MG.csv', 'consulta_vagas_2016_MS.csv', 'consulta_vagas_2016_MT.csv', 'consulta_vagas_2016_PA.csv', 'consulta_vagas_2016_PB.csv', 'consulta_vagas_2016_PE.csv', 'consulta_vagas_2016_PI.csv', 'consulta_vagas_2016_PR.csv', 'consulta_vagas_2016_RJ.csv', 'consulta_vagas_2016_RN.csv', 'consulta_vagas_2016_RO.csv', 'consulta_vagas_2016_RR.csv', 'consulta_vagas_2016_RS.csv', 'consulta_vagas_2016_SC.csv', 'consulta_vagas_2016_SE.csv', 'consulta_vagas_2016_SP.csv', 'consulta_vagas_2016_TO.csv']

else:

	#
	lista_arquivos_consulta_vagas = ['consulta_vagas_2016_AC.csv']

#
engine = create_engine('postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/idemocracia' if banco_dados_remoto else 'postgres://postgres:postgres@127.0.0.1:5432/idemocracia', client_encoding='utf8')

#
metadata = MetaData()

#
metadata.reflect(engine, schema='tse')

#
base = automap_base(metadata=metadata)

#
base.prepare()

#
Session = sessionmaker(bind=engine)

#
session = Session()

#
def strptime(date_string, format, default=None):
    
	#
    try:
    
        return datetime.datetime.strptime(date_string, format)
    
    except (ValueError, TypeError):

        return default

#
def tratamento_data_frame(data_frame):

	# Removendo multiplos espaços em branco.
	data_frame = data_frame.replace({'\s+': ' '}, regex=True)

	# Removendo caracter especial "¨".
	for column in data_frame:
		data_frame[column] = data_frame[column].apply(lambda x : x.replace(u"\u00A8", " ") if isinstance(x, str) else x)

	# ASCI II.
	for column in data_frame:
		data_frame[column] = data_frame[column].apply(lambda x : unidecode.unidecode(x) if isinstance(x, str) else x)

	# Upper.
	for column in data_frame:
		data_frame[column] = data_frame[column].apply(lambda x : x.upper() if isinstance(x, str) else x)

	# Trim.
	for column in data_frame:
		data_frame[column] = data_frame[column].apply(lambda x : x.strip() if isinstance(x, str) else x)

	# String.
	for column in data_frame:
		data_frame[column] = data_frame[column].astype(str)

	return data_frame

#
for c in base.classes:
	print('--- Tabela/Entidade : %s' % c)
	print(dir(c))
	print('-----')

#
for file in lista_arquivos_consulta_coligacao:

	#
	arquivo = diretorio_consulta_coligacao + file

	# fonte
	fonte = session.query(base.classes.fonte).filter_by(repositorio_url=arquivo).first()

	#
	if(fonte == None):

		#
		fonte = base.classes.fonte()

	#
	fonte.sigla                = "TSE"
	fonte.descricao            = "Tribunal Superior Eleitoral"
	fonte.url                  = "http://www.tse.jus.br"
	fonte.repositorio_url      = arquivo
	fonte.obtencao_data_hora   = obtencao_data_fonte
	fonte.importacao_data_hora = datetime.datetime.now().date()

	#
	session.add(fonte)

	#
	try:

		#
		data_frame = pd.read_csv(arquivo, encoding='iso-8859-1', delimiter=";", header=0)

		#
		data_frame = tratamento_data_frame(data_frame)

		#
		msg = ('%s - %s' % (arquivo, datetime.datetime.now().strftime('%d/%m/%Y - %I:%M:%s')))

		#
		print(msg)

		#
		logging.info(msg)

		#
		if(gui):

			#
			pbar = tqdm(total=len(data_frame.index))

		#
		for index, row in data_frame.iterrows():

			#
			numero_linha = index + 2

			#
			if(gui):

				# GUI
				pbar.update(1)

			#
			try:

				#
				if((numero_linha % 3000) == 0):

					#
					session.commit()

				# coligacao_partidaria - key
				coligacao_partidaria_key = ('%s' % (row['SQ_COLIGACAO']))

				# coligacao_partidaria
				coligacao_partidaria = session.query(base.classes.coligacao_partidaria).filter_by(tse_key=coligacao_partidaria_key).first()

				#
				if(coligacao_partidaria == None):

					#
					coligacao_partidaria = base.classes.coligacao_partidaria()

				#
				coligacao_partidaria.tse_key                  = coligacao_partidaria_key
				coligacao_partidaria.tse_sequencial_coligacao = str(row['SQ_COLIGACAO'])
				coligacao_partidaria.tse_nome                 = row['NM_COLIGACAO']
				coligacao_partidaria.tse_tipo_descricao       = row['TP_AGREMIACAO']

				#
				session.add(coligacao_partidaria)

				# fonte_referencia - coligacao_partidaria
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, coligacao_partidaria=coligacao_partidaria).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte                = fonte
				fonte_referencia.coligacao_partidaria = coligacao_partidaria
				fonte_referencia.registro             = numero_linha

				#
				session.add(fonte_referencia)

				#
				for sigla_partido in row['DS_COMPOSICAO_COLIGACAO'].split('/'):

					# partido - key
					partido_key = ('%s' % sigla_partido.strip())

					# partido
					partido = session.query(base.classes.partido).filter_by(tse_key=partido_key).first()

					#
					if(partido == None):

						#
						partido = base.classes.partido()

					#
					partido.tse_key   = partido_key
					partido.tse_sigla = sigla_partido.strip()

					#
					session.add(partido)

					# fonte_referencia - partido
					fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, partido=partido).first()

					#
					if(fonte_referencia == None):

						#
						fonte_referencia = base.classes.fonte_referencia()

					#
					fonte_referencia.fonte    = fonte
					fonte_referencia.partido  = partido
					fonte_referencia.registro = numero_linha

					#
					session.add(fonte_referencia)

					# coligacao_partidaria_partido
					coligacao_partidaria_partido = session.query(base.classes.coligacao_partidaria_partido).filter_by(coligacao_partidaria=coligacao_partidaria, partido=partido).first()

					#
					if(coligacao_partidaria_partido == None):

						#
						coligacao_partidaria_partido = base.classes.coligacao_partidaria_partido()

					#
					coligacao_partidaria_partido.coligacao_partidaria = coligacao_partidaria
					coligacao_partidaria_partido.partido              = partido

					#
					session.add(coligacao_partidaria_partido)

					# fonte_referencia - coligacao_partidaria_partido
					fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, coligacao_partidaria_partido=coligacao_partidaria_partido).first()

					#
					if(fonte_referencia == None):

						#
						fonte_referencia = base.classes.fonte_referencia()

					#
					fonte_referencia.fonte                        = fonte
					fonte_referencia.coligacao_partidaria_partido = coligacao_partidaria_partido
					fonte_referencia.registro                     = numero_linha

					#
					session.add(fonte_referencia)

			#
			except:

				#
				msg = ('\n "%s" - "%s" Registro Não Importado - "%s" - "%s" - "%s" \n' % (str(row), arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

				#
				print(msg)

				#
				logging.error(msg)

		#
		session.commit()

		#
		if(gui):

			# GUI
			pbar.close();

		#
		continue

	#
	except:

		#
		msg = ('\n "%s" Arquivo Não Importado - "%s" - "%s" - "%s" \n' % (arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

		#
		print(msg)

		#
		logging.error(msg)

		#
		continue

#
for file in lista_arquivos_consulta_candidato:

	#
	arquivo = diretorio_consulta_candidato + file

	# fonte
	fonte = session.query(base.classes.fonte).filter_by(repositorio_url=arquivo).first()

	#
	if(fonte == None):

		#
		fonte = base.classes.fonte()

	#
	fonte.sigla                = "TSE"
	fonte.descricao            = "Tribunal Superior Eleitoral"
	fonte.url                  = "http://www.tse.jus.br"
	fonte.repositorio_url      = arquivo
	fonte.obtencao_data_hora   = obtencao_data_fonte
	fonte.importacao_data_hora = datetime.datetime.now().date()

	#
	session.add(fonte)

	#
	try:

		#
		data_frame = pd.read_csv(arquivo, encoding='iso-8859-1', delimiter=";", header=0)

		#
		data_frame['NR_CPF_CANDIDATO'] = data_frame['NR_CPF_CANDIDATO'].astype(str)

		#
		data_frame = tratamento_data_frame(data_frame)

		#
		msg = ('%s - %s' % (arquivo, datetime.datetime.now().strftime('%d/%m/%Y - %I:%M:%s')))

		#
		print(msg)

		#
		logging.info(msg)

		#
		if(gui):

			#
			pbar = tqdm(total=len(data_frame.index))

		#
		for index, row in data_frame.iterrows():

			#
			numero_linha = index + 2

			#
			if(gui):

				# GUI
				pbar.update(1)

			#
			try:

				#
				if((numero_linha % 1000) == 0):

					#
					session.commit()

				# pleito_geral - key
				pleito_geral_key = ('%s' % (str(row['CD_ELEICAO'])))

				# pleito_geral
				pleito_geral = session.query(base.classes.pleito_geral).filter_by(tse_key=pleito_geral_key).first()

				#
				if(pleito_geral == None):

					#
					pleito_geral = base.classes.pleito_geral()

				#
				pleito_geral.tse_key            = pleito_geral_key
				pleito_geral.tse_codigo         = row['CD_ELEICAO']
				pleito_geral.tse_descricao      = row['DS_ELEICAO']
				pleito_geral.tse_urno           = row['NR_TURNO']
				pleito_geral.tse_data_hora      = strptime(row['DT_ELEICAO'], '%d/%m/%Y')
				pleito_geral.tse_tipo_codigo    = row['CD_TIPO_ELEICAO']
				pleito_geral.tse_tipo_descricao = row['NM_TIPO_ELEICAO']

				#
				session.add(pleito_geral)

				# fonte_referencia - pleito_geral
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, pleito_geral=pleito_geral).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte        = fonte
				fonte_referencia.pleito_geral = pleito_geral
				fonte_referencia.registro     = numero_linha

				#
				session.add(fonte_referencia)

				# pleito_regional - key
				pleito_regional_key = ('%s-%s-%s' % (str(row['CD_ELEICAO']), str(row['SG_UF']), str(row['SG_UE'])))

				# pleito_regional
				pleito_regional = session.query(base.classes.pleito_regional).filter_by(tse_key=pleito_regional_key).first()

				#
				if(pleito_regional == None):

					#
					pleito_regional = base.classes.pleito_regional()

				#
				pleito_regional.pleito_geral                  = pleito_geral
				pleito_regional.tse_key                       = pleito_regional_key
				pleito_regional.tse_codigo                    = row['CD_ELEICAO']
				pleito_regional.tse_descricao                 = row['DS_ELEICAO']
				pleito_regional.tse_abragencia_tipo_descricao = row['TP_ABRANGENCIA']
				pleito_regional.tse_turno                     = row['NR_TURNO']
				pleito_regional.tse_data_hora                 = strptime(row['DT_ELEICAO'], '%d/%m/%Y')
				pleito_regional.tse_tipo_codigo               = row['CD_TIPO_ELEICAO']
				pleito_regional.tse_tipo_descricao            = row['NM_TIPO_ELEICAO']

				#
				session.add(pleito_regional)

				# fonte_referencia - pleito_regional
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, pleito_regional=pleito_regional).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte           = fonte
				fonte_referencia.pleito_regional = pleito_regional
				fonte_referencia.registro        = numero_linha

				#
				session.add(fonte_referencia)

				# pais_nascimento - key
				pais_nascimento_key = ('%s' % ('BRASIL'))

				# pais_nascimento
				pais_nascimento = session.query(base.classes.pais).filter_by(tse_nome=pais_nascimento_key).first()

				#
				if(pais_nascimento == None):

					#
					pais_nascimento = base.classes.pais()

				#
				pais_nascimento.tse_nome = 'BRASIL'

				#
				session.add(pais_nascimento)

				# fonte_referencia - pais_nascimento
				# N/A

				# unidade_federativa_nascimento - key
				unidade_federativa_nascimento_key = ('%s' % row['SG_UF_NASCIMENTO'])

				# unidade_federativa_nascimento
				unidade_federativa_nascimento = session.query(base.classes.unidade_federativa).filter_by(tse_key=unidade_federativa_nascimento_key).first()

				#
				if(unidade_federativa_nascimento == None):

					#
					unidade_federativa_nascimento = base.classes.unidade_federativa()

				#
				unidade_federativa_nascimento.pais      = pais_nascimento
				unidade_federativa_nascimento.tse_key   = unidade_federativa_nascimento_key
				unidade_federativa_nascimento.tse_sigla = row['SG_UF_NASCIMENTO']

				#
				session.add(unidade_federativa_nascimento)

				# fonte_referencia - unidade_federativa_nascimento
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, unidade_federativa=unidade_federativa_nascimento).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte              = fonte
				fonte_referencia.unidade_federativa = unidade_federativa_nascimento
				fonte_referencia.registro           = numero_linha

				#
				session.add(fonte_referencia)

				# municipio_nascimento - key
				municipio_nascimento_key = ('%s-%s' % (row['SG_UF_NASCIMENTO'], row['NM_MUNICIPIO_NASCIMENTO']))

				# municipio_nascimento
				municipio_nascimento = session.query(base.classes.municipio).filter_by(tse_key=municipio_nascimento_key).first()

				#
				if(municipio_nascimento == None):

					#
					municipio_nascimento = base.classes.municipio()

				#
				municipio_nascimento.unidade_federativa = unidade_federativa_nascimento
				municipio_nascimento.tse_key            = municipio_nascimento_key
				municipio_nascimento.tse_nome           = row['NM_MUNICIPIO_NASCIMENTO']

				#
				session.add(municipio_nascimento)

				# fonte_referencia - municipio_nascimento
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, municipio=municipio_nascimento).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte     = fonte
				fonte_referencia.municipio = municipio_nascimento
				fonte_referencia.registro  = numero_linha

				#
				session.add(fonte_referencia)

				# pessoa_fisica - key
				pessoa_fisica_key = ('%s' % row['NR_CPF_CANDIDATO']).zfill(11)

				# pessoa_fisica
				pessoa_fisica = session.query(base.classes.pessoa_fisica).filter_by(tse_key=pessoa_fisica_key).first()

				#
				if(pessoa_fisica == None):

					#
					pessoa_fisica = base.classes.pessoa_fisica()

				#
				pessoa_fisica.id_pais_nascimento               = pais_nascimento.id
				pessoa_fisica.id_unidade_federativa_nascimento = unidade_federativa_nascimento.id
				pessoa_fisica.id_municipio_nascimento          = municipio_nascimento.id
				pessoa_fisica.tse_key                          = pessoa_fisica_key
				pessoa_fisica.tse_cpf                          = row['NR_CPF_CANDIDATO'].zfill(11)
				pessoa_fisica.tse_nome                         = row['NM_CANDIDATO']
				pessoa_fisica.tse_nome_social                  = row['NM_SOCIAL_CANDIDATO'] if row['NM_SOCIAL_CANDIDATO'] != "#NULO#" else None
				pessoa_fisica.tse_data_hora_nascimento         = strptime(row['DT_NASCIMENTO'], '%d/%m/%Y')
				pessoa_fisica.tse_numero_titulo_eleitoral      = row['NR_TITULO_ELEITORAL_CANDIDATO']

				#
				session.add(pessoa_fisica)

				# fonte_referencia - pessoa_fisica
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, pessoa_fisica=pessoa_fisica).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte         = fonte
				fonte_referencia.pessoa_fisica = pessoa_fisica
				fonte_referencia.registro      = numero_linha

				#
				session.add(fonte_referencia)

				# cargo - key
				cargo_key = ('%s' % (str(row['CD_CARGO'])))

				# cargo
				cargo = session.query(base.classes.cargo).filter_by(tse_key=cargo_key).first()

				#
				if(cargo == None):

					#
					cargo = base.classes.cargo()

				#
				cargo.tse_key       = cargo_key
				cargo.tse_codigo    = row['CD_CARGO']
				cargo.tse_descricao = row['DS_CARGO']

				#
				session.add(cargo)

				# fonte_referencia - cargo
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, cargo=cargo).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte    = fonte
				fonte_referencia.cargo    = cargo
				fonte_referencia.registro = numero_linha

				#
				session.add(fonte_referencia)

				# pais_candidatura - key
				pais_candidatura_key = ('%s' % ('BRASIL'))

				# pais_candidatura
				pais_candidatura = session.query(base.classes.pais).filter_by(tse_nome=pais_candidatura_key).first()

				#
				if(pais_candidatura == None):

					#
					pais_candidatura = base.classes.pais()

				#
				pais_candidatura.tse_nome = 'BRASIL'

				#
				session.add(pais_candidatura)

				# fonte_referencia - pais_candidatura
				# N/A

				# unidade_federativa_candidatura - key
				unidade_federativa_candidatura_key = ('%s' % row['SG_UF'])

				# unidade_federativa_candidatura
				unidade_federativa_candidatura = session.query(base.classes.unidade_federativa).filter_by(tse_key=unidade_federativa_candidatura_key).first()

				#
				if(unidade_federativa_candidatura == None):

					#
					unidade_federativa_candidatura = base.classes.unidade_federativa()

				#
				unidade_federativa_candidatura.pais      = pais_candidatura
				unidade_federativa_candidatura.tse_key   = unidade_federativa_candidatura_key
				unidade_federativa_candidatura.tse_sigla = row['SG_UF']

				#
				session.add(unidade_federativa_candidatura)

				# fonte_referencia - unidade_federativa_candidatura
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, unidade_federativa=unidade_federativa_candidatura).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte              = fonte
				fonte_referencia.unidade_federativa = unidade_federativa_candidatura
				fonte_referencia.registro           = numero_linha

				#
				session.add(fonte_referencia)

				# municipio_candidatura - key
				municipio_candidatura_key = ('%s-%s' % (row['SG_UF'], row['NM_UE']))

				# municipio_candidatura
				municipio_candidatura = session.query(base.classes.municipio).filter_by(tse_key=municipio_candidatura_key).first()

				#
				if(municipio_candidatura == None):

					#
					municipio_candidatura = base.classes.municipio()

				#
				municipio_candidatura.unidade_federativa = unidade_federativa_candidatura
				municipio_candidatura.tse_key            = municipio_candidatura_key
				municipio_candidatura.tse_sigla          = row['SG_UE']
				municipio_candidatura.tse_nome           = row['NM_UE']

				#
				session.add(municipio_candidatura)

				# fonte_referencia - municipio_candidatura
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, municipio=municipio_candidatura).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte     = fonte
				fonte_referencia.municipio = municipio_candidatura
				fonte_referencia.registro  = numero_linha

				#
				session.add(fonte_referencia)

				# coligacao_partidaria - key
				coligacao_partidaria_key = ('%s' % (row['SQ_COLIGACAO']))

				# coligacao_partidaria
				coligacao_partidaria = session.query(base.classes.coligacao_partidaria).filter_by(tse_key=coligacao_partidaria_key).first()

				#
				if(coligacao_partidaria == None):

					#
					coligacao_partidaria = base.classes.coligacao_partidaria()

				#
				coligacao_partidaria.tse_key                  = coligacao_partidaria_key
				coligacao_partidaria.tse_sequencial_coligacao = str(row['SQ_COLIGACAO'])
				coligacao_partidaria.tse_nome                 = row['NM_COLIGACAO']
				coligacao_partidaria.tse_tipo_descricao       = row['TP_AGREMIACAO']

				#
				session.add(coligacao_partidaria)

				# fonte_referencia - coligacao_partidaria
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, coligacao_partidaria=coligacao_partidaria).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte                = fonte
				fonte_referencia.coligacao_partidaria = coligacao_partidaria
				fonte_referencia.registro             = numero_linha

				#
				session.add(fonte_referencia)

				#
				for sigla_partido in row['DS_COMPOSICAO_COLIGACAO'].split('/'):

					# partido - key
					partido_key = ('%s' % sigla_partido.strip())

					# partido
					partido = session.query(base.classes.partido).filter_by(tse_key=partido_key).first()

					#
					if(partido == None):

						#
						partido = base.classes.partido()

					#
					partido.tse_key   = partido_key
					partido.tse_sigla = sigla_partido.strip()

					#
					session.add(partido)

					# fonte_referencia - partido
					fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, partido=partido).first()

					#
					if(fonte_referencia == None):

						#
						fonte_referencia = base.classes.fonte_referencia()

					#
					fonte_referencia.fonte    = fonte
					fonte_referencia.partido  = partido
					fonte_referencia.registro = numero_linha

					#
					session.add(fonte_referencia)

					# coligacao_partidaria_partido
					coligacao_partidaria_partido = session.query(base.classes.coligacao_partidaria_partido).filter_by(coligacao_partidaria=coligacao_partidaria, partido=partido).first()

					#
					if(coligacao_partidaria_partido == None):

						#
						coligacao_partidaria_partido = base.classes.coligacao_partidaria_partido()

					#
					coligacao_partidaria_partido.coligacao_partidaria = coligacao_partidaria
					coligacao_partidaria_partido.partido              = partido

					#
					session.add(coligacao_partidaria_partido)

					# fonte_referencia - coligacao_partidaria_partido
					fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, coligacao_partidaria_partido=coligacao_partidaria_partido).first()

					#
					if(fonte_referencia == None):

						#
						fonte_referencia = base.classes.fonte_referencia()

					#
					fonte_referencia.fonte                        = fonte
					fonte_referencia.coligacao_partidaria_partido = coligacao_partidaria_partido
					fonte_referencia.registro                     = numero_linha

					#
					session.add(fonte_referencia)

				# partido - key
				partido_key = ('%s' % (row['SG_PARTIDO']))

				# partido
				partido = session.query(base.classes.partido).filter_by(tse_key=partido_key).first()

				#
				if(partido == None):

					#
					partido = base.classes.partido()

				#
				partido.tse_key    = partido_key
				partido.tse_numero = row['NR_PARTIDO']
				partido.tse_sigla  = row['SG_PARTIDO']
				partido.tse_nome   = row['NM_PARTIDO']

				#
				session.add(partido)

				# fonte_referencia - partido
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, partido=partido).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte    = fonte
				fonte_referencia.partido  = partido
				fonte_referencia.registro = numero_linha

				#
				session.add(fonte_referencia)					


				# candidatura - key
				candidatura_key = ('%s' % row['SQ_CANDIDATO'])

				# candidatura
				candidatura = session.query(base.classes.candidatura).filter_by(tse_key=candidatura_key).first()

				#
				if(candidatura == None):

					#
					candidatura = base.classes.candidatura()

				#
				candidatura.pleito_geral                       = pleito_geral
				candidatura.pleito_regional                    = pleito_regional
				candidatura.pessoa_fisica                      = pessoa_fisica
				candidatura.cargo                              = cargo
				candidatura.pais                               = pais_candidatura
				candidatura.unidade_federativa                 = unidade_federativa_candidatura
				candidatura.municipio                          = municipio_candidatura
				candidatura.partido                            = partido
				candidatura.coligacao_partidaria               = coligacao_partidaria
				candidatura.tse_key                            = candidatura_key
				candidatura.tse_candidato_sequencial           = row['SQ_CANDIDATO']
				candidatura.tse_candidato_numero               = row['NR_CANDIDATO']
				candidatura.tse_candidato_nome_urna            = row['NM_URNA_CANDIDATO']
				candidatura.tse_candidatura_situacao_codigo    = row['CD_SITUACAO_CANDIDATURA']
				candidatura.tse_candidatura_situacao_descricao = row['DS_SITUACAO_CANDIDATURA']
				candidatura.tse_candidatura_protocolo          = row['NR_PROTOCOLO_CANDIDATURA']
				candidatura.tse_processo_numero                = row['NR_PROCESSO']
				candidatura.tse_ocupacao_codigo                = row['CD_OCUPACAO']
				candidatura.tse_ocupacao_descricao             = row['DS_OCUPACAO']
				candidatura.tse_genero_codigo                  = row['CD_GENERO']
				candidatura.tse_genero_descricao               = row['DS_GENERO']
				candidatura.tse_grau_instrucao_codigo          = row['CD_GRAU_INSTRUCAO']
				candidatura.tse_grau_instrucao_descricao       = row['DS_GRAU_INSTRUCAO']
				candidatura.tse_estado_civil_codigo            = row['CD_ESTADO_CIVIL']
				candidatura.tse_estado_civil_descricao         = row['DS_ESTADO_CIVIL']
				candidatura.tse_cor_raca_codigo                = row['CD_COR_RACA']
				candidatura.tse_cor_raca_descricao             = row['DS_COR_RACA']
				candidatura.tse_nacionalidade_codigo           = row['CD_NACIONALIDADE']
				candidatura.tse_nacionalidade_descricao        = row['DS_NACIONALIDADE']
				candidatura.tse_situacao_turno_codigo          = row['CD_SIT_TOT_TURNO']
				candidatura.tse_situacao_turno_descricao       = row['DS_SIT_TOT_TURNO']
				candidatura.tse_reeleicao                      = row['ST_REELEICAO'].upper() == 'S'
				candidatura.tse_bens_declarar                  = row['ST_DECLARAR_BENS'].upper() == 'S'
				candidatura.tse_email                          = row['NM_EMAIL'].lower()

				#
				session.add(candidatura)

				# fonte_referencia - candidatura
				fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, candidatura=candidatura).first()

				#
				if(fonte_referencia == None):

					#
					fonte_referencia = base.classes.fonte_referencia()

				#
				fonte_referencia.fonte       = fonte
				fonte_referencia.candidatura = candidatura
				fonte_referencia.registro    = numero_linha

				#
				session.add(fonte_referencia)				

				# Garantia de Idempotência -> fonte_referencia -> candidatura_bem
				for candidatura_bem in session.query(base.classes.candidatura_bem).filter_by(candidatura=candidatura).all():
					session.query(base.classes.fonte_referencia).filter_by(candidatura_bem=candidatura_bem).delete()

				# Garantia de Idempotência -> candidatura_bem
				session.query(base.classes.candidatura_bem).filter_by(candidatura=candidatura).delete()

				# Garantia de Idempotência -> fonte_referencia -> candidatura_motivo_cassacao
				for candidatura_motivo_cassacao in session.query(base.classes.candidatura_motivo_cassacao).filter_by(candidatura=candidatura).all():
					session.query(base.classes.fonte_referencia).filter_by(candidatura_motivo_cassacao=candidatura_motivo_cassacao).delete()

				# Garantia de Idempotência -> candidatura_motivo_cassacao
				session.query(base.classes.candidatura_motivo_cassacao).filter_by(candidatura=candidatura).delete()

				#
				continue

			#
			except:

				#
				msg = ('\n "%s" - "%s" Registro Não Importado - "%s" - "%s" - "%s" \n' % (str(row), arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

				#
				print(msg)

				#
				logging.error(msg)

		#
		session.commit()

		#
		if(gui):

			# GUI
			pbar.close();

		#
		continue

	#
	except:

		#
		msg = ('\n "%s" Arquivo Não Importado - "%s" - "%s" - "%s" \n' % (arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

		#
		print(msg)

		#
		logging.error(msg)

		#
		continue

#
for file in lista_arquivos_consulta_bem_candidato:

	#
	arquivo = diretorio_consulta_bem_candidato + file

	# fonte
	fonte = session.query(base.classes.fonte).filter_by(repositorio_url=arquivo).first()

	#
	if(fonte == None):

		#
		fonte = base.classes.fonte()

	#
	fonte.sigla                = "TSE"
	fonte.descricao            = "Tribunal Superior Eleitoral"
	fonte.url                  = "http://www.tse.jus.br"
	fonte.repositorio_url      = arquivo
	fonte.obtencao_data_hora   = obtencao_data_fonte
	fonte.importacao_data_hora = datetime.datetime.now().date()

	#
	session.add(fonte)

	#
	try:

		#
		data_frame = pd.read_csv(arquivo, encoding='iso-8859-1', delimiter=";", header=0)

		#
		data_frame = tratamento_data_frame(data_frame)

		#
		msg = ('%s - %s' % (arquivo, datetime.datetime.now().strftime('%d/%m/%Y - %I:%M:%s')))

		#
		print(msg)

		#
		logging.info(msg)

		#
		if(gui):

			#
			pbar = tqdm(total=len(data_frame.index))

		#
		for index, row in data_frame.iterrows():

			#
			numero_linha = index + 2

			#
			if(gui):

				# GUI
				pbar.update(1)

			#
			try:

				#
				if((numero_linha % 1000) == 0):

					#
					session.commit()

				# candidatura - key
				candidatura_key = ('%s' % (str(row['SQ_CANDIDATO'])))

				# candidatura
				candidatura = session.query(base.classes.candidatura).filter_by(tse_key=candidatura_key).first()

				#
				if(candidatura != None):

					# candidatura_bem - key
					candidatura_bem_key = ('%s-%s' % (str(row['SQ_CANDIDATO']), str(row['NR_ORDEM_CANDIDATO'])))

					# candidatura_bem
					candidatura_bem = session.query(base.classes.candidatura_bem).filter_by(tse_key=candidatura_bem_key).first()

					#
					if(candidatura_bem == None):

						#
						candidatura_bem = base.classes.candidatura_bem()

					#
					candidatura_bem.candidatura                      = candidatura
					candidatura_bem.tse_key                          = candidatura_bem_key
					candidatura_bem.tse_ordem                        = row['NR_ORDEM_CANDIDATO']
					candidatura_bem.tse_tipo_codigo                  = row['CD_TIPO_BEM_CANDIDATO']
					candidatura_bem.tse_tipo_descricao               = row['DS_TIPO_BEM_CANDIDATO']
					candidatura_bem.tse_descricao                    = row['DS_BEM_CANDIDATO']
					candidatura_bem.tse_valor                        = float(row['VR_BEM_CANDIDATO'].replace(',', '.'))
					candidatura_bem.tse_data_hora_ultima_atualizacao = strptime(('%s-%s' % (row['DT_ULTIMA_ATUALIZACAO'], row['HH_ULTIMA_ATUALIZACAO'])), '%d/%m/%Y-%H:%M:%S')

					#
					session.add(candidatura_bem)

					# fonte_referencia - candidatura_bem
					fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, candidatura_bem=candidatura_bem).first()

					#
					if(fonte_referencia == None):

						#
						fonte_referencia = base.classes.fonte_referencia()

					#
					fonte_referencia.fonte           = fonte
					fonte_referencia.candidatura_bem = candidatura_bem
					fonte_referencia.registro        = numero_linha

					#
					session.add(fonte_referencia)

				#
				else:

					#
					msg = ('\n "%s" - "%s" "Alerta Importar - candidatura_bem - não localizado - candidatura \n' % (str(row), arquivo))

					#
					print(msg)

					#
					logging.warning(msg)

				#TODO
				continue

			#
			except:

				#
				msg = ('\n "%s" - "%s" Registro Não Importado - "%s" - "%s" - "%s" \n' % (str(row), arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

				#
				print(msg)

				#
				logging.error(msg)

		#
		session.commit()

		#
		if(gui):

			# GUI
			pbar.close();

		#
		continue

	#
	except:

		#
		msg = ('\n "%s" Arquivo Não Importado - "%s" - "%s" - "%s" \n' % (arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

		#
		print(msg)

		#
		logging.error(msg)

		#
		continue

#
for file in lista_arquivos_consulta_motivo_cassacao:

	#
	arquivo = diretorio_consulta_motivo_cassacao + file

	# fonte
	fonte = session.query(base.classes.fonte).filter_by(repositorio_url=arquivo).first()

	#
	if(fonte == None):

		#
		fonte = base.classes.fonte()

	#
	fonte.sigla                = "TSE"
	fonte.descricao            = "Tribunal Superior Eleitoral"
	fonte.url                  = "http://www.tse.jus.br"
	fonte.repositorio_url      = arquivo
	fonte.obtencao_data_hora   = obtencao_data_fonte
	fonte.importacao_data_hora = datetime.datetime.now().date()

	#
	session.add(fonte)

	#
	try:

		#
		data_frame = pd.read_csv(arquivo, encoding='iso-8859-1', delimiter=";", header=0)

		#
		data_frame = tratamento_data_frame(data_frame)

		#
		msg = ('%s - %s' % (arquivo, datetime.datetime.now().strftime('%d/%m/%Y - %I:%M:%s')))

		#
		print(msg)

		#
		logging.info(msg)

		#
		if(gui):

			#
			pbar = tqdm(total=len(data_frame.index))

		#
		for index, row in data_frame.iterrows():

			#
			numero_linha = index + 2

			#
			if(gui):

				# GUI
				pbar.update(1)

			#
			try:

				#
				if((numero_linha % 1000) == 0):

					#
					session.commit()

				# candidatura - key
				candidatura_key = ('%s' % (str(row['SQ_CANDIDATO'])))

				# candidatura
				candidatura = session.query(base.classes.candidatura).filter_by(tse_key=candidatura_key).first()

				#
				if(candidatura != None):

					# motivo_cassacao - key
					motivo_cassacao_key = ('%s' % (row['DS_MOTIVO_CASSACAO']))

					# motivo_cassacao
					motivo_cassacao = session.query(base.classes.motivo_cassacao).filter_by(tse_key=motivo_cassacao_key).first()

					#
					if(motivo_cassacao == None):

						#
						motivo_cassacao = base.classes.motivo_cassacao()

					#
					motivo_cassacao.tse_key       = motivo_cassacao_key
					motivo_cassacao.tse_descricao = row['DS_MOTIVO_CASSACAO']

					#
					session.add(motivo_cassacao)

					# fonte_referencia - motivo_cassacao
					fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, motivo_cassacao=motivo_cassacao).first()

					#
					if(fonte_referencia == None):

						#
						fonte_referencia = base.classes.fonte_referencia()

					#
					fonte_referencia.fonte           = fonte
					fonte_referencia.motivo_cassacao = motivo_cassacao
					fonte_referencia.registro        = numero_linha

					#
					session.add(fonte_referencia)

					# candidatura_motivo_cassacao
					candidatura_motivo_cassacao = session.query(base.classes.candidatura_motivo_cassacao).filter_by(candidatura=candidatura, motivo_cassacao=motivo_cassacao).first()

					#
					if(candidatura_motivo_cassacao == None):

						#
						candidatura_motivo_cassacao = base.classes.candidatura_motivo_cassacao()

					#
					candidatura_motivo_cassacao.candidatura     = candidatura
					candidatura_motivo_cassacao.motivo_cassacao = motivo_cassacao

					#
					session.add(candidatura_motivo_cassacao)

					# fonte_referencia - candidatura_motivo_cassacao
					fonte_referencia = session.query(base.classes.fonte_referencia).filter_by(fonte=fonte, candidatura_motivo_cassacao=candidatura_motivo_cassacao).first()

					#
					if(fonte_referencia == None):

						#
						fonte_referencia = base.classes.fonte_referencia()

					#
					fonte_referencia.fonte                       = fonte
					fonte_referencia.candidatura_motivo_cassacao = candidatura_motivo_cassacao
					fonte_referencia.registro                    = numero_linha

					#
					session.add(fonte_referencia)

				#
				else:

					#
					msg = ('\n "%s" - "%s" "Alerta Importar - candidatura_motivo_cassacao - não localizado - candidatura \n' % (str(row), arquivo))

					#
					print(msg)

					#
					logging.warning(msg)

				#
				continue

			#
			except:

				#
				msg = ('\n "%s" - "%s" Registro Não Importado - "%s" - "%s" - "%s" \n' % (str(row), arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

				#
				print(msg)

				#
				logging.error(msg)

		#
		session.commit()

		#
		if(gui):

			# GUI
			pbar.close();

		#
		continue

	#
	except:

		#
		msg = ('\n "%s" Arquivo Não Importado - "%s" - "%s" - "%s" \n' % (arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

		#
		print(msg)

		#
		logging.error(msg)

		#
		continue

#
for file in lista_arquivos_consulta_vagas:

	#
	arquivo = diretorio_consulta_vagas + file

	# fonte
	fonte = session.query(base.classes.fonte).filter_by(repositorio_url=arquivo).first()

	#
	if(fonte == None):

		#
		fonte = base.classes.fonte()

	#
	fonte.sigla                = "TSE"
	fonte.descricao            = "Tribunal Superior Eleitoral"
	fonte.url                  = "http://www.tse.jus.br"
	fonte.repositorio_url      = arquivo
	fonte.obtencao_data_hora   = obtencao_data_fonte
	fonte.importacao_data_hora = datetime.datetime.now().date()

	#
	session.add(fonte)

	#
	try:

		#
		data_frame = pd.read_csv(arquivo, encoding='iso-8859-1', delimiter=";", header=0)

		#
		data_frame = tratamento_data_frame(data_frame)

		#
		msg = ('%s - %s' % (arquivo, datetime.datetime.now().strftime('%d/%m/%Y - %I:%M:%s')))

		#
		print(msg)

		#
		logging.info(msg)

		#
		if(gui):

			#
			pbar = tqdm(total=len(data_frame.index))

		#
		for index, row in data_frame.iterrows():

			#
			numero_linha = index + 2

			#
			if(gui):

				# GUI
				pbar.update(1)

			#
			try:

				#
				if((numero_linha % 1000) == 0):

					#
					session.commit()

				# pleito_regional - key
				pleito_regional_key = ('%s-%s-%s' % (str(row['CD_ELEICAO']), str(row['SG_UF']), str(row['SG_UE'])))

				# pleito_regional
				pleito_regional = session.query(base.classes.pleito_regional).filter_by(tse_key=pleito_regional_key).first()

				#
				if(pleito_regional == None):

					#
					msg = ('\n "%s" - "%s" "Alerta Importar - pleito_regional_cargo - não localizado - pleito_regional \n' % (str(row), arquivo))

					#
					print(msg)

					#
					logging.warning(msg)

				# cargo - key
				cargo_key = ('%s' % (str(row['CD_CARGO'])))

				# cargo
				cargo = session.query(base.classes.cargo).filter_by(tse_key=cargo_key).first()

				#
				if(cargo == None):

					#
					msg = ('\n "%s" - "%s" "Alerta Importar - pleito_regional_cargo - não localizado - cargo \n' % (str(row), arquivo))

					#
					print(msg)

					#
					logging.warning(msg)

				#
				if((pleito_regional != None) & (cargo != None)):

					# pleito_regional_cargo
					pleito_regional_cargo = session.query(base.classes.pleito_regional_cargo).filter_by(pleito_regional=pleito_regional, cargo=cargo).first()

					#
					if(pleito_regional_cargo == None):

						#
						pleito_regional_cargo = base.classes.pleito_regional_cargo()

					#
					pleito_regional_cargo.pleito_regional      = pleito_regional
					pleito_regional_cargo.cargo                = cargo
					pleito_regional_cargo.tse_quantidade_vagas = int(row['QT_VAGAS'])

					#
					session.add(pleito_regional_cargo)

				#
				continue

			#
			except:

				#
				msg = ('\n "%s" - "%s" Registro Não Importado - "%s" - "%s" - "%s" \n' % (str(row), arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

				#
				print(msg)

				#
				logging.error(msg)

		#
		session.commit()

		#
		if(gui):

			# GUI
			pbar.close();

		#
		continue

	#
	except:

		#
		msg = ('\n "%s" Arquivo Não Importado - "%s" - "%s" - "%s" \n' % (arquivo, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[-1].tb_lineno))

		#
		print(msg)

		#
		logging.error(msg)

		#
		continue