from django.conf                                import settings
from rest_framework                             import generics, status, views
from rest_framework.response                    import Response
from formContactApp.models.form                 import Form
from formContactApp.serializers.formSerializer  import FormSerializer


#Traer todos los productos
class FormView (generics.ListAPIView):

    queryset = Form.objects.all()
    serializer_class=FormSerializer

#Traer un producto filtrado 
class FormFilterView (generics.ListAPIView):
    serializer_class = FormSerializer

#Crear un producto
class FormCreateView(generics.CreateAPIView):
    serializer_class = FormSerializer    
    queryset=Form.objects.all()

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
    