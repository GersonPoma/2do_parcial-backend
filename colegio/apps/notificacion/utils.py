from pyfcm import FCMNotification
from django.conf import settings

#push_service = FCMNotification(api_key=settings.FCM_SERVER_KEY)

def enviar_notificacion_push(tokens, titulo, mensaje, data=None):
    if not tokens:
        return None

    result = push_service.notify_multiple_devices(
        registration_ids=list(tokens),
        message_title=titulo,
        message_body=mensaje,
        data_message=data or {},
    )

    return result
