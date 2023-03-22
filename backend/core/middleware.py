import logging


logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """Логирует метод вызова"""
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        # print("hello from middleware")
        print(request.method)
        print(__name__)
        logger.info(request.method)
        response = self._get_response(request)
        return response
