from rest_framework.exceptions import APIException


class HorarioNoPassadoException(APIException):
    status_code = 403
    default_detail = 'Esse horário já passou.'
    default_code = 'service_unavailable'


class HorarioOcupadoException(APIException):
    status_code = 403
    default_detail = 'Não é possível criar esse horário pois haverá conflito de horários na agenda.'
    default_code = 'service_unavailable'


class HorarioInicialMaiorQueFinalException(APIException):
    status_code = 409
    default_detail = 'Horário final não pode ser antes do inicial.'
    default_code = 'service_unavailable'


class DataInválidaException(APIException):
    status_code = 400
    default_detail = 'Data inválida. O formato da data deve ser esse dd-mm-yyyy'
    default_code = 'service_unavailable'