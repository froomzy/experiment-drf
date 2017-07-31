from rest_framework.renderers import JSONRenderer


class MyRenderer(JSONRenderer):

    def create_meta(self, paginator):
        return {
            'count': paginator.page.paginator.count,
            'self': 'something goes here',
            'prev': paginator.get_previous_link(),
            'next': paginator.get_next_link()
        }

    def create_errors(self, data):
        return data

    def render(self, data, accepted_media_type=None, renderer_context=None):
        print(renderer_context)
        response = renderer_context.get('response')
        paginator = renderer_context.get('paginator')
        view = renderer_context.get('view')
        print(view)
        if response and response.status_code > 399:
            data = self.create_errors(data=data)
            body_name = 'errors'
        else:
            data = data
            body_name = 'results'

        result = {
            'meta': 'meta',  # self.create_meta(paginator=paginator),
            body_name: data
        }

        return super().render(result, accepted_media_type, renderer_context)
