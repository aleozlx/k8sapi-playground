# pylint: disable=import-error,no-name-in-module
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import yaml
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

job_spec = client.V1JobSpec(
    template=client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(name='test_job'),
        spec=client.V1PodSpec(
            containers=[
                client.V1Container(
                    name='test',
                    image='busybox',
                    command=['hostname']
                )
            ],
            restart_policy='Never'
        )
    )
)

print(job_spec)

# https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Job.md
try:
    # jobApi.create_namespaced_job(namespace, client.V1Job(
    #     metadata=client.V1ObjectMeta(generate_name='test-job-'),
    #     spec=job_spec
    # ), pretty='true')

    jobApi.create_namespaced_job(namespace, body=yaml.safe_load("""---
apiVersion: batch/v1
kind: Job
metadata:
  generateName: test-job-
spec:
  template:
    metadata:
      name: test_job
    spec:
      containers:
        - name: test
          image: busybox
          command: ["hostname"]
      restartPolicy: Never
"""), pretty='true')
except ApiException as e:
    print('ApiException:', e.reason)
    print(e.body)

while 1:
    print('.')
    # sys.stdout.flush()
    time.sleep(3)

