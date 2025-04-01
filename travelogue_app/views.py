import uuid
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.serializers.json import DjangoJSONEncoder

from travelogue_app.models import *
# Create your views here.


####jishnu functions
def instreenode(nodeid,venueid,distance,parentnodeid,level):
    n=tree()
    n.nodeid=nodeid
    n.venueid=venueid
    n.distance=distance
    n.parentnodeid=parentnodeid
    n.level=level
    n.save()

    # qry="INSERT INTO `tree`(nodeid,`venueid`,`distance`,`parentnodeid`,`level`)VALUES('"+str(nodeid)+"','"+str(venueid)+"','"+str(distance)+"','"+str(parentnodeid)+"','"+str(level)+"')"
    # db=Db()
    # res=db.insert(qry)

def getparentnodeid(nodeid):


    data= tree.objects.get(nodeid=nodeid)
    return data.parentnodeid

def getleafnodeidies():
    nodeids_not_in_parents = tree.objects.exclude(nodeid__in=tree.objects.values('parentnodeid')).values('nodeid')
    nodeid=[]
    for i in nodeids_not_in_parents:
        print(i,"==========")
        nodeid.append(i['nodeid'])
    return nodeid
    # qry="SELECT `nodeid` FROM `tree` WHERE `nodeid` NOT IN (SELECT `parentnodeid` FROM `tree`)"
    # db=Db()
    # res=db.select(qry)
    # nodeid=[]
    # for i in res:
    #     nodeid.append(i['nodeid'])
    #
    # return nodeid
    #





######end jishnu functions



def home(request):
    places_count = Place.objects.count()  
    dfd = Place.objects.all()
    
    user_c=User.objects.count()
    
    fe=Feedback.objects.count()
    re=Review.objects.count()
    
    fefull=Feedback.objects.all()



    return render(request, "home.html", {'dfd': dfd, 'places_count': places_count,'user_c': user_c,'fe': fe,'re':re,'fefull':fefull})




def log(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pawd')

        try:
            lg = Login.objects.get(username=uname, password=pwd)
            request.session['login_id']=lg.pk

            if lg.utype == "admin":
               
                return HttpResponse("<script>alert('Login Success !');window.location='adminhome'</script>")
            
            else:
                return HttpResponse("<script>alert('Invalid Entry');window.location='/login'</script>")
        except Login.DoesNotExist:
            return HttpResponse("<script>alert('LOGIN FAILD ');window.location='/login'</script>")

    return render(request,"login.html")


def admin_view_users(request):
    b=User.objects.all()
    return render(request,"admin_view_users.html",{'b':b})


def adminhome(request):
    b=User.objects.all()
    return render(request,"adminhome.html",{'b':b})

def admin_manage_notification(request):
    ss= Notification.objects.all()
    print(ss)
    if request.method == "POST":
        noti = request.POST.get('noti') 
        today_date = timezone.now().date() 
        pop = Notification(notification=noti, date=today_date)
        pop.save()
        return HttpResponse("<script>alert('added');window.location='admin_manage_notification'</script>")

    return render(request, "admin_manage_notification.html",{'ss':ss})


def admin_update_notification(request,id):
    upd=Notification.objects.get(id=id)
    print(upd)
    if request.method=="POST":
        noti = request.POST['noti']
        today_date = timezone.now().date() 
        
        upd.notification=noti
        upd.date=today_date
        upd.save()
        return HttpResponse("<script>alert('Updated');window.location='/admin_manage_notification'</script>")

    return render(request, "admin_manage_notification.html",{'upd':upd})


def admin_delete_notification(request,id):
    dte=Notification.objects.get(id=id)
    dte.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/admin_manage_notification'</script>")

def admin_view_feedback(request):
    feed=Feedback.objects.all()
    return render(request,"admin_view_feedback.html",{'feed':feed})



def admin_manage_places(request):
    ss= Place.objects.all()
    cc=category.objects.all()
    print(ss)
    if request.method == "POST":
        plc_name = request.POST['plc_name']
        city = request.POST['city']
        LandMark = request.POST['lmark']
        State = request.POST['state']
        lati = request.POST['lati']
        longi = request.POST['longi']
        cat = request.POST['cat']

        pop = Place(place_name=plc_name,city=city,landmark=LandMark,state=State,lati=lati,longi=longi,status="pending",CATEGORY_id=cat)
        pop.save()
        return HttpResponse("<script>alert('added');window.location='/admin_manage_places'</script>")

    return render(request, "admin_manage_places.html",{'ss':ss,"cc":cc})


def admin_update_places(request,id):
    obj=Place.objects.get(id=id)
    if 'update' in request.POST:
        plc_name = request.POST['plc_name']
        city = request.POST['city']
        LandMark = request.POST['lmark']
        State = request.POST['state']
        lati = request.POST['lati']
        longi = request.POST['longi']
        
        
        obj.place_name=plc_name
        obj.city=city
        obj.landmark=LandMark
        obj.state=State
        obj.lati=lati
        obj.longi=longi
        obj.save()
        return HttpResponse("<script>alert('updated');window.location='/admin_manage_places'</script>")

    return render(request, "admin_manage_places.html",{'obj':obj})
    
    
def admin_delete_delete(request,id):
    obj=Place.objects.get(id=id)
    obj.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/admin_manage_places'</script>")



def admin_manage_package(request):
    ss= Package.objects.all()
    rev=Facility.objects.all()
    
    print(ss)
    if request.method == "POST":
        facility = request.POST['facility']
        pkname = request.POST['pkname']
        description = request.POST['description']
        valid_from = request.POST['valid_from']
        valid_till = request.POST['valid_till']
        price = request.POST['price']
        
        pop = Package(package_name=pkname,facility=facility,description=description,valid_from=valid_from,valid_till=valid_till,price=price,facility_id=facility)
        pop.save()
        return HttpResponse("<script>alert('added');window.location='/admin_manage_package'</script>")

    return render(request,"admin_manage_package.html",{'ss':ss,'rev':rev})

def admin_update_package(request,id):
    rev=Facility.objects.all()
    obj=Package.objects.get(package_id=id)
    if 'update' in request.POST:
        fa = request.POST['fac']
        pkname = request.POST['pkname']
        description = request.POST['description']
        valid_from = request.POST['valid_from']
        valid_till = request.POST['valid_till']
        price = request.POST['price']
        
        
        obj.facility_id=fa
        obj.package_name=pkname
        obj.description=description
        obj.valid_from=valid_from
        obj.valid_till=valid_till
        obj.price=price
        obj.save()
        return HttpResponse("<script>alert('updated');window.location='/admin_manage_package'</script>")

    return render(request,"admin_manage_package.html",{'obj':obj,'rev':rev})
    

def admin_delete_package(request,id):
    obj=Package.objects.get(package_id=id)
    obj.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/admin_manage_package'</script>")

def admin_view_review(request):
    rev=Review.objects.all()
    return render(request,'admin_view_review.html',{'rev':rev})




def admin_manage_facility(request):
    obj=Facility.objects.all()

    if request.method=='POST':
       
        type=request.POST['type']
        name=request.POST['name']
        lati=request.POST['lati']
        longi=request.POST['longi']
        email=request.POST['email']
        place=request.POST['place']
        city=request.POST['city']
        state=request.POST['state']
        phone=request.POST['phone']
        image=request.FILES['img1']
        fs = FileSystemStorage()
        f_nam =fs.save(image.name, image)
        ab=Facility(type=type,f_name=name,f_place=place,lati=lati,longi=longi,city=city,state=state,phone=phone,email=email,photo=f_nam)
        ab.save()
        return HttpResponse("<script>alert('Success');window.location='/admin_manage_facility'</script>")
    return render(request,'admin_manage_facility.html',{'obj':obj})

    


def admin_update_facility(request,id):
    obj1=Facility.objects.get(id=id)
    if 'update' in request.POST:
        type=request.POST['type']
        name=request.POST['name']
        lati=request.POST['lati']
        longi=request.POST['longi']
        email=request.POST['email']
        place=request.POST['place']
        city=request.POST['city']
        state=request.POST['state']
        phone=request.POST['phone']
        image=request.FILES['img1']
        fs = FileSystemStorage()
        f_nam =fs.save(image.name, image)
        
        
        obj1.type=type
        obj1.f_name=name
        obj1.lati=lati
        obj1.longi=longi
        obj1.email=email
        obj1.f_place=place
        obj1.city=city
        obj1.state=state
        obj1.phone=phone
        obj1.photo=f_nam
        obj1.save()
        return HttpResponse("<script>alert('updated');window.location='/admin_manage_facility'</script>")

    return render(request,"admin_manage_facility.html",{'obj1':obj1})
    
    
    

def admin_delete_facility(request,id):
    obj1=Facility.objects.get(id=id)
    obj1.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/admin_manage_facility'</script>")



   
##########################################################################################3





def andlogin(request):
    uname=request.POST['user']
    password=request.POST['pass']




    obj=Login.objects.filter(username=uname,password=password)

    if obj.exists():
        obj=obj[0]
        print(obj,"hiiiii")
        return JsonResponse(
            {
                'status':'ok',
                'lid':obj.id
            }
        )
    else:
        return JsonResponse(
            {
                'status':'no'
            }
        )

        


def user_registration(request):
    name=request.POST['name']
    place=request.POST['place']
    # post=request.POST['address']
    pin=request.POST['pincode']
    phonenumber=request.POST['phone']
    email=request.POST['email']
    gender=request.POST['gender']
    photo=request.POST['photo']
    confirmpassword=request.POST['pass']

    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(photo)
    fh = open("C:\\Users\\computer\\Downloads\\smart travelogue(thelast)\\smart travelogue\\Smart_Travelogue\\static\\" + date + ".jpg", "wb")
    path =  '/static/' + date + '.jpg'
    fh.write(a)
    fh.close()



    lg=Login()
    lg.username=email
    lg.password=confirmpassword
    lg.type='pending'
    lg.save()

    dobj=User()
    dobj.Name=name
    dobj.Place=place
    # dobj.Post=post
    dobj.Pin=pin
    dobj.Phonenumber=phonenumber
    dobj.Email=email
    dobj.Gender=gender
    dobj.Photo=path
    dobj.LOGIN=lg
    dobj.save()
    return JsonResponse({"status": "ok"})



def user_viewprofile(request):
    lid=request.POST['lid']
    data=User.objects.get(LOGIN_id=lid)
    return JsonResponse({"status":"ok",
                         'name':data.Name,
                         'place':data.Place,
                         'post':data.Post,
                         'pin':data.Pin,
                         'phone':data.Phonenumber,
                         'email':data.Email,
                         'gender':data.Gender,
                         'photo':data.Photo,

                         })

def user_editprofile(request):
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phonenumber = request.POST['phonenumber']
    email = request.POST['email']
    gender = request.POST['gender']
    photo = request.POST['photo']
    lid = request.POST['lid']
    dobj = User.objects.get(LOGIN=lid)
    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    if len(photo)>0:
        a = base64.b64decode(photo)
        fh = open(r"C:\\Users\\computer\\Downloads\\smart travelogue(thelast)\\smart travelogue\\Smart_Travelogue\\static\\" + date + ".jpg", "wb")
        path = '/static/' + date + '.jpg'
        fh.write(a)
        fh.close()

        dobj.Photo = path
        dobj.save()

    dobj.Name = name
    dobj.place = place
    dobj.post = post
    dobj.pin = pin
    dobj.phonenumber = phonenumber
    dobj.Email = email
    dobj.IDproof = IDproof
    dobj.Gender = gender
    dobj.save()
    return JsonResponse({"status":"ok"})





def view_placess(request):
    data=[]
    try:
        dd=Place.objects.all()
        for i in dd:
            data.append({
                'place_id':i.place_id,
                'place_name':i.place_name,
                'city':i.city,
                'landmark':i.landmark,
                'state':i.state,
                'lati':i.lati,
                'longi':i.longi,
                'status':i.status,
            
            })
            if data:
                status="success"
            else:
                status="error"
            
    except:
        status='error'
        
    response = {
        
    'status': status,
        'data': data
    }

    return JsonResponse(response)

    
def send_rating(request):
    print("########################")
    data=[]
    review=request.POST.get("review")
    place_id=request.POST.get('place_id')
    ratingString=request.POST.get('ratingString')
    print("ratingString : ",ratingString)
    photo=request.FILES.get('image')
    fs = FileSystemStorage()
    f_nam =fs.save(photo.name, photo)
        
    
    
    try:
        obj=Review(review=review,rating=ratingString,date=timezone.now().date(),photo1=f_nam,place_id=place_id)
        obj.save()
        if obj:
            data['status']="success"
        else:
            data['status']="failed"
        
    except:
        status = "error"
        
    response = {
        
       'status': status,
        'data': data
    }
    
    return JsonResponse(response)

        

# def send_rating(request):
#     print("########################")
#     data = {}
#     review = request.POST.get("review")
#     place_id = request.POST.get('place_id')
#     photo = request.FILES.get('image')
#     fs = FileSystemStorage()
#     print("mmmmmmmmmmmmmmm",photo)
    
#     print(";;;;;;;;;;;;;;;;;")
#     f_nam = fs.save(photo.name, photo)
#     print("gggggggggggggg")
#     obj = Review(review=review, rating="hh", date='curdate()', photo1=f_nam, place_id=place_id)
#     obj.save()
#     print("////////////////////////")
#     if obj:
#         data['status'] = "success"
#         print("pppppppppppppppppppppp")
#     else:
#         data['status'] = "failed"
#         print(",,,,,,,,,,,,,,,,,,,,,,,,,,")

#     response = {
#         'data': data
#     }
    
#     return JsonResponse(response)

    
    

def view_noti(request):
    data=[]
    try:
        dd=Notification.objects.all()
        for i in dd:
            data.append({
                'noti_id':i.noti_id,
                'noti':i.notification,
                'date':i.date,
               
            
            })
            if data:
                status="success"
            else:
                status="error"
            
    except:
        status='error'
        
    response = {
        
    'status': status,
    'data': data
    }

    return JsonResponse(response)

  



def view_packages(request):
    data=[]
    try:
        dd=Package.objects.all()
        for i in dd:
            data.append({
                'package_id': i.package_id,
                'p_name': i.package_name,
                'details': i.description,
                'valid_from': i.valid_from,
                'valid_till': i.valid_till,
                'price': i.price,
               
            
            })
            if data:
                status="success"
            else:
                status="error"
            
    except:
        status='error'
        
    response = {
        
    'status': status,
    'data': data
    }

    return JsonResponse(response)

from django.db.models import F, FloatField, ExpressionWrapper, Func, Value
from django.db.models.functions import Cos, Sin, Radians

from django.db.models import Func, FloatField

class Acos(Func):
    function = 'ACOS'
    output_field = FloatField()
    
def user_near_by_facility(request):
    data = []
    
    lati = request.GET.get("lati")
    longi = request.GET.get("logi")
    
    print(lati,longi)
    
    if lati is None or longi is None:
        return JsonResponse({'status': 'error', 'message': 'Latitude or longitude not provided in the request.'})
    
    try:
        lati = float(lati)
        longi = float(longi)
        print("##########")
        facilities = Facility.objects.annotate(
            distance=ExpressionWrapper(
                Acos(
                    Cos(Radians(lati)) * Cos(Radians(F('lati'))) *
                    Cos(Radians(F('longi')) - Radians(longi)) +
                    Sin(Radians(lati)) * Sin(Radians(F('lati')))
                ) * Value(3959), 
                output_field=FloatField()
            )
        ).filter(distance__lte=30)  
        print("######",facilities)
        for facility in facilities:
            data.append({
                'facility_id': facility.facility_id,
                'type': facility.type,
                'f_name': facility.f_name,
                'f_place': facility.f_place,
                'city': facility.city,
                'state': facility.state,
                'phone': facility.phone, 
                'email': facility.email,
                'lati': facility.lati,
                'longi': facility.longi,
                
                'photo':str(facility.photo) if facility.photo else None
                
            })
            
        if data:
            status = 'success' 
        else:
            status = 'error' 

    except Exception as e:
        status = 'error'
        data = []
        
    response = {
        'status': status,
        'data': data
    }

    return JsonResponse(response, encoder=DjangoJSONEncoder)





   
def user_view_near_by_places(request):
    data = []
    
    lati = request.GET.get("lati")
    longi = request.GET.get("logi")
    
    print(lati,longi)
    
    if lati is None or longi is None:
        return JsonResponse({'status': 'error', 'message': 'Latitude or longitude not provided in the request.'})
    
    try:
        lati = float(lati)
        longi = float(longi)
        print("##########")
        obj = Place.objects.annotate(
            distance=ExpressionWrapper(
                Acos(
                    Cos(Radians(lati)) * Cos(Radians(F('lati'))) *
                    Cos(Radians(F('longi')) - Radians(longi)) +
                    Sin(Radians(lati)) * Sin(Radians(F('lati')))
                ) * Value(3959), 
                output_field=FloatField()
            )
        ).filter(distance__lte=30)  
        print("######",obj)
        for i in obj:
            data.append({
                'place_id': i.place_id,
                'p_name': i.place_name,
                'city': i.city,
                'state': i.state,
                'lmark': i.landmark, 
                'latitude': i.lati,
                'longitude': i.longi,
                
                
                
            })
            
        if data:
            status = 'success' 
        else:
            status = 'error' 

    except Exception as e:
        status = 'error'
        data = []
        
    response = {
        'status': status,
        'data': data
    }

    return JsonResponse(response)




def multi_file_upload(request):
    if request.method == 'POST':
        login_id = request.POST.get('log_id')
        print("login_id : ", login_id)
        
        file = request.FILES.get('file')
        path = "static/" + str(uuid.uuid4()) + file.name
        with open(path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        result_list = file.name.split('.')
        print(result_list[1])
        
        c_title = request.POST.get('title')
        user_post = Media(user_id=login_id, title=c_title, file_path=path, file_extension=result_list[1])
        user_post.save()
        
        data = {
            'status': 'success',
            'method': 'Multi_file_upload'
        }
        
        return JsonResponse(data)
    else:
        return render(request, 'upload_form.html')
    
    
    

def add_travelogue(request):
    data={}
    
    title=request.GET.get("title")
    desc=request.GET.get("desc")
    
    l_id=request.GET.get("login_id")
    
    obj=User.objects.get(login_id=l_id)
    u_id=obj.pk
    
    kk = Travelogue(travel_title=title,description=desc,user_id=u_id)
    kk.save()
    
    if kk:
        data['status']="success"
        
    else:
        data['status']="error"
           
    return JsonResponse(data)
  
    

        



def View_travelogue(request):
    data=[]
    lid=request.GET.get("login")
    obj=User.objects.get(login_id=lid)
    uid=obj.pk
    try:
        
        dd=Travelogue.objects.filter(user_id=uid)
        for i in dd:
            data.append({
                'id':i.travelogue_id,
                'Title':i.travel_title,
                'description':i.description,
               
            
            })
            if data:
                status="success"
            else:
                status="error"
            
    except:
        status='error'
        
    response = {
        
    'status': status,
    'data': data
    }

    return JsonResponse(response)

  
def user_view_facility(request):
    data = []
    try:
              
        facilities = Facility.objects.all()
        print("######",facilities)
        for facility in facilities:
            data.append({
                'facility_id': facility.facility_id,
                'type': facility.type,
                'f_name': facility.f_name,
                'f_place': facility.f_place,
                'city': facility.city,
                'state': facility.state,
                'phone': facility.phone, 
                'email': facility.email,
                'lati': facility.lati,
                'longi': facility.longi,
                
                'photo':str(facility.photo) if facility.photo else None
                
            })
            
        if data:
            status = 'success' 
        else:
            status = 'error' 

    except Exception as e:
        status = 'error'
        
        
    response = {
        'status': status,
        'data': data
    }

    return JsonResponse(response, encoder=DjangoJSONEncoder)



def Multi_file_upload(request):
    data=[]
    
    title=request.POST.get('title')
    plc_id=request.POST.get('plc_id')
    user_id=request.POST.get('log_id')
    desc=request.POST.get('desc')
    
    

    fileType=request.POST.get('fileType')
    photo=request.FILES.get('file')
    
    fs = FileSystemStorage()
    f_nam =fs.save(photo.name, photo)
        
 
    obj=Media(media_type=fileType,file=f_nam,title=title,description=desc,place_id=plc_id,travelogue_id=user_id)
    obj.save()
    
   
    if obj:
        status = "success"
    else:
        status = "error"
    
    response = {
        
       'status': status,
        'data': data,
        'method':"Multi_file_upload"
       
    }
    
    
    return JsonResponse(response)




def dropdwonviewplace(request):
    data=[]
    try:
        dd=Place.objects.all()
        for i in dd:
            data.append({
                'place_id':i.place_id,
                'place_name':i.place_name,
                
            
            })
            if data:
                status="success"
            else:
                status="error"
            
    except:
        status='error'
        
    response = {
        
    'status': status,
        'data': data,
        'method':"dropdwonviewplace"
    }

    return JsonResponse(response)


def searchvenue(request):
    s=request.POST["s"]

    p=Place.objects.filter(city__icontains=s)

    data=[]

    c=[]


    for i in p:

        if i.city not in c:
            c.append(i.city)
            data.append({
                'name':i.city
            })

    print(data)
    return JsonResponse(
        {
            'status':'ok',
            'data':data
        }
    )



def sendfeedback(request):
    lid= request.POST["lid"]
    feed= request.POST["feedback"]

    from datetime import  datetime

    f=Feedback()
    f.user=User.objects.get(LOGIN_id=lid)
    f.feedback=feed
    f.date=datetime.now()
    f.save()
    return JsonResponse(
        {
            'status':'ok'
        }
    )


def user_add_travel(request):
    lid=request.POST["lid"]
    title=request.POST["title"]
    description=request.POST["description"]

    from datetime import  datetime
    f=Travelogue()
    f.travel_title=title
    f.description= description
    f.user= User.objects.get(LOGIN_id=lid)
    f.date=datetime.now()
    f.save()

    return JsonResponse(
        {
            'status':'ok'
        }
    )

def user_view_traveogue(request):
    lid= request.POST["lid"]
    data=Travelogue.objects.filter(user__LOGIN_id=lid)

    li=[]

    for i in data:
        li.append(
            {
                'id':i.id,
                'title':i.travel_title,
                'description':i.description,
                'date':i.date
            }
        )

    return  JsonResponse(
        {
            'status':'ok',
            'data':li
        }
    )


def travel_delete(request):
    id= request.POST["id"]

    Travelogue.objects.filter(id=id).delete()

    return JsonResponse(
        {
            'status':'ok'
        }
    )



def getdistancebetweentwocord(la1,lo1,la2,lo2):
    from geopy.distance import geodesic
    newport_ri = (la1,lo1)
    cleveland_oh = (la2,lo2)
    s=geodesic(newport_ri, cleveland_oh).kilometers
    print("computed distance", la1,lo1,la2,lo2,s )
    return s


def getvenuebycategoryid(catid):
    # qry="SELECT `venue_id` FROM `venue` WHERE `category_id`='"+str(catid)+"'"
    # db=Db()
    res= Place.objects.filter(CATEGORY__id=catid)
    venueid = []
    for i in res:
        venueid.append(i.id)

    return venueid


def getnodeidbylevel(level):
    # qry="SELECT `nodeid` FROM `tree` WHERE `level`='"+str(level)+"'"
    # db = Db()
    # res = db.select(qry)
    res=tree.objects.filter(level=level)
    nodeid = []
    for i in res:
        nodeid.append(i.nodeid)

    return nodeid


def getfullpathofparentnodeid(nodeid):
    path=[]
    n=int(nodeid)
    # path.append(n)
    while n>0:


        parentnodeid=getparentnodeid(str(n))
        path.append(n)
        n=parentnodeid

    return path






def and_generateplanning(request):
    tree.objects.filter().delete()
    nodeid=1
    choices=request.POST["selected"]
    place=request.POST["place"]

    print(choices)

    print(place,"hoiiiiiiiiiiiiiiiiiiiii")

    from geopy.geocoders import Nominatim

    def get_coordinates(place_name):
        # Create a geolocator object using Nominatim API
        geolocator = Nominatim(user_agent="myGeocoder")

        # Geocode the place name to get location details
        location = geolocator.geocode(place_name)

        if location:
            # Return the latitude and longitude if found
            return location.latitude, location.longitude
        else:
            # If the place is not found, return None
            return None, None
    lat,long=get_coordinates(place)

    print(lat,long,"jishnu")


    #
    # lat=float(request.POST["latitude"])
    # #
    # print(lat)
    # long=float(request.form["longitude"])
    #request.form["longitude"]
    # print(long)

    print("lk1", lat,long)


    nodeid=1
    parentnodeid=0
    level=0


    choices=choices[0:-1]
    s= choices.split(",")

    while level < len(s):
        if nodeid==1:
          l= (s[0])
          l = getvenuebycategoryid(l)
          for j in l:
              # qry="SELECT `latitude`,`longitude` FROM `venue` WHERE `venue_id`='"+str(j)+"'"
              # resk= db.selectOne(qry)

              resk= Place.objects.get(id=j)

              lat2= float( resk.lati)
              lo2= float(resk.longi)
              dis=getdistancebetweentwocord(lat,long,lat2,lo2)

              if dis< 7000000000:
                  instreenode(nodeid, j,str(dis), parentnodeid, level)
                  nodeid = nodeid + 1
          level=level+1
        else :
            sm=getnodeidbylevel(level-1)
            for k in sm:
                n=s[level]
                v=getvenuebycategoryid(n)
                for l in v:

                    d1=tree.objects.get(nodeid=str(k))
                    resk= Place.objects.get(id=d1.venueid)

                    # db=Db()
                    # qry = "SELECT `latitude`,`longitude` FROM `venue` WHERE `venue_id` in (SELECT `venueid` FROM `tree` WHERE `nodeid`='"+str(k)+"')"
                    # print(qry)
                    #
                    # resk = db.selectOne(qry)

                    print(resk)
                    lat = float(resk.lati)
                    lo = float(resk.longi)
                    # qry = "SELECT `latitude`,`longitude` FROM `venue` WHERE `venue_id`='" + str(l) + "'"
                    # resk = db.selectOne(qry)


                    resk=Place.objects.get(id=str(l))
                    lat2 = float(resk.lati)
                    lo2 = float(resk.longi)
                    dis = getdistancebetweentwocord(lat, lo, lat2, lo2)

                    instreenode(nodeid,l,dis,k,level)
                    nodeid = nodeid + 1
            level=level+1


    s= getleafnodeidies()
    p=[]

    for i in s:
        b=getfullpathofparentnodeid(i)
        p.append(b)

    res=[]
    distlist = []
    for i in p:

        k=[]




        # still position lat long

        stilllat= float(lat)
        stilllongitude= float(long)

        dist=0.0
        for j in i:

            # qry=  "SELECT * FROM `venue` JOIN `tree` ON `tree`.`venueid`=`venue`.`venue_id` WHERE `tree`.`nodeid`='"+str(j)+"'"
            # db=Db()
            # resa=db.selectOne(qry)

            resa= tree.objects.get(nodeid=j)
            resa=Place.objects.get(id=resa.venueid)


            latitude= float(resa.lati)
            longitude= float(resa.longi)
            dist=dist+ getdistancebetweentwocord(stilllat,stilllongitude,latitude,longitude)
            stilllat= latitude
            stilllongitude=longitude

            k.append(resa)
        distlist.append(dist)
        print(dist,"distnace")
        sed=[]
        fg=[]
        for ms in range(len(k)-1,-1,-1):
            sed.append(k[ms])
            fg.append(
                {
                    'venue_name':k[ms].place_name,
                    'venue_details':k[ms].city,
                    'Address':k[ms].landmark,
                    'latitude':k[ms].lati,
                    'longitude':k[ms].longi

                }
            )



        res.append({'plan':fg })



    print("lengths")
    print(len(distlist),len(res))



    for ms in range(0,len(res)):

        for  ks in range(0, len(res)):

            if distlist[ms] < distlist[ks]:

                temp= res[ms]
                res[ms]= res[ks]
                res[ks]= temp

                temp = distlist[ms]
                distlist[ms] = distlist[ks]
                distlist[ks] = temp

    print(len(res),"---------------------------")
    print("hfddkgfjdhghdfkjhghdfhghdfhghkdjfhgkhdfhghdf dfhgjkhdfhghdfkh ghdfkh ghdfkhg hdkfhgh kjhdfhgk jhdfjhgjhd==========")
    print(res)



    print("Printing plans")

    for i in  range(0,len(distlist)):
        print( distlist[i],res[i])




    print(res,"========")
    return  JsonResponse({'status':'ok','data':res})


def user_view_notification(request):

    li=[]

    data=Notification.objects.all()

    for i in data:

        li.append(
            {
                'id':i.id,
                'notification':i.notification,
                'date':i.date,
            }
        )

    return  JsonResponse(
        {
            'status':'ok',
            'data':li
        }
    )



def user_view_facility(request):

    f=Facility.objects.all()

    li=[]

    for i in f:

        li.append(
            {
                'id': i.id,
                'type': i.type,
                'f_name': i.f_name,
                'f_place': i.f_place,
                'lati': i.lati,
                'longi': i.longi,
                'city': i.city,
                'state': i.state,
                'phone': i.phone,
                'email': i.email,
                'photo': i.photo,
            }
        )
    print(li)
    return JsonResponse(
        {
            'status':'ok',
            'data':li
        }
    )


def user_view_package(request):
    fid =request.POST["fid"]

    data= Package.objects.filter(facility_id=fid)
    li = []

    for i in data:
        li.append(
            {
                'id': i.id,
                'package_name': i.package_name,
                'description': i.description,
                'valid_from': i.valid_from,
                'valid_till': i.valid_till,
                'price': i.price,
            }
        )
    return JsonResponse(
        {
            'status': 'ok',
            'data': li
        }
    )


def viewcategory(request):
    data=category.objects.all()
    li=[]
    for i in data:
        li.append(
            {
                'id':i.id,
                'category_name':i.category,
            }
        )
    return  JsonResponse(
        {
            'status':'ok',
            'data':li
        }
    )



def user_send_review(request):
    pid= request.POST["pid"]
    review= request.POST["review"]
    rating= request.POST["rating"]
    photo1= request.POST["photo1"]

    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(photo1)
    fh = open(
        "C:\\Users\\computer\\Downloads\\smart travelogue(thelast)\\smart travelogue\\Smart_Travelogue\\static\\" + date + ".jpg",
        "wb")
    path = '/static/' + date + '.jpg'
    fh.write(a)
    fh.close()

    r=review()
    r.place_id=pid
    r.review= review
    r.rating= rating
    r.date= date
    r.photo1=path
    r.save()


    from textblob import TextBlob
    data=TextBlob(review)
    # Create a TextBlob object
    blob = TextBlob(review)
    sentiment = blob.sentiment

    if sentiment ==0:

        p=Place.objects.get(id=pid)
        p.neu= p.neu+1
        p.save()

    if sentiment > 0:
        p = Place.objects.get(id=pid)
        p.neu = p.pos + 1
        p.save()

    if sentiment < 0:
        p = Place.objects.get(id=pid)
        p.neg = p.neg + 1
        p.save()


    return  JsonResponse(
        {
            'status':'ok'
        }
    )


def user_add_media(request):

    place= request.POST["place"]
    # media_type= request.POST["media_type"]
    file= request.POST["file"]
    title= request.POST["title"]
    description= request.POST["description"]
    travelogueid= request.POST["travelogueid"]

    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(file)
    fh = open(
        "C:\\Users\\computer\\Downloads\\smart travelogue(thelast)\\smart travelogue\\Smart_Travelogue\\static\\" + date + ".jpg",
        "wb")
    path = '/static/' + date + '.jpg'
    fh.write(a)
    fh.close()





    m=Media()
    m.place=place
    m.media_type="img"
    m.title=title
    m.file=path
    m.description=description
    m.travelogue_id=travelogueid
    m.save()

    return  JsonResponse(
        {
            'status':'ok'
        }
    )



def viewmedia(request):
    tlid= request.POST["tlid"]

    m=Media.objects.filter(travelogue_id=tlid)
    li=[]

    for i in m:
        li.append(
            {
                'id':i.id,
                'place':i.place,
                'file':i.file,
                'title':i.title,
                'description':i.description,

            }
        )

    return JsonResponse(
        {
            'status':'ok',
            'data':li
        }
    )


def admin_add_category(request):

    data= category.objects.all()


    if request.method=="POST":
        plc_name=request.POST["plc_name"]

        c=category()
        c.category=plc_name
        c.save()

        return HttpResponse(
            "<script>alert('Category added successfully');window.location='/admin_add_category'</script>"
        )



    return render(request,"admin_add_category.html",{'data':data})


def admin_delete_category(request,id):

    category.objects.filter(id=id).delete()

    return HttpResponse(
        "<script>alert('Category added successfully');window.location='/admin_add_category'</script>"
    )



def user_view_places(request):

    data=Place.objects.all()

    li=[]

    for i in data:

        li.append(
            {
                'id':i.id,
                'place_name':i.place_name,
                'city':i.city,
                'landmark':i.landmark,
                'state':i.state,
                'lati':i.lati,
                'longi':i.longi,
                'cat':i.CATEGORY.category

            }
        )

    return  JsonResponse(
        {
            'status':'ok',
            'data':li
        }
    )


def sindex(request):
    return render(request,"sindex.html")