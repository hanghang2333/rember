from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf.urls.static import static
import codecs,random,os
from trans.models import IMG
from django.conf import settings

def updata(request):
    print(request)
    if request.FILES:
        if not os.path.exists('upload'):
            os.makedirs('upload')
        imgname = str(request.FILES.get('fileUpload'))
        P = IMG()
        P.img = os.path.join('upload',imgname)
        P.save()
        imgout = codecs.open(os.path.join(settings.MEDIA_ROOT,'upload',imgname),'wb')
        imgout.write(request.FILES.get('fileUpload').read())
        #imgout = codecs.open(os.path.join('upload',imgname),'wb')
        #imgout.write(request.FILES.get('fileUpload').read())
        readtmp = codecs.open('trans/templates/home.html','r','utf8').readlines()[0:10]
        writetmp = codecs.open('trans/templates/home.html','w','utf8')
        writetmp.write(''.join(readtmp))
        writetmp.write("<img src="+'"'+os.path.join('media','upload',imgname)+'"'+'alt="imgname_sample" />'+'\n')
        writetmp.write('</form>\n</body>\n</html>')
        writetmp.close()
    #return render(request,'home.html')
    return HttpResponseRedirect(reverse('ho'))
def home(request):
    from django.conf import settings
    print('+++++',settings.MEDIA_ROOT)

    #img = IMG.objects.all()
    #print('++++----------+++',img)
    #return render(request, 'home1.html', {'img':img})
    return render(request,'home.html')
'''
def receive_data(request):
    if request.GET:
        #print('有提交')
        pass
    s1 = request.GET.get('putonghua',None)
    s2 = request.GET.get('fangyan',None)
    #print('s1&s2:',s1,s2)
    #print(request.GET)
    if request.GET.get('fanyi') != None:
        s2 = model.convert(s1)
        return render(request,'home.html',{'string1':s1,'string2':s2})
    elif request.GET.get('tijiao')!=None:
        output.write('<>'+s1+'<+>'+s2+'<>'+'\n')
        output.flush()
        return render(request,'home.html',{'string1':s1,'string2':s2})
    else:
        idx = int(random.random()*s_num)
        s1 = sentences[idx]
        s2 = model.convert(s1)        
        return render(request,'home.html',{'string1':s1,'string2':s2})
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(reverse('add2',args={a,b}))
'''