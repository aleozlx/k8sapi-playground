# pylint: disable=import-error,no-name-in-module
from kubernetes import client, config
import time
import sys
print("Hello")
config.load_incluster_config()

namespace = 'bluecheese'
# v1 = client.CoreV1Api()
jobApi = client.BatchV1Api()
# ret = v1.list_namespaced_pod('celery-jobq', watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
job = client.V1Job()
jobApi.create_namespaced_job(namespace, job)

while 1:
    print('.')
    # sys.stdout.flush()
    time.sleep(3)

