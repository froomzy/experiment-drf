from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings

# from experimentdrf.application.renderers import MyRenderer
from . import models, serializers, renderers


class MyResponseMixin:
    """
    Generate a response in the style:
    {
        meta: {
            self: ... 
            count: 2
            links: {
                next: ...
                previous: ...
            }
        },
        results: [
            ...
        ],
        errors: [
            ...
        ]
    }
    
    Meta contains a links section, that will include the self link, as well as pagination links.
    Results will contain a list of results. If there are no results there is an empty list.
    Errors will contain a list of errors. If there are no errors there is an empty list.
    """
    def __init__(self, *args, **kwargs):
        self.paginator = api_settings.DEFAULT_PAGINATION_CLASS()
        super().__init__(*args, **kwargs)

    def get_response(self, data, status):
        meta = {
            "links": {
                "next": self.paginator.get_next_link(),
                "previous": self.paginator.get_previous_link()
            },
            "count": self.paginator.page.paginator.count
        }
        results = data
        errors = []

        result = {
            "meta": meta,
            "results": results,
            "errors": errors
        }
        return Response(result, status=status)


class ApplicationView(MyResponseMixin, APIView):
    renderer_classes = (renderers.MyRenderer,)

    def get(self, request, *args, **kwargs):
        user = request.user
        queryset = models.Application.objects.filter(user=user)
        applications = self.paginator.paginate_queryset(queryset=queryset, request=request, view=self)
        serializer = serializers.ApplicationSerializer(applications, many=True)
        return self.get_response(data=serializer.data, status=status.HTTP_200_OK)
        # return Response(data=serializer.data, status=status.HTTP_200_OK)
        # def get


class ApplicationDetailView(MyResponseMixin, APIView):
    renderer_classes = (renderers.MyRenderer,)

    def get(self, request, *args, **kwargs):
        queryset = models.Application.objects.filter(pk=kwargs['pk'])

