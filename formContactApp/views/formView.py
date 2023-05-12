from django.conf                                import settings
from rest_framework                             import generics, status, views
from rest_framework.response                    import Response
from formContactApp.models.form                 import Form
from formContactApp.serializers.formSerializer  import FormSerializer
# from django.db  import models


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
    

    # def clean_birth_date(self):
    #     birth_date = self.cleaned_data['birth_date']
    #     age = (date.today() - birth_date) // timedelta(days=365.25)
    #     if age < 18:
    #         raise form.ValidationError("Debes ser mayor de 18 años para registrarte")
    #     return birth_date

# class Form(models.Model):
#     # Definición de campos del modelo

#     # Validación personalizada para no permitir usuarios menores de edad
#     def clean(self):
#         if (date.today() - self.fecha_nacimiento).days < 365 * 18:
#             raise ValidationError("Debe ser mayor de 18 años para registrarse.")

#     # Resto de campos del modelo

# # Señal pre-save para validar la edad antes de guardar el registro
# @receiver(pre_save, sender=Contact)
# def validate_age(sender, instance, **kwargs):
#     instance.clean()