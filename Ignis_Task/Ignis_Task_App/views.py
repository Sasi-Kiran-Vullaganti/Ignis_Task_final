from django.shortcuts import redirect, render,HttpResponse
from Ignis_Task_App.models import Events
# Create your views here.
def home(request):
    events = Events.objects.all()
    context = {'events':events}
    return render(request,'home.html',context)

def addEvent(request):
    if request.method=='POST':
        ename = request.POST['ename']
        eloc = request.POST.get('eloc')
        edate = request.POST.get('edate')
        etime = request.POST.get('etime')
        if len(request.FILES) !=0:
            eimg = request.FILES['eimg']
        print(ename+eloc+edate+etime)
        ins = Events(event_name=ename,location=eloc,event_date=edate,event_time=etime,event_image=eimg,like="False")
        ins.save()
        mess = {'message':True}
        return redirect('/')
    else:
        return render(request,'addEvent.html')

def allLikeEvents(request):
    events = Events.objects.all()
    context = {'events':events}
    return render(request,'allLikedEvent.html',context)

def like(request,eid):
    events = Events.objects.filter(id=eid).update(like=True)
    return redirect('/')

def dislike(request,eid):
    events = Events.objects.filter(id=eid).update(like=False)
    return redirect('/')