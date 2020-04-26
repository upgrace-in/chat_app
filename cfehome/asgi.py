import os
import django
from channels.routing import get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_sockets.settings')
django.setup()
application = get_default_application()
