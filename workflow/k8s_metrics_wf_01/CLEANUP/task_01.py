import json
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order

dev_var = Variables()
context = Variables.task_call()

device_id_list = context["device_id_list"]

for device in device_id_list.values():
    order = Order(device)
    order.command_objects_instances('k8s_pods')
    ms_instances = json.loads(order.content.decode())
    for instance in ms_instances:
        Order(device).command_execute('DELETE', {'k8s_pods': instance})

ret = MSA_API.process_content('ENDED', f'workflow deleted, pods cleared', context, True)
print(ret)
