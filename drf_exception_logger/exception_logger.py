from http import HTTPStatus
import uuid
import json
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


class ExceptionLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except:
            err_id = str(uuid.uuid4()).replace('-', '')
            err_payload = {"error": "Internal server error", "errorId": err_id}
            response = HttpResponse(
                json.dumps(err_payload),
                content_type="application/json",
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
            logger.exception(f'errorId:[{err_id}]')

        return response
