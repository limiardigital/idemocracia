-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.8.0
-- PostgreSQL version: 12
-- Project Site: pgmodeler.com.br
-- Model Author: Joao Paulo Silva Simoes


-- Database creation must be done outside an multicommand file.
-- These commands were put in this file only for convenience.
-- -- object: idemocracia | type: DATABASE --
-- -- DROP DATABASE IF EXISTS idemocracia;
-- 
-- -- Prepended SQL commands --
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
-- -- ddl-end --
-- 
-- CREATE DATABASE idemocracia
-- ;
-- -- ddl-end --
-- 

-- object: tse | type: SCHEMA --
-- DROP SCHEMA IF EXISTS tse CASCADE;
CREATE SCHEMA tse;
-- ddl-end --
ALTER SCHEMA tse OWNER TO postgres;
-- ddl-end --

SET search_path TO pg_catalog,public,tse;
-- ddl-end --

-- object: tse.fonte | type: TABLE --
-- DROP TABLE IF EXISTS tse.fonte CASCADE;
CREATE TABLE tse.fonte(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	sigla text,
	descricao text,
	url text,
	repositorio_url text,
	obtencao_data_hora timestamp,
	importacao_data_hora timestamp,
	CONSTRAINT pk_fonte PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.fonte IS 'Entidade responsavel por armazenar a "Fonte".';
-- ddl-end --
ALTER TABLE tse.fonte OWNER TO postgres;
-- ddl-end --

-- object: tse.coligacao_partidaria | type: TABLE --
-- DROP TABLE IF EXISTS tse.coligacao_partidaria CASCADE;
CREATE TABLE tse.coligacao_partidaria(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	tse_key text,
	tse_sequencial_coligacao text,
	tse_nome text,
	tse_tipo_descricao text,
	CONSTRAINT pk_coligacao_partidaria PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.coligacao_partidaria IS 'Entidade responsavel por armazenar "Coligaçao Partidaria".';
-- ddl-end --
ALTER TABLE tse.coligacao_partidaria OWNER TO postgres;
-- ddl-end --

-- object: ix_coligacao_partidaria_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_coligacao_partidaria_0001 CASCADE;
CREATE INDEX ix_coligacao_partidaria_0001 ON tse.coligacao_partidaria
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.partido | type: TABLE --
-- DROP TABLE IF EXISTS tse.partido CASCADE;
CREATE TABLE tse.partido(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	tse_key text,
	tse_numero text,
	tse_sigla text,
	tse_nome text,
	CONSTRAINT pk_partido PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.partido IS 'Entidade responsavel por armazenar "Partido".';
-- ddl-end --
ALTER TABLE tse.partido OWNER TO postgres;
-- ddl-end --

-- object: tse.coligacao_partidaria_partido | type: TABLE --
-- DROP TABLE IF EXISTS tse.coligacao_partidaria_partido CASCADE;
CREATE TABLE tse.coligacao_partidaria_partido(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_coligacao_partidaria uuid NOT NULL,
	id_partido uuid NOT NULL,
	CONSTRAINT pk_coligacao_partidaria_partido PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.coligacao_partidaria_partido IS 'Entidade responsavel por armazenar a ligaçao "Coligaçao Partidaria" e "Partido".';
-- ddl-end --
ALTER TABLE tse.coligacao_partidaria_partido OWNER TO postgres;
-- ddl-end --

-- object: ix_fonte_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_0001 CASCADE;
CREATE INDEX ix_fonte_0001 ON tse.fonte
	USING btree
	(
	  repositorio_url ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_coligacao_partidaria_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_coligacao_partidaria_0001 CASCADE;
CREATE UNIQUE INDEX uix_coligacao_partidaria_0001 ON tse.coligacao_partidaria
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_coligacao_partidaria_partido_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_coligacao_partidaria_partido_0001 CASCADE;
CREATE INDEX ix_coligacao_partidaria_partido_0001 ON tse.coligacao_partidaria_partido
	USING btree
	(
	  id_coligacao_partidaria ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_coligacao_partidaria_partido_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_coligacao_partidaria_partido_0002 CASCADE;
CREATE INDEX ix_coligacao_partidaria_partido_0002 ON tse.coligacao_partidaria_partido
	USING btree
	(
	  id_partido ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_partido_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_partido_0001 CASCADE;
CREATE INDEX ix_partido_0001 ON tse.partido
	USING btree
	(
	  tse_numero ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.fonte_referencia | type: TABLE --
-- DROP TABLE IF EXISTS tse.fonte_referencia CASCADE;
CREATE TABLE tse.fonte_referencia(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_fonte uuid NOT NULL,
	id_coligacao_partidaria uuid,
	id_coligacao_partidaria_composicao uuid,
	id_partido uuid,
	id_pleito_geral uuid,
	id_pleito_regional uuid,
	id_pessoa_fisica uuid,
	id_cargo uuid,
	id_pais uuid,
	id_unidade_federativa uuid,
	id_municipio uuid,
	id_candidatura uuid,
	id_candidatura_bem uuid,
	id_candidatura_motivo_cassacao uuid,
	id_motivo_cassacao uuid,
	id_pleito_geral_cargo uuid,
	id_pleito_regional_cargo uuid,
	registro varchar(255),
	CONSTRAINT pk_fonte_referencia PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.fonte_referencia IS 'Entidade responsavel por armazenar a ligaçao "Fonte" e demais entidades".';
-- ddl-end --
ALTER TABLE tse.fonte_referencia OWNER TO postgres;
-- ddl-end --

-- object: tse.pleito_geral | type: TABLE --
-- DROP TABLE IF EXISTS tse.pleito_geral CASCADE;
CREATE TABLE tse.pleito_geral(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	tse_key text,
	tse_codigo text,
	tse_descricao text,
	tse_turno text,
	tse_data_hora timestamp,
	tse_tipo_codigo text,
	tse_tipo_descricao text,
	CONSTRAINT pk_pleito_geral PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.pleito_geral IS 'Entidade responsavel por armazenar "Pleito Geral".';
-- ddl-end --
ALTER TABLE tse.pleito_geral OWNER TO postgres;
-- ddl-end --

-- object: uix_partido_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_partido_0001 CASCADE;
CREATE UNIQUE INDEX uix_partido_0001 ON tse.partido
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0001 CASCADE;
CREATE INDEX ix_fonte_referencia_0001 ON tse.fonte_referencia
	USING btree
	(
	  id_fonte ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.pleito_regional | type: TABLE --
-- DROP TABLE IF EXISTS tse.pleito_regional CASCADE;
CREATE TABLE tse.pleito_regional(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_pleito_geral uuid,
	tse_key text,
	tse_codigo text,
	tse_descricao text,
	tse_abragencia_tipo_descricao text,
	tse_turno text,
	tse_data_hora timestamp,
	tse_tipo_codigo text,
	tse_tipo_descricao text,
	CONSTRAINT pk_pleito_regional PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.pleito_regional IS 'Entidade responsavel por armazenar "Pleito Regional".';
-- ddl-end --
ALTER TABLE tse.pleito_regional OWNER TO postgres;
-- ddl-end --

-- object: ix_pleito_geral_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pleito_geral_0001 CASCADE;
CREATE INDEX ix_pleito_geral_0001 ON tse.pleito_geral
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_pleito_geral_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_pleito_geral_0001 CASCADE;
CREATE UNIQUE INDEX uix_pleito_geral_0001 ON tse.pleito_geral
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pleito_regional_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pleito_regional_0001 CASCADE;
CREATE INDEX ix_pleito_regional_0001 ON tse.pleito_regional
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_pleito_regional_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_pleito_regional_0001 CASCADE;
CREATE UNIQUE INDEX uix_pleito_regional_0001 ON tse.pleito_regional
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0002 CASCADE;
CREATE INDEX ix_fonte_referencia_0002 ON tse.fonte_referencia
	USING btree
	(
	  id_coligacao_partidaria ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0003 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0003 CASCADE;
CREATE INDEX ix_fonte_referencia_0003 ON tse.fonte_referencia
	USING btree
	(
	  id_coligacao_partidaria_composicao ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0004 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0004 CASCADE;
CREATE INDEX ix_fonte_referencia_0004 ON tse.fonte_referencia
	USING btree
	(
	  id_partido ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0005 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0005 CASCADE;
CREATE INDEX ix_fonte_referencia_0005 ON tse.fonte_referencia
	USING btree
	(
	  id_pleito_geral ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0006 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0006 CASCADE;
CREATE INDEX ix_fonte_referencia_0006 ON tse.fonte_referencia
	USING btree
	(
	  id_pleito_regional ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.candidatura | type: TABLE --
-- DROP TABLE IF EXISTS tse.candidatura CASCADE;
CREATE TABLE tse.candidatura(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_pleito_geral uuid,
	id_pleito_regional uuid,
	id_pessoa_fisica uuid,
	id_cargo uuid,
	id_pais uuid,
	id_unidade_federativa uuid,
	id_municipio uuid,
	id_partido uuid,
	id_coligacao_partidaria uuid,
	tse_key text,
	tse_candidato_sequencial text,
	tse_candidato_numero text,
	tse_candidato_nome_urna text,
	tse_candidatura_situacao_codigo text,
	tse_candidatura_situacao_descricao text,
	tse_candidatura_protocolo text,
	tse_processo_numero text,
	tse_ocupacao_codigo text,
	tse_ocupacao_descricao text,
	tse_genero_codigo text,
	tse_genero_descricao text,
	tse_grau_instrucao_codigo text,
	tse_grau_instrucao_descricao text,
	tse_estado_civil_codigo text,
	tse_estado_civil_descricao text,
	tse_cor_raca_codigo text,
	tse_cor_raca_descricao text,
	tse_nacionalidade_codigo text,
	tse_nacionalidade_descricao text,
	tse_situacao_turno_codigo text,
	tse_situacao_turno_descricao text,
	tse_reeleicao boolean,
	tse_bens_declarar boolean,
	tse_email text,
	CONSTRAINT pk_candidatura PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.candidatura IS 'Entidade responsavel por armazenar "Candidatura".';
-- ddl-end --
ALTER TABLE tse.candidatura OWNER TO postgres;
-- ddl-end --

-- object: tse.pessoa_fisica | type: TABLE --
-- DROP TABLE IF EXISTS tse.pessoa_fisica CASCADE;
CREATE TABLE tse.pessoa_fisica(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_pais_nascimento uuid,
	id_unidade_federativa_nascimento uuid,
	id_municipio_nascimento uuid,
	tse_key text,
	tse_cpf text,
	tse_nome text,
	tse_nome_social text,
	tse_data_hora_nascimento timestamp,
	tse_numero_titulo_eleitoral text,
	CONSTRAINT pk_pessoa_fisica PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.pessoa_fisica IS 'Entidade responsavel por armazenar "Pessoa Fisica".';
-- ddl-end --
ALTER TABLE tse.pessoa_fisica OWNER TO postgres;
-- ddl-end --

-- object: ix_candidatura_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0001 CASCADE;
CREATE INDEX ix_candidatura_0001 ON tse.candidatura
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pessoa_fisica_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pessoa_fisica_0001 CASCADE;
CREATE INDEX ix_pessoa_fisica_0001 ON tse.pessoa_fisica
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pessoa_fisica_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pessoa_fisica_0002 CASCADE;
CREATE INDEX ix_pessoa_fisica_0002 ON tse.pessoa_fisica
	USING btree
	(
	  id_pais_nascimento ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0002 CASCADE;
CREATE INDEX ix_candidatura_0002 ON tse.candidatura
	USING btree
	(
	  id_pleito_geral ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0003 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0003 CASCADE;
CREATE INDEX ix_candidatura_0003 ON tse.candidatura
	USING btree
	(
	  id_pleito_regional ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0004 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0004 CASCADE;
CREATE INDEX ix_candidatura_0004 ON tse.candidatura
	USING btree
	(
	  id_pessoa_fisica ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0005 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0005 CASCADE;
CREATE INDEX ix_candidatura_0005 ON tse.candidatura
	USING btree
	(
	  id_cargo ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0007 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0007 CASCADE;
CREATE INDEX ix_fonte_referencia_0007 ON tse.fonte_referencia
	USING btree
	(
	  id_pessoa_fisica ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0008 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0008 CASCADE;
CREATE INDEX ix_fonte_referencia_0008 ON tse.fonte_referencia
	USING btree
	(
	  id_cargo ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.cargo | type: TABLE --
-- DROP TABLE IF EXISTS tse.cargo CASCADE;
CREATE TABLE tse.cargo(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	tse_key text,
	tse_codigo text,
	tse_descricao text,
	CONSTRAINT pk_cargo PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.cargo IS 'Entidade responsavel por armazenar "Cargo".';
-- ddl-end --
ALTER TABLE tse.cargo OWNER TO postgres;
-- ddl-end --

-- object: ix_cargo_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_cargo_0001 CASCADE;
CREATE INDEX ix_cargo_0001 ON tse.cargo
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_cargo_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_cargo_0001 CASCADE;
CREATE UNIQUE INDEX uix_cargo_0001 ON tse.cargo
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0006 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0006 CASCADE;
CREATE INDEX ix_candidatura_0006 ON tse.candidatura
	USING btree
	(
	  id_pais ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0009 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0009 CASCADE;
CREATE INDEX ix_fonte_referencia_0009 ON tse.fonte_referencia
	USING btree
	(
	  id_pais ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.pais | type: TABLE --
-- DROP TABLE IF EXISTS tse.pais CASCADE;
CREATE TABLE tse.pais(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	tse_codigo text,
	tse_sigla text,
	tse_nome text,
	CONSTRAINT pk_pais PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.pais IS 'Entidade responsavel por armazenar "Pais".';
-- ddl-end --
ALTER TABLE tse.pais OWNER TO postgres;
-- ddl-end --

-- object: tse.unidade_federativa | type: TABLE --
-- DROP TABLE IF EXISTS tse.unidade_federativa CASCADE;
CREATE TABLE tse.unidade_federativa(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_pais uuid,
	tse_key text,
	tse_sigla text,
	tse_nome text,
	CONSTRAINT pk_unidade_federativa PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.unidade_federativa IS 'Entidade responsavel por armazenar "Unidade Federativa".';
-- ddl-end --
ALTER TABLE tse.unidade_federativa OWNER TO postgres;
-- ddl-end --

-- object: tse.municipio | type: TABLE --
-- DROP TABLE IF EXISTS tse.municipio CASCADE;
CREATE TABLE tse.municipio(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_unidade_federativa uuid,
	tse_key text,
	tse_sigla text,
	tse_nome text,
	CONSTRAINT pk_municipio PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.municipio IS 'Entidade responsavel por armazenar "Municipio".';
-- ddl-end --
ALTER TABLE tse.municipio OWNER TO postgres;
-- ddl-end --

-- object: ix_pais_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pais_0001 CASCADE;
CREATE INDEX ix_pais_0001 ON tse.unidade_federativa
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pais_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pais_0002 CASCADE;
CREATE INDEX ix_pais_0002 ON tse.unidade_federativa
	USING btree
	(
	  id_pais ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_pais_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_pais_0001 CASCADE;
CREATE UNIQUE INDEX uix_pais_0001 ON tse.unidade_federativa
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0010 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0010 CASCADE;
CREATE INDEX ix_fonte_referencia_0010 ON tse.fonte_referencia
	USING btree
	(
	  id_municipio ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0011 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0011 CASCADE;
CREATE INDEX ix_fonte_referencia_0011 ON tse.fonte_referencia
	USING btree
	(
	  id_municipio ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0012 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0012 CASCADE;
CREATE INDEX ix_fonte_referencia_0012 ON tse.fonte_referencia
	USING btree
	(
	  id_candidatura ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_municipio_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_municipio_0001 CASCADE;
CREATE INDEX ix_municipio_0001 ON tse.municipio
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_municipio_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_municipio_0002 CASCADE;
CREATE INDEX ix_municipio_0002 ON tse.municipio
	USING btree
	(
	  id_unidade_federativa ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_municipio_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_municipio_0001 CASCADE;
CREATE UNIQUE INDEX uix_municipio_0001 ON tse.municipio
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0007 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0007 CASCADE;
CREATE INDEX ix_candidatura_0007 ON tse.candidatura
	USING btree
	(
	  id_unidade_federativa ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0008 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0008 CASCADE;
CREATE INDEX ix_candidatura_0008 ON tse.candidatura
	USING btree
	(
	  id_municipio ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0009 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0009 CASCADE;
CREATE INDEX ix_candidatura_0009 ON tse.candidatura
	USING btree
	(
	  id_partido ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pessoa_fisica_0003 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pessoa_fisica_0003 CASCADE;
CREATE INDEX ix_pessoa_fisica_0003 ON tse.pessoa_fisica
	USING btree
	(
	  id_unidade_federativa_nascimento ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pessoa_fisica_0004 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pessoa_fisica_0004 CASCADE;
CREATE INDEX ix_pessoa_fisica_0004 ON tse.pessoa_fisica
	USING btree
	(
	  id_municipio_nascimento ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_pessoa_fisica_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_pessoa_fisica_0001 CASCADE;
CREATE UNIQUE INDEX uix_pessoa_fisica_0001 ON tse.pessoa_fisica
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.candidatura_bem | type: TABLE --
-- DROP TABLE IF EXISTS tse.candidatura_bem CASCADE;
CREATE TABLE tse.candidatura_bem(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_candidatura uuid NOT NULL,
	tse_key text,
	tse_ordem text,
	tse_tipo_codigo text,
	tse_tipo_descricao text,
	tse_descricao text,
	tse_valor numeric(20,6),
	tse_data_hora_ultima_atualizacao timestamp,
	CONSTRAINT pk_candidatura_bem PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.candidatura_bem IS 'Entidade responsavel por armazenar "Candidatura / Bem".';
-- ddl-end --
ALTER TABLE tse.candidatura_bem OWNER TO postgres;
-- ddl-end --

-- object: ix_candidatura_bem_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_bem_0001 CASCADE;
CREATE INDEX ix_candidatura_bem_0001 ON tse.candidatura_bem
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_bem_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_bem_0002 CASCADE;
CREATE INDEX ix_candidatura_bem_0002 ON tse.candidatura_bem
	USING btree
	(
	  id_candidatura ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_candidatura_bem_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_candidatura_bem_0001 CASCADE;
CREATE UNIQUE INDEX uix_candidatura_bem_0001 ON tse.candidatura_bem
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0013 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0013 CASCADE;
CREATE INDEX ix_fonte_referencia_0013 ON tse.fonte_referencia
	USING btree
	(
	  id_candidatura_bem ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.candidatura_motivo_cassacao | type: TABLE --
-- DROP TABLE IF EXISTS tse.candidatura_motivo_cassacao CASCADE;
CREATE TABLE tse.candidatura_motivo_cassacao(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_candidatura uuid NOT NULL,
	id_motivo_cassacao uuid NOT NULL,
	CONSTRAINT pk_candidatura_motivo_cassacao PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.candidatura_motivo_cassacao IS 'Entidade responsavel por armazenar a ligaçao "Candidatura" e "Motivo Cassacao".';
-- ddl-end --
ALTER TABLE tse.candidatura_motivo_cassacao OWNER TO postgres;
-- ddl-end --

-- object: ix_candidatura_motivo_cassacao_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_motivo_cassacao_0001 CASCADE;
CREATE INDEX ix_candidatura_motivo_cassacao_0001 ON tse.candidatura_motivo_cassacao
	USING btree
	(
	  id_candidatura ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_motivo_cassacao_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_motivo_cassacao_0002 CASCADE;
CREATE INDEX ix_candidatura_motivo_cassacao_0002 ON tse.candidatura_motivo_cassacao
	USING btree
	(
	  id_motivo_cassacao ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0014 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0014 CASCADE;
CREATE INDEX ix_fonte_referencia_0014 ON tse.fonte_referencia
	USING btree
	(
	  id_candidatura_motivo_cassacao ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.pleito_geral_cargo | type: TABLE --
-- DROP TABLE IF EXISTS tse.pleito_geral_cargo CASCADE;
CREATE TABLE tse.pleito_geral_cargo(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_pleito_geral uuid NOT NULL,
	id_cargo uuid NOT NULL,
	tse_quantidade_vagas bigint,
	CONSTRAINT pk_pleito_geral_cargo PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.pleito_geral_cargo IS 'Entidade responsavel por armazenar a ligaçao "Pleito Geral" e "Cargo".';
-- ddl-end --
ALTER TABLE tse.pleito_geral_cargo OWNER TO postgres;
-- ddl-end --

-- object: uix_coligacao_partidaria_partido_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_coligacao_partidaria_partido_0001 CASCADE;
CREATE UNIQUE INDEX uix_coligacao_partidaria_partido_0001 ON tse.coligacao_partidaria_partido
	USING btree
	(
	  id_coligacao_partidaria ASC NULLS LAST,
	  id_partido ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pleito_geral_cargo_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pleito_geral_cargo_0001 CASCADE;
CREATE INDEX ix_pleito_geral_cargo_0001 ON tse.pleito_geral_cargo
	USING btree
	(
	  id_pleito_geral ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pleito_geral_cargo_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pleito_geral_cargo_0002 CASCADE;
CREATE INDEX ix_pleito_geral_cargo_0002 ON tse.pleito_geral_cargo
	USING btree
	(
	  id_cargo ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_pleito_geral_cargo_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_pleito_geral_cargo_0001 CASCADE;
CREATE UNIQUE INDEX uix_pleito_geral_cargo_0001 ON tse.pleito_geral_cargo
	USING btree
	(
	  id_pleito_geral ASC NULLS LAST,
	  id_cargo ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0015 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0015 CASCADE;
CREATE INDEX ix_fonte_referencia_0015 ON tse.fonte_referencia
	USING btree
	(
	  id_motivo_cassacao ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.pleito_regional_cargo | type: TABLE --
-- DROP TABLE IF EXISTS tse.pleito_regional_cargo CASCADE;
CREATE TABLE tse.pleito_regional_cargo(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	id_pleito_regional uuid NOT NULL,
	id_cargo uuid NOT NULL,
	tse_quantidade_vagas bigint,
	CONSTRAINT pk_pleito_regional_cargo PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.pleito_regional_cargo IS 'Entidade responsavel por armazenar a ligaçao "Pleito Regional" e "Cargo".';
-- ddl-end --
ALTER TABLE tse.pleito_regional_cargo OWNER TO postgres;
-- ddl-end --

-- object: ix_pleito_regional_cargo_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pleito_regional_cargo_0001 CASCADE;
CREATE INDEX ix_pleito_regional_cargo_0001 ON tse.pleito_regional_cargo
	USING btree
	(
	  id_pleito_regional ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_pleito_regional_cargo_0002 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_pleito_regional_cargo_0002 CASCADE;
CREATE INDEX ix_pleito_regional_cargo_0002 ON tse.pleito_regional_cargo
	USING btree
	(
	  id_cargo ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_pleito_regional_cargo_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_pleito_regional_cargo_0001 CASCADE;
CREATE UNIQUE INDEX uix_pleito_regional_cargo_0001 ON tse.pleito_regional_cargo
	USING btree
	(
	  id_pleito_regional ASC NULLS LAST,
	  id_cargo ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0016 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0016 CASCADE;
CREATE INDEX ix_fonte_referencia_0016 ON tse.fonte_referencia
	USING btree
	(
	  id_pleito_geral_cargo ASC NULLS LAST
	);
-- ddl-end --

-- object: tse.motivo_cassacao | type: TABLE --
-- DROP TABLE IF EXISTS tse.motivo_cassacao CASCADE;
CREATE TABLE tse.motivo_cassacao(
	id uuid NOT NULL DEFAULT uuid_generate_v1(),
	tse_key text,
	tse_codigo text,
	tse_descricao text,
	CONSTRAINT pk_motivo_cassacao PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE tse.motivo_cassacao IS 'Entidade responsavel por armazenar "Cassacao".';
-- ddl-end --
ALTER TABLE tse.motivo_cassacao OWNER TO postgres;
-- ddl-end --

-- object: ix_motivo_cassacao_01 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_motivo_cassacao_01 CASCADE;
CREATE INDEX ix_motivo_cassacao_01 ON tse.motivo_cassacao
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_motivo_cassacao_01 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_motivo_cassacao_01 CASCADE;
CREATE UNIQUE INDEX uix_motivo_cassacao_01 ON tse.motivo_cassacao
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_fonte_referencia_0017 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_fonte_referencia_0017 CASCADE;
CREATE INDEX ix_fonte_referencia_0017 ON tse.fonte_referencia
	USING btree
	(
	  id_pleito_regional_cargo ASC NULLS LAST
	);
-- ddl-end --

-- object: ix_candidatura_0010 | type: INDEX --
-- DROP INDEX IF EXISTS tse.ix_candidatura_0010 CASCADE;
CREATE INDEX ix_candidatura_0010 ON tse.candidatura
	USING btree
	(
	  id_coligacao_partidaria ASC NULLS LAST
	);
-- ddl-end --

-- object: uix_candidatura_0001 | type: INDEX --
-- DROP INDEX IF EXISTS tse.uix_candidatura_0001 CASCADE;
CREATE UNIQUE INDEX uix_candidatura_0001 ON tse.candidatura
	USING btree
	(
	  tse_key ASC NULLS LAST
	);
-- ddl-end --

-- object: fk_coligacao_partidaria_partido_coligacao_partidaria | type: CONSTRAINT --
-- ALTER TABLE tse.coligacao_partidaria_partido DROP CONSTRAINT IF EXISTS fk_coligacao_partidaria_partido_coligacao_partidaria CASCADE;
ALTER TABLE tse.coligacao_partidaria_partido ADD CONSTRAINT fk_coligacao_partidaria_partido_coligacao_partidaria FOREIGN KEY (id_coligacao_partidaria)
REFERENCES tse.coligacao_partidaria (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_coligacao_partidaria_partido_partido | type: CONSTRAINT --
-- ALTER TABLE tse.coligacao_partidaria_partido DROP CONSTRAINT IF EXISTS fk_coligacao_partidaria_partido_partido CASCADE;
ALTER TABLE tse.coligacao_partidaria_partido ADD CONSTRAINT fk_coligacao_partidaria_partido_partido FOREIGN KEY (id_partido)
REFERENCES tse.partido (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_fonte | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_fonte CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_fonte FOREIGN KEY (id_fonte)
REFERENCES tse.fonte (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_coligacao_partidaria | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_coligacao_partidaria CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_coligacao_partidaria FOREIGN KEY (id_coligacao_partidaria)
REFERENCES tse.coligacao_partidaria (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_coligacao_partidaria_composicao | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_coligacao_partidaria_composicao CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_coligacao_partidaria_composicao FOREIGN KEY (id_coligacao_partidaria_composicao)
REFERENCES tse.coligacao_partidaria_partido (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_partido | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_partido CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_partido FOREIGN KEY (id_partido)
REFERENCES tse.partido (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_pleito_geral | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_pleito_geral CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_pleito_geral FOREIGN KEY (id_pleito_geral)
REFERENCES tse.pleito_geral (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_pleito_regional | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_pleito_regional CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_pleito_regional FOREIGN KEY (id_pleito_regional)
REFERENCES tse.pleito_regional (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_pessoa_fisica | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_pessoa_fisica CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_pessoa_fisica FOREIGN KEY (id_pessoa_fisica)
REFERENCES tse.pessoa_fisica (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_cargo | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_cargo CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_cargo FOREIGN KEY (id_cargo)
REFERENCES tse.cargo (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_pais | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_pais CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_pais FOREIGN KEY (id_pais)
REFERENCES tse.pais (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_unidade_federativa | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_unidade_federativa CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_unidade_federativa FOREIGN KEY (id_unidade_federativa)
REFERENCES tse.unidade_federativa (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_municipio | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_municipio CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_municipio FOREIGN KEY (id_municipio)
REFERENCES tse.municipio (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_candidatura | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_candidatura CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_candidatura FOREIGN KEY (id_candidatura)
REFERENCES tse.candidatura (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_candidatura_bem | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_candidatura_bem CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_candidatura_bem FOREIGN KEY (id_candidatura_bem)
REFERENCES tse.candidatura_bem (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_candidatura_motivo_cassacao | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_candidatura_motivo_cassacao CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_candidatura_motivo_cassacao FOREIGN KEY (id_candidatura_motivo_cassacao)
REFERENCES tse.candidatura_motivo_cassacao (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_motivo_cassacao | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_motivo_cassacao CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_motivo_cassacao FOREIGN KEY (id_motivo_cassacao)
REFERENCES tse.motivo_cassacao (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_pleito_geral_cargo | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_pleito_geral_cargo CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_pleito_geral_cargo FOREIGN KEY (id_pleito_geral_cargo)
REFERENCES tse.pleito_geral_cargo (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_fonte_referencia_pleito_regional_cargo | type: CONSTRAINT --
-- ALTER TABLE tse.fonte_referencia DROP CONSTRAINT IF EXISTS fk_fonte_referencia_pleito_regional_cargo CASCADE;
ALTER TABLE tse.fonte_referencia ADD CONSTRAINT fk_fonte_referencia_pleito_regional_cargo FOREIGN KEY (id_pleito_regional_cargo)
REFERENCES tse.pleito_regional_cargo (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_pleito_regional_pleito_geral | type: CONSTRAINT --
-- ALTER TABLE tse.pleito_regional DROP CONSTRAINT IF EXISTS fk_pleito_regional_pleito_geral CASCADE;
ALTER TABLE tse.pleito_regional ADD CONSTRAINT fk_pleito_regional_pleito_geral FOREIGN KEY (id_pleito_geral)
REFERENCES tse.pleito_geral (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_pleito_geral | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_pleito_geral CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_pleito_geral FOREIGN KEY (id_pleito_geral)
REFERENCES tse.pleito_geral (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_pleito_regional | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_pleito_regional CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_pleito_regional FOREIGN KEY (id_pleito_regional)
REFERENCES tse.pleito_regional (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_pessoa_fisica | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_pessoa_fisica CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_pessoa_fisica FOREIGN KEY (id_pessoa_fisica)
REFERENCES tse.pessoa_fisica (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_cargo | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_cargo CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_cargo FOREIGN KEY (id_cargo)
REFERENCES tse.cargo (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_pais | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_pais CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_pais FOREIGN KEY (id_pais)
REFERENCES tse.pais (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_unidade_federativa | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_unidade_federativa CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_unidade_federativa FOREIGN KEY (id_unidade_federativa)
REFERENCES tse.unidade_federativa (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_municipio | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_municipio CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_municipio FOREIGN KEY (id_municipio)
REFERENCES tse.municipio (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_partido | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_partido CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_partido FOREIGN KEY (id_partido)
REFERENCES tse.partido (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_coligacao_partidaria | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura DROP CONSTRAINT IF EXISTS fk_candidatura_coligacao_partidaria CASCADE;
ALTER TABLE tse.candidatura ADD CONSTRAINT fk_candidatura_coligacao_partidaria FOREIGN KEY (id_coligacao_partidaria)
REFERENCES tse.coligacao_partidaria (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_pessoa_fisica_pais_nascimento | type: CONSTRAINT --
-- ALTER TABLE tse.pessoa_fisica DROP CONSTRAINT IF EXISTS fk_pessoa_fisica_pais_nascimento CASCADE;
ALTER TABLE tse.pessoa_fisica ADD CONSTRAINT fk_pessoa_fisica_pais_nascimento FOREIGN KEY (id_pais_nascimento)
REFERENCES tse.pais (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_pessoa_fisica_unidade_federativa_nascimento | type: CONSTRAINT --
-- ALTER TABLE tse.pessoa_fisica DROP CONSTRAINT IF EXISTS fk_pessoa_fisica_unidade_federativa_nascimento CASCADE;
ALTER TABLE tse.pessoa_fisica ADD CONSTRAINT fk_pessoa_fisica_unidade_federativa_nascimento FOREIGN KEY (id_unidade_federativa_nascimento)
REFERENCES tse.unidade_federativa (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_pessoa_fisica_municipio_nascimento | type: CONSTRAINT --
-- ALTER TABLE tse.pessoa_fisica DROP CONSTRAINT IF EXISTS fk_pessoa_fisica_municipio_nascimento CASCADE;
ALTER TABLE tse.pessoa_fisica ADD CONSTRAINT fk_pessoa_fisica_municipio_nascimento FOREIGN KEY (id_municipio_nascimento)
REFERENCES tse.municipio (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_unidade_federativa_pais | type: CONSTRAINT --
-- ALTER TABLE tse.unidade_federativa DROP CONSTRAINT IF EXISTS fk_unidade_federativa_pais CASCADE;
ALTER TABLE tse.unidade_federativa ADD CONSTRAINT fk_unidade_federativa_pais FOREIGN KEY (id_pais)
REFERENCES tse.pais (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_municipio_unidade_federativa | type: CONSTRAINT --
-- ALTER TABLE tse.municipio DROP CONSTRAINT IF EXISTS fk_municipio_unidade_federativa CASCADE;
ALTER TABLE tse.municipio ADD CONSTRAINT fk_municipio_unidade_federativa FOREIGN KEY (id_unidade_federativa)
REFERENCES tse.unidade_federativa (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_bem_candidatura | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura_bem DROP CONSTRAINT IF EXISTS fk_candidatura_bem_candidatura CASCADE;
ALTER TABLE tse.candidatura_bem ADD CONSTRAINT fk_candidatura_bem_candidatura FOREIGN KEY (id_candidatura)
REFERENCES tse.candidatura (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_motivo_cassacao_candidatura | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura_motivo_cassacao DROP CONSTRAINT IF EXISTS fk_candidatura_motivo_cassacao_candidatura CASCADE;
ALTER TABLE tse.candidatura_motivo_cassacao ADD CONSTRAINT fk_candidatura_motivo_cassacao_candidatura FOREIGN KEY (id_candidatura)
REFERENCES tse.candidatura (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_candidatura_motivo_cassacao_motivo_cassacao | type: CONSTRAINT --
-- ALTER TABLE tse.candidatura_motivo_cassacao DROP CONSTRAINT IF EXISTS fk_candidatura_motivo_cassacao_motivo_cassacao CASCADE;
ALTER TABLE tse.candidatura_motivo_cassacao ADD CONSTRAINT fk_candidatura_motivo_cassacao_motivo_cassacao FOREIGN KEY (id_motivo_cassacao)
REFERENCES tse.motivo_cassacao (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_pleito_geral_cargo_pleito_geral | type: CONSTRAINT --
-- ALTER TABLE tse.pleito_geral_cargo DROP CONSTRAINT IF EXISTS fk_pleito_geral_cargo_pleito_geral CASCADE;
ALTER TABLE tse.pleito_geral_cargo ADD CONSTRAINT fk_pleito_geral_cargo_pleito_geral FOREIGN KEY (id_pleito_geral)
REFERENCES tse.pleito_geral (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_pleito_geral_cargo_cargo | type: CONSTRAINT --
-- ALTER TABLE tse.pleito_geral_cargo DROP CONSTRAINT IF EXISTS fk_pleito_geral_cargo_cargo CASCADE;
ALTER TABLE tse.pleito_geral_cargo ADD CONSTRAINT fk_pleito_geral_cargo_cargo FOREIGN KEY (id_cargo)
REFERENCES tse.cargo (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_pleito_regional_cargo_pleito_regional | type: CONSTRAINT --
-- ALTER TABLE tse.pleito_regional_cargo DROP CONSTRAINT IF EXISTS fk_pleito_regional_cargo_pleito_regional CASCADE;
ALTER TABLE tse.pleito_regional_cargo ADD CONSTRAINT fk_pleito_regional_cargo_pleito_regional FOREIGN KEY (id_pleito_regional)
REFERENCES tse.pleito_regional (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_pleito_regional_cargo_cargo | type: CONSTRAINT --
-- ALTER TABLE tse.pleito_regional_cargo DROP CONSTRAINT IF EXISTS fk_pleito_regional_cargo_cargo CASCADE;
ALTER TABLE tse.pleito_regional_cargo ADD CONSTRAINT fk_pleito_regional_cargo_cargo FOREIGN KEY (id_cargo)
REFERENCES tse.cargo (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


