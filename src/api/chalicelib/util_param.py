#
import uuid

#
QUERY_PARAM_PAGE_NUMBER = 'page_number'
QUERY_PARAM_PAGE_SIZE = 'page_size'

QUERY_PARAM_CANDIDATO_NOME_URNA = 'candidato_nome_urna'
QUERY_PARAM_PESSOA_FISICA_NOME = 'pessoa_fisica_nome'
QUERY_PARAM_PESSOA_FISICA_NOME_SOCIAL = 'pessoa_fisica_nome_social'

#
PATH_PARAM_TSE_ID = 'id'

#
QUERY_PARAM_TSE_ID_COLIGACAO_PARTIDARIA = 'id_coligacao_partidaria'
QUERY_PARAM_TSE_ID_COLIGACAO_PARTIDARIA_COMPOSICAO = 'id_coligacao_partidaria_composicao'
QUERY_PARAM_TSE_ID_PARTIDO = 'id_partido'
QUERY_PARAM_TSE_ID_PLEITO_GERAL = 'id_pleito_geral'
QUERY_PARAM_TSE_ID_PLEITO_REGIONAL = 'id_pleito_regional'
QUERY_PARAM_TSE_ID_PESSOA_FISICA = 'id_pessoa_fisica'
QUERY_PARAM_TSE_ID_CARGO = 'id_cargo'
QUERY_PARAM_TSE_ID_PAIS = 'id_pais'
QUERY_PARAM_TSE_ID_UNIDADE_FEDERATIVA = 'id_unidade_federativa'
QUERY_PARAM_TSE_ID_MUNICIPIO = 'id_municipio'
QUERY_PARAM_TSE_ID_CANDIDATURA = 'id_candidatura'
QUERY_PARAM_TSE_ID_CANDIDATURA_BEM = 'id_candidatura_bem'
QUERY_PARAM_TSE_ID_CANDIDATURA_MOTIVO_CASSACAO = 'id_candidatura_motivo_cassacao'
QUERY_PARAM_TSE_ID_MOTIVO_CASSACAO = 'id_motivo_cassacao'
QUERY_PARAM_TSE_ID_PLEITO_GERAL_CARGO = 'id_pleito_geral_cargo'
QUERY_PARAM_TSE_ID_PLEITO_REGIONAL_CARGO = 'id_pleito_regional_cargo'

#
QUERY_PARAM_PAGE_NUMBER_DEFAULT_VALUE = 1
QUERY_PARAM_PAGE_SIZE_DEFAULT_VALUE = 100

#
def process_path_param_uuid(param_name, param):

    #
    value = param

    #
    try:

        #
        value = str(uuid.UUID(value))

    except Exception as e:

        #
        raise Exception('path_param_value_invalid: param: %(param)s - value: %(value)s' % {'param': param_name, 'value': value})

    #
    return value

#
def process_query_param_uuid(query_params, param_name, required):

    #
    value = None

    #
    if (required and ((query_params is None) or (param_name not in query_params))):

        #
        raise Exception('query_param_required: param: %(param)s' % {'param': param_name});

    #
    if (query_params is not None):

        #
        try:

            #
            value = query_params[param_name]

        except Exception as e:

            #
            value = None

        #
        if (value is not None):

            #
            try:

                #
                value = str(uuid.UUID(value))

            except Exception as e:

                #
                raise Exception('query_param_value_invalid: param: %(param)s - value: %(value)s' % {'param': param_name, 'value': value})

    #
    return value

#
def process_query_param_integer(query_params, param_name, required, minValue, maxValue, defaultValue = None):

    #
    value = None

    #
    if (required and ((query_params is None) or (param_name not in query_params))):

        #
        raise Exception('query_param_required: param: %(param)s' % {'param': param_name});

    #
    if (query_params is not None):

        #
        try:

            #
            value = query_params[param_name]

        except Exception as e:

            #
            value = defaultValue

        #
        if (value is not None):

            #
            try:

                #
                value = int(value)

            except:

                #
                raise Exception('query_param_value_invalid: param: %(param)s - value: %(value)s' % {'param': param_name, 'value': value});

            # 
            if not ((value >= minValue) and (value <= maxValue)):

                #
                raise Exception('query_param_out_of_range: param: %(param)s - value: %(value)s - min_value: %(minValue)s - max_value: %(maxValue)s' % {'param': param_name, 'value': value, 'minValue': minValue, 'maxValue': maxValue});

    else:

        #
        value = defaultValue

    #
    return value

#
def process_query_param_string(query_params, param_name, required):

    #
    value = None

    #
    if (required and ((query_params is None) or (param_name not in query_params))):

        #
        raise Exception('query_param_required: param: %(param)s' % {'param': param_name});

    #
    if (query_params is not None):

        #
        try:

            #
            value = query_params[param_name]

        except Exception as e:

            #
            value = None

        #
        if (value is not None):

            #
            try:

                #
                value = str(value.replace('*', '%'))

            except Exception as e:

                #
                raise Exception('query_param_value_invalid: param: %(param)s - value: %(value)s' % {'param': param_name, 'value': value})

    #
    return value