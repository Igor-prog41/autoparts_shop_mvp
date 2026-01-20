from apps.catalog.models import PageVisit


class VisitLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith("/admin"):
            return response
        if request.path.startswith("/static"):
            return response

        # visit registration
        if request.method == "GET":
            PageVisit.objects.create(
                ip_address=self.get_client_ip(request),
                path=request.path,
                user_agent=request.META.get("HTTP_USER_AGENT", ""),
            )

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")

