#!/usr/bin/env python3


import boto3
import argparse
import multiprocessing


def worker(num, profile, region, src, dst):
    print('Worker Starting', num)
    aws_region = region
    src_queue_name = src
    dst_queue_name = dst

    print('Connecting to SQS...')
    print('Source ' + src_queue_name)
    print('Destination ' + dst_queue_name)
    session = boto3.Session(profile_name=str(profile), region_name=aws_region)
    client = session.client('sqs')

    print('Connected to SQS')

    src_queue = client.get_queue_url(QueueName=src_queue_name)['QueueUrl']
    dst_queue = client.get_queue_url(QueueName=dst_queue_name)['QueueUrl']

    print('Source URL ' + src_queue)
    print('Destination URL ' + dst_queue)

    while True:
        messages = client.receive_message(QueueUrl=src_queue, MaxNumberOfMessages=10)
        if 'Messages' in messages:
            for src_message in messages['Messages']:
                print(str(num) + ': Processing message ' + src_message['MessageId'])
                msg_body = src_message['Body']
                client.send_message(QueueUrl=dst_queue, MessageBody=msg_body)
                client.delete_message(QueueUrl=src_queue, ReceiptHandle=src_message['ReceiptHandle'])
            if len(messages) <= 0:
                break
        else:
            print('Queue is now empty')
            break


if __name__ == '__main__':
    jobs = []
    parser = argparse.ArgumentParser(description="Migrate messages from SQS queues.")
    parser.add_argument('-s', '--src', required=True,
                        help='Name of the source queue.')
    parser.add_argument('-d', '--dst', required=True,
                        help='Name of the destination queue.')
    parser.add_argument('-w', '--wrk', default=10,
                        help='Number of workers to start (default: 10).')
    parser.add_argument('-p', '--prf', default='default',
                        help='AWS Credentials Profile to run as (default: default).')
    parser.add_argument('--region', default='us-east-1',
                        help='The AWS region of the queues (default: \'us-east-1\').')
    args = parser.parse_args()
    print('Starting ' + str(args.wrk) + ' workers ')
    print('Using ' + str(args.prf) + ' profile from .aws/credentials file')
    for i in range(int(args.wrk)):
        p = multiprocessing.Process(target=worker,args=(i, args.prf, args.region, args.src, args.dst))
        jobs.append(p)
        p.start()


