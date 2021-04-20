import os
from Ques_2.ClientClass import obj1

s3_client = obj1.s3_client


def create_s3_bucket(bucket1, loc):

    response = s3_client.create_bucket(
        ACL='private',
        Bucket=bucket1,
        CreateBucketConfiguration={
             'LocationConstraint': loc
        }
    )

    return response


def upload_zip_files(bucket1):
    for file in os.listdir():
        if '.zip' in file:
            upload_to_bucket = bucket1
            upload_to_bucket_dir = str(file)
            s3_client.upload_file(file, upload_to_bucket, upload_to_bucket_dir)


def put_object_in_s3_bucket(filename, bucket1):
    f = open(filename, "r")
    data = f.read()
    print(data)

    response3 = s3_client.put_object(
        ACL='private',
        Body=data,
        Bucket=bucket1,
        Key=filename,
    )

    return response3
