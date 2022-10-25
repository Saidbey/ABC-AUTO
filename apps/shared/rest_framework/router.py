from rest_framework.routers import SimpleRouter


class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'
