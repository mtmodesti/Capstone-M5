from rest_framework.exceptions import APIException

class HorarioMarcadoException(APIException):
    status_code = 403
    default_detail = 'Essa horário já está marcado.'
    default_code = 'service_unavailable'


class HorarioPassouException(APIException):
    status_code = 403
    default_detail = 'Essa horário já passou.'
    default_code = 'service_unavailable'


class DataInvalidaException(APIException):
    status_code = 400
    default_detail = 'Data inválida. O formato da data deve ser esse dd-mm-yyyy'
    default_code = 'service_unavailable'
