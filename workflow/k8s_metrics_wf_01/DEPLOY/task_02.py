from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order

context = Variables.task_call()

'''
deploy app
'''

ret = MSA_API.process_content('ENDED', f'App Deployed on DEVICE ID {context["metrics"]}', context, True)
print(ret)
