from django.shortcuts import render
from django.conf import settings

def home(request):
    students = []
    try:
        cnn = settings.DBCONNECTION()
        cr = cnn.cursor()
        cr.execute("select username ,email from user where type=2")
        students = cr.fetchall()
    except Exception as ex:
        print(ex)
    return render(request,'facultyhome.html',{"students":students})
