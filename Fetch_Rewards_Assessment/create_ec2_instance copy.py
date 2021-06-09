# create EC2 instance
import boto3


def create_ec2_instance(ec2):
    try:
        print("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        response = resource_ec2.run_instances(
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/xvda',
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'VolumeSize': 10,
                        'VolumeType': 'standard'
                    },
                    'DeviceName': '/dev/xvdf',
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'VolumeSize': 100,
                        'VolumeType': 'standard'
                    },


                },
            ],
            ImageId='ami-0d5eff06f840b45e9',
            InstanceType='t2.micro',
            KeyName='Your Access key here',
            MaxCount=1,
            MinCount=1,

        )

    except Exception as e:
        print(e)


create_ec2_instance('ec2')


def create_iam_users():
    try:
        print("Creating IAM users")
        iam = boto3.client("iam")
        response = iam.create_user(UserName="user-1")
        response = iam.create_user(UserName="user-2")
    except Exception as p:
        print(p)


create_iam_users()
