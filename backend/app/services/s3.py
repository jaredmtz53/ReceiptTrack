import logging
import uuid

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
from fastapi import UploadFile

from app.config.settings import settings

s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_DEFAULT_REGION,
    config=Config(
        signature_version="s3v4",
        s3={"addressing_style": "virtual"}
    )
)


def upload_receipt_image(file: UploadFile):

    object_key = f"receipts/{uuid.uuid4()}-{file.filename}"

    try:
        s3_client.upload_fileobj(
            file.file,
            settings.AWS_S3_BUCKET,
            object_key,
            ExtraArgs={
                "ContentType": file.content_type
            }
        )
        return object_key

    except ClientError as e:
        logging.error(e)
        raise e


def generate_receipt_image_url(object_key: str, expiration: int = 3600):
    return s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": settings.AWS_S3_BUCKET,
            "Key": object_key,
        },
        ExpiresIn=expiration
    )