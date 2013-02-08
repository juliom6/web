from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from search.models import Publicacion

def buscador(request):
    return render_to_response('search_engine.html', {}, context_instance = RequestContext(request))
def resultados(request):
    if 'q' in request.GET:
		q = request.GET['q']
		publicaciones = Publicacion.objects.filter(titulo__icontains = q)
		return render_to_response('resultados_busqueda.html', {'publicaciones': publicaciones, 'consulta': q})
        #mensaje = 'Acabas de buscar el termino: %r' % request.GET['q']
    else:
        #mensaje = 'Enviaste una busqueda vacia'
    	return HttpResponse('Por favor envia un termino de busqueda.')
def audioyvideo(request):
	c1 = Publicacion.objects.filter(descripcion__icontains = 'audio').count()
	c2 = Publicacion.objects.filter(descripcion__icontains = 'video').count()
	return render_to_response('audioyvideo.html', {'audiocantidad': c1, 'videocantidad': c2})
def audio(request):
	c1 = Publicacion.objects.filter(descripcion__icontains = 'audio').count()
	c2 = Publicacion.objects.filter(descripcion__icontains = 'video').count()
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'audio')
	return render_to_response('audio.html', {'publicaciones': publicaciones, 'audiocantidad': c1, 'videocantidad': c2})
def video(request):
	c1 = Publicacion.objects.filter(descripcion__icontains = 'audio').count()
	c2 = Publicacion.objects.filter(descripcion__icontains = 'video').count()
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'video')
	return render_to_response('video.html', {'publicaciones': publicaciones, 'audiocantidad': c1, 'videocantidad': c2})
def celulares(request):
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'celular')
	return render_to_response('resultados_busqueda.html', {'publicaciones': publicaciones, 'consulta': 'celulares'})
def computacion(request):
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'usb')		
	return render_to_response('resultados_busqueda.html', {'publicaciones': publicaciones, 'consulta': 'computacion'})
def libros(request):
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'libro')
	return render_to_response('resultados_busqueda.html', {'publicaciones': publicaciones, 'consulta': 'libros'})
def instrumentosmusicales(request):
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'instrumento musical')
	return render_to_response('resultados_busqueda.html', {'publicaciones': publicaciones, 'consulta': 'instrumentos musicales'})
def producto(request, id_producto):
	id_producto = int(id_producto)
	publicacion = Publicacion.objects.get(id = id_producto)
	return render_to_response('mostrar_producto.html', {'publicacion': publicacion})
