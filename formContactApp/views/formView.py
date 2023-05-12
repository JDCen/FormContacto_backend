from django.conf                                import settings
from rest_framework                             import generics, status, views
from rest_framework.response                    import Response
from formContactApp.models.form                 import Form
from formContactApp.serializers.formSerializer  import FormSerializer
# from django.db  import models
from datetime import datetime
from dateutil.relativedelta import relativedelta
from rest_framework import serializers


#Traer todos los productos
class FormView (generics.ListAPIView):

    queryset = Form.objects.all()
    serializer_class=FormSerializer

#Traer un producto filtrado 
class FormFilterView (generics.ListAPIView):
    serializer_class = FormSerializer

    def get_queryset(self):
        queryset = Form.objects.filter(id = self.kwargs['pk'])
        return queryset

#Crear un producto
class FormCreateView(generics.CreateAPIView):
    serializer_class = FormSerializer    
    queryset=Form.objects.all()

    def perform_create(self, serializer):
        # Obtener los datos del formulario
        data = serializer.validated_data

        # Validar la fecha de nacimiento
        fecha_nacimiento = data['fecha_nacimiento']
        edad = relativedelta(datetime.now(), fecha_nacimiento).years
        if edad < 18:
            raise serializers.ValidationError('Lo siento, debes ser mayor de edad para registrarte.')

        # Validar la cantidad de registros por ciudad
        ciudad = data['ciudad']
        if Form.objects.filter(ciudad=ciudad).count() >= 3:
            raise serializers.ValidationError('Lo siento, ya se han registrado 3 personas para esta ciudad.')

        # Crear el registro
        serializer.save()

#Eliminar un producto        
class FormDeleteView (generics.DestroyAPIView):
    serializer_class = FormSerializer    
    queryset = Form.objects.all()

    def delete(self, request, *args, **kwargs): 
        return super().destroy(request, *args, **kwargs) 

#Actualizar un producto 
class FormUpdateView(generics.UpdateAPIView):
    serializer_class   = FormSerializer    
    queryset=Form.objects.all()
