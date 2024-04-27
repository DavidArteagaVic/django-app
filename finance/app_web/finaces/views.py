from django.shortcuts import render, redirect
from .models import clientes
from .models import Transaccion
from .forms import ClienteForm

def visualizar_clientes(request):
    # Obtener todos los objetos de Clientes
    clientes1 = clientes.objects.all()
    
    # Pasar los clientes a la plantilla
    return render(request, 'visualizar_clientes.html', {'clientes': clientes1})



def visualizar_transacciones(request):
    # Obtener todas las transacciones
    transacciones = Transaccion.objects.all()
    
    # Pasar las transacciones a la plantilla
    return render(request, 'visualizar_transacciones.html', {'transacciones': transacciones})



def crear_cliente(request):
    if request.method == 'POST':
        # Si se envió un formulario, procesarlo
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito después de crear el cliente
            return redirect('pagina_de_exito')
    else:
        # Si es una solicitud GET, mostrar el formulario vacío
        form = ClienteForm()
    
    return render(request, 'crear_cliente.html', {'form': form})

