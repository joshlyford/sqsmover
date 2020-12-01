# sqsmover
Python Boto3 Amazon (AWS) SQS  Message Mover

```console
❯ ./sqsmover.py -h
usage: sqsmover.py [-h] -s SRC -d DST [-w WRK] [-p PRF] [--region REGION]

Migrate messages from SQS queues.

optional arguments:
  -h, --help         show this help message and exit
  -s SRC, --src SRC  Name of the source queue.
  -d DST, --dst DST  Name of the destination queue.
  -w WRK, --wrk WRK  Number of workers to start (default: 10).
  -p PRF, --prf PRF  AWS Credentials Profile to run as (default: default).
  --region REGION    The AWS region of the queues (default: 'us-east-1').
```


```console
./sqsmover.py -s sqs-dead-letter-queue-name -d sqs-worker-queue -w 5 -p alternateprofile
```