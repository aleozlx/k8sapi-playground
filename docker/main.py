# pylint: disable=import-error,no-name-in-module
from kubernetes import client, config
import time
import sys
print("Hello")
config.load_incluster_config()

print("Listing pods with their IPs:")
v1 = client.CoreV1Api()
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

while 1:
    print('.')
    # sys.stdout.flush()
    time.sleep(3)
