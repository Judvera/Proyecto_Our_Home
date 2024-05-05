from .models import User, Property

def listar_propiedades_comuna(comuna):
    return Property.objects.filter(comuna=comuna)

def listar_propiedades_arrendador(rut_arrendador):
    return Property.objects.filter(usuario_propietario__rut=rut_arrendador)

def actualizar_datos_usuario(rut, telefono_nuevo):
    usuario = User.objects.get(rut=rut)
    usuario.telefono_personal = telefono_nuevo
    usuario.save()

def eliminar_propiedad(id_propiedad):
    propiedad = Property.objects.get(id=id_propiedad)
    propiedad.delete()