from django.http import HttpResponse
import mygetter

def hello(request):
    # Get our server's information.
    ip  = request.GET.get("ip")
    title = request.GET.get("title")
    motd = request.GET.get("motd")
    # Create the image.
    server_new = mygetter.Server_Stats()
    image = server_new.status_get(ip,title,motd)
    return HttpResponse(image,content_type='image/png')