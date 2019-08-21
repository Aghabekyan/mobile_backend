from rest_framework import status
from rest_framework.exceptions import APIException


class NotAdminException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'error': True, 'message': 'Not Admin'}

class NotOwnerException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'error': True, 'message': 'Not Owner'}
