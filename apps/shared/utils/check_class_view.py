from django.http import JsonResponse
from django.views import View

JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


class BaseView(View):

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return self._response({'errorMessage': e.message}, status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
            json_dumps_params=JSON_DUMPS_PARAMS

        )
