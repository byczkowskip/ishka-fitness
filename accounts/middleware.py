from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin


class CORPMiddleware(MiddlewareMixin):
    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        response['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
        return response