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
        print('++++++'+request)
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
