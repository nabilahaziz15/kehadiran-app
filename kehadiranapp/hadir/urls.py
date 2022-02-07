from django.urls import path
from . import views
from kehadiranapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

#DataFlair Django Tutorials
urlpatterns = [
	path('', views.index, name = 'index'),
	path('upload/', views.upload, name = 'upload-hadir'),
	path('update/<int:hadir_id>', views.update_hadir),
	path('delete/<int:hadir_id>', views.delete_hadir),
	# path('api-auth/', include('rest_framework.urls')),
	path('', views.index, name='index')

]

#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)


'''x-html has doctype manadatory while html doesn't require you to declare doctype
xmlns type is mandatory in html
html, head, body and title is mandatory
must be properly nested
must be properly closed
must be used in lowercase
'''

	# path('vo',views.upload_form),
	# path('',views.listkehadiran,name='upload_form'),