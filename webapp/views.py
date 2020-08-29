from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.conf import settings

def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')

def loginpage(request):
    if request.method == "GET":
        regmsg = ""
        loginmsg=""
        evalue = request.GET.get('e')
        if evalue=="1":
            regmsg = "Register Done !"
        if evalue=="0":
            regmsg = "Register Not Done !"
        if evalue=="2":
            loginmsg = "Invalid User !"            
        return render(request,'login.html',{"regmsg":regmsg,"loginmsg":loginmsg}) 
    else:
        mail = request.POST.get('email')
        pwd = request.POST.get('pwd')       

        query = "select * from user where email='{0}' and password='{1}'".format(mail,pwd)

        try:
            cnn = settings.DBCONNECTION()
            cr = cnn.cursor()
            cr.execute(query)
            
            record = cr.fetchone() # single tuple
            if record is None:
                return redirect('/college/login?e=2')
            else:     
                type = record[4]           
                if type==1:
                    # /faculty/home
                    return redirect('/faculty/home')
                else:
                    # /student/home
                    return redirect('/student/home')
                    
        except Exception as ex:
            return HttpResponse("Login Failed !") 
        finally:
            cnn.close()

def register(request):
    name = request.POST.get('unm')       
    mail = request.POST.get('email')
    pwd = request.POST.get('pwd')
    type = request.POST.get('type')
    branch = request.POST.get('branch')

    query = "insert into user(username,email,password,type,branch) value('{0}','{1}','{2}',{3},{4})".format(name,mail,pwd,type,branch)

    try:
        cnn = settings.DBCONNECTION()
        cr = cnn.cursor()
        cr.execute(query)
        cnn.commit()
        return redirect('/college/login?e=1')
    except Exception as ex:
        return redirect('/college/login?e=0')  
    finally:
        cnn.close()
    