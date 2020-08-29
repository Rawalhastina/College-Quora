from django.urls import path , include

urlpatterns = [
    path('college/', include('webapp.urls')),
    path('faculty/', include('facultyapp.urls')),
    path('student/', include('studentapp.urls')),
]
