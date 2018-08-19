import time
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Prepara memo para: Empleado: juan Perez - Fecha de Designacion: 08-20-2018",
                   "Python is 10 seconds awsm!",
                   icon_path="custom.ico",
                   duration=20)

toaster.show_toast("Example two",
                   "This notification is in it's own thread!",
                   icon_path=None,
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)