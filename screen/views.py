from django.shortcuts import render,render_to_response
from django.utils.safestring import mark_safe
# Create your views here.
import json
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from run_sft import  devices_info,adb_cmd
import  csv
def standardRes():
    res = {}
    res['status'] = 0
    res['info'] = 'success'
    res['data'] = ''
    return res
def index(request):
    return render(request,"room1.html")

def stf_deivce(request):
    res=standardRes()
    devicename=request.POST['device']
    if devicename=='emulator-5554':
        capport="1717"
        touchport="1111"
    else:
        capport="1718"
        touchport = "1112"
    adb_cmd(devicename,capport,touchport).start_cap()
    adb_cmd(devicename,capport,touchport).start_touch()
    return JsonResponse(res
    )



def get_devices(request):
    res=standardRes()
    devices = devices_info()
    res['data']=devices[0]
    res['count'] = devices[1]
    return JsonResponse(res
    )
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

