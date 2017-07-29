from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from mpdcontroller.models import MpdController

@login_required(login_url='/admin/login')
def command(request, command):
    result_dict = {'command': command}
    mpd_controller = MpdController()
    result_dict.update(mpd_controller.run(command))
    return JsonResponse(result_dict)


@login_required(login_url='/admin/login')
def controller(request):
    return render(request, 'mpdcontroller/index.html', {
        'mpd_http_output_url': settings.MPD_HTTP_OUTPUT_URL,
    })
