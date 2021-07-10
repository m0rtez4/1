import datetime
from kavenegar import *
from MrBambo.settings import Kavenegar_API
from random import randint
from . import models

def send_otp(mobile,otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
            'sender': '1000596446',  # optional
            'receptor': mobile,  # multiple mobile number, split by comma
            'message': 'your otp : {} '.format(otp),
        }
        response = api.sms_send(params)
        print('OTP : ', otp)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(1000,9999)

def check_otp_expiration(mobile):
    try :
        user = models.MyUser.objects.get(mobile=mobile)
        now = datetime.datetime.now()
        otp_time = user.otp_create_time
        diff_time = now - otp_time
        print('otp_time :',diff_time)

        if diff_time.seconds > 120 :
            return False
        return True

    except models.MyUser.DoesNotExist :
        return False