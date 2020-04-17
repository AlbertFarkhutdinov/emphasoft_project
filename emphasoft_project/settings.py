import socket
if socket.gethostname() == 'albert-VirtualBox':
    from emphasoft_project.local_settings import *
    print(STATIC_ROOT)
    print(STATIC_URL)
else:
    from emphasoft_project.production_settings import *
    print(STATIC_ROOT)
    print(STATIC_URL)
