from plyer import notification


def send_notification():
    notification.notify(
        
        title="My List",
        message="HELLO BUDDY!!!",
        app_icon="notification_bell.ico",
        app_name="Notifier",
        timeout=10
        
    )
#main function 
send_notification()
