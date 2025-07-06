
class CookieConsentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lee la cookie y la guarda en request
        request.cookie_consent = request.COOKIES.get('cookie_consent', None)

        response = self.get_response(request)
        return response