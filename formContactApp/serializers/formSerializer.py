from rest_framework                 import serializers
from formContactApp.models.form     import Form

class FormSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Form
        fields = ['sexo', 'fecha_nacimiento', 'nombre', 'apellido', 'email', 'direccion', 
        'casa_apto', 'pais', 'departamento', 'ciudad', 'descripcion']

        def create (self, validate_data):
            formInstance = Form.objects.create(**validate_data)
            return formInstance

        def to_representation(self, obj):
            form = Form.objects.get(id=obj.id)
            return {
                "id" : form.id,
                "fecha_nacimiento" : form.fecha_nacimiento,
                "nombre" : form.nombre,
                "apellido" : form.apellido,
                "email" : form.email,
                "direccion" : form.direccion,
                "casa_apto" : form.casa_apto,
                "pais" : form.pais,
                "departamento" : form.departamento,
                "ciudad" : form.ciudad,
                "descripcion" : form.descripcion

            }  

