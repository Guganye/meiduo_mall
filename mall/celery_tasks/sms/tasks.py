from ronglian_sms_sdk import SmsSDK
from celery_tasks.main import app

@app.task
def celery_send_sms_code(mobile, sms_code):
    sdk = SmsSDK(accId='2c94811c9860a9c4019888893e0d07c3', \
                 accToken='0f251435c33e41fba0de98d07fd09620', \
                 appId='2c94811c9860a9c4019888893fcf07ca')
    sdk.sendMessage(tid='1', mobile=mobile, datas=(sms_code, '5'))
