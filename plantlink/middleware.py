class XFrameOptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Content-Security-Policy'] = "frame-ancestors 'self' http://localhost:8000 https://2581-2405-3800-883-def1-c8e1-229-ec28-995a.ngrok-free.app https://27.125.250.42 http://127.0.0.1:8000/"
        return response