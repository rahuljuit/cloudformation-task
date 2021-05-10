from ClientClass import obj1
from botocore.exceptions import ClientError
from botocore.exceptions import ParamValidationError

cf_client = obj1.cf_client


def parse_template(template):
    with open(template) as template_file_obj:
        template_body = template_file_obj.read()
    try:
        cf_client.validate_template(TemplateBody=template_body)
        return template_body
    except ClientError as error:
        print(error)


def create_template_stack(stack_name):
    try:
        cf_client.create_stack(
            StackName=stack_name,
            TemplateBody=parse_template('C:/Users/Rahul/PycharmProjects/boto3demo/Ques_2/Infrastructure.yaml'),
            Capabilities=[
                'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM'
            ]
        )
        waiter = cf_client.get_waiter('stack_create_complete')
        waiter.wait(StackName=stack_name)
    except ClientError as error:
        if error.response['Error']['Code'] == 'AlreadyExistsException':
            try:
                cf_client.update_stack(
                    StackName=stack_name,
                    TemplateBody=parse_template('C:/Users/Rahul/PycharmProjects/boto3demo/Ques_2/Infrastructure.yaml'),
                    Capabilities=[
                        'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM'
                    ])
                waiter = cf_client.get_waiter('stack_create_complete')
                waiter.wait(StackName=stack_name)
            except ClientError as error:
                print('Unable to Update Stack', error)

    except ParamValidationError as error:
        print('Error in template', error)

    return '{0} successfully got created '.format(stack_name)
