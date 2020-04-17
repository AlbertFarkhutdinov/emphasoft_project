import socket
if socket.gethostname() == 'albert-VirtualBox':
    from emphasoft_project.local_settings import *
    print(SECURE_SSL_REDIRECT)
else:
    from emphasoft_project.production_settings import *
    print(SECURE_SSL_REDIRECT)
