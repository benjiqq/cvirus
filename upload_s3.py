import logging
import boto3
from botocore.exceptions import ClientError

opencovid_bucket = "opencovid"
s3 = boto3.client('s3')
s3_client = boto3.client('s3')

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL':'public-read'})
    except ClientError as e:
        logging.error(e)
        return False
    return True

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True



def list_buckets():
    response = s3.list_buckets()
    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        #print(f'  {bucket["Name"]}')
        print(f'  {bucket}')


#url = '{}/{}/{}'.format(s3.meta.endpoint_url, opencovid_bucket, "worldometer_country_2020-03-20.csv")
#print (url)

for key in s3_client.list_objects(Bucket=opencovid_bucket)['Contents']:
    print(key)

#upload_file(fn, "opencovid")

fn = "./data_sources/worldometer/worldometer_country_2020-03-20.csv"
#upload_file(fn, opencovid_bucket, "worldometer_country_2020-03-20.csv")

#create_bucket("opencovid")
