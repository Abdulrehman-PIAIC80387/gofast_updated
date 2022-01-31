#!/kunden/homepages/9/d891743934/htdocs/env/bin/python3

import os
import sys
import traceback

home = '/kunden/homepages/9/d891743934/htdocs/'
try:
    os.environ['VIRTUAL_ENV'] = os.path.join(home, 'env/bin')
    os.environ['PATH'] = os.environ['VIRTUAL_ENV'] + ':' + os.environ['PATH']

    project = os.path.join(home, 'gofast_project')
    # Add a custom Python path.
    sys.path.insert(0, project)

    # Switch to the directory of your project.
    os.chdir(project)

    # Set the DJANGO_SETTINGS_MODULE environment variable.
    os.environ['DJANGO_SETTINGS_MODULE'] = "gofast_project.settings"

    from django_fastcgi.servers.fastcgi import runfastcgi
    from django.core.servers.basehttp import get_internal_wsgi_application

    wsgi_application = get_internal_wsgi_application()
    runfastcgi(wsgi_application, method="prefork", daemonize="false", minspare=1, maxspare=1, maxchildren=1)
except:
    with open(os.path.join(home, 'tmp/error.log'), 'w') as fp:
        traceback.print_exc(file = fp)
