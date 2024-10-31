from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        errors = []

        for fields, messages in exc.detail.items():
            if isinstance(messages, list):
                for message in messages:
                    errors.append({
                        'field': fields,
                        'message': message
                    })
            else:
                errors.append({
                    'field':fields,
                    'message': message
                })
        response.data = {
            'errors' : errors
        }
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    return response
