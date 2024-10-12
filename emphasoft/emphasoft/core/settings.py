import socket
if socket.gethostname() == 'albert-VirtualBox':
    from emphasoft.core.local_settings import *
else:
    from emphasoft.core.production_settings import *
print(STATIC_ROOT)
print(STATIC_URL)
