import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()
<<<<<<< HEAD
=======

from whitenoise import WhiteNoise

application = WhiteNoise(application)
>>>>>>> 2aa59cd686b20bd9b1ab5b8b7dda1a956fc18380
