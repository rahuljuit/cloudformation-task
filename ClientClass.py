import boto3


class AWSClients:

    def __init__(self):
        self.session_var = boto3.session.Session(profile_name='s3_developer')
        self.s3_client = self.session_var.client('s3')
        self.cf_client = self.session_var.client('cloudformation')


obj1 = AWSClients()
