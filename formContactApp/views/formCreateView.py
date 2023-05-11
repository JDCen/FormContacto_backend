from rest_framework import status, views
from rest_framework import Response
from formContactApp.serializers.formSerializer import FormSerializer


class FormCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)
        serializer.is_valid(raise exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)