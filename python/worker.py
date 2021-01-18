from PIL import Image
import boto3
import os
import tempfile
import time

try:
    # Python 3
    import urllib.parse as urlparse
except:
    # Python 2.7.
    import urlparse


def main():
    sqs = boto3.client('sqs', endpoint_url='http://localhost:3460')
    s3 = boto3.client('s3', endpoint_url='http://localhost:3450')
    queue_url = "https://sqs.us-east-1.amazonaws.com/049920107807/queue-l-f-z"
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=30,
            WaitTimeSeconds=5
        )
        
        print(response)
        if 'Messages' not in response:
            continue
        message = response['Messages'][0]
        print(message['Body'])
        receipt_handle = message['ReceiptHandle']
        s3_url_parse = urlparse.urlparse(message['Body'])

        fd, path = tempfile.mkstemp()
        target_fd, target_path = tempfile.mkstemp(suffix=".jpg")
        try:
            with os.fdopen(fd, 'wb') as tmp:
                s3.download_fileobj(s3_url_parse.netloc, s3_url_parse.path[1:], tmp)
            img = Image.open(path)
            rgb_im = img.convert('RGB')
            rgb_im.save(target_path, quality=100)
            s3.upload_file(target_path, s3_url_parse.netloc, s3_url_parse.path[1:].replace(".png", ".jpg"))
        finally:
            os.remove(path)
            os.remove(target_path)
        
        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )


if __name__ == "__main__":
    main()
