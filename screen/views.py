from django.shortcuts import render,render_to_response
from django.utils.safestring import mark_safe
# Create your views here.
import json,os
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

def physical (request):
    """
        获取命令，进行物理操作
    """

    code=request.POST.get('keycode')
    os.system("adb shell input keyevent {}".format(code))


class Keycode():
    home="KEYCODE_HOME"
    menu="KEYCODE_MENU"
    back='KEYCODE_BACK'
    light='224'    #唤起屏幕
    dark='223'     #锁屏


def Ui_Xml(request):
    res = standardRes()
    cmd="adb shell uiautomator dump --compressed"
    os.system(cmd)
    devicename='123'
    cmd="adb pull /sdcard/window_dump.xml {}".format("123.xml")
    print(cmd,"cmd")
    os.system(cmd)
    with open("123.xml",'r',encoding='utf-8') as f:
        res['data'] = f.read()

    return JsonResponse(res
    )

def Activity_Package():
    res = standardRes()
    cmd = "adb shell dumpsys window | findstr mCurrentFocus"
    activity = os.popen(cmd).readlines()[0].split('u0')[1].split('/')[0]
    package = os.popen(cmd).readlines()[0].split('u0')[1].split('/')[1].split('}')[0]
    res['data']={"activity":activity,"package":package}
    return JsonResponse(res
    )

def uploadFile(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("E:\\", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作

        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
