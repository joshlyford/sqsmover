# sqsmover
Python Boto3 Amazon (AWS) SQS  Message Mover

```console
❯ ./sqsmover.py -h
usage: sqsmover.py [-h] [-w WRK] -s SRC -d DST [--region REGION]

Migrate messages from SQS queues.

optional arguments:
  -h, --help         show this help message and exit
  -w WRK, --wrk WRK  Number of workers to start. (default: 10)
  -s SRC, --src SRC  Name of the source queue.
  -d DST, --dst DST  Name of the destination queue.
  --region REGION    The AWS region of the queues (default: 'us-east-1').
```