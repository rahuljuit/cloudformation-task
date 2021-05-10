import DeployStack
import s3Operations
import zipconverter
from ClientClass import obj1

s3_client = obj1.s3_client

bucket1 = 'bucketwith-code'
loc = 'ap-south-1'
zip_file_name = 'lambda_function2.zip'
code_file = 'lambda_function.py'
stack_name = 'mys3infra'
template = 'Infrastructure.yaml'
filename = 'test.txt'
src_bucket = 'task1-input-bucket'

# res1 = s3Operations.create_s3_bucket(bucket1, loc)
# print(res1)
# print("Code Bucket Created")

res2 = zipconverter.zip_file_maker(zip_file_name, code_file)
print(res2)
print("ZipFile Created")

# waiter = s3_client.get_waiter('bucket_exists')
# waiter.wait(Bucket=bucket1)
# s3Operations.upload_zip_files(bucket1)
# print("Zip File Uploaded")

# res3 = DeployStack.create_template_stack(stack_name)
# print(res3)
# print("Stack Got Created")
#
# waiter = s3_client.get_waiter('bucket_exists')
# waiter.wait(Bucket=src_bucket)
# res4 = s3Operations.put_object_in_s3_bucket('C:/Users/Rahul/PycharmProjects/boto3demo/Ques_2/test.txt', src_bucket)
# print("Object added to the source bucket")
