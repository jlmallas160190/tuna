import json
import logging
import os

import boto3
import environ
from botocore.exceptions import ClientError

env = environ.Env(
    USE_SECRET_MANAGER=(bool, False),
    COMMON_SECRET_VAULT=(str, ""),
    DB_SECRET_VAULT=(str, ""),
)


def _get_sensitive_value_from_secret_manager(secret_vault_name, value_name):
    client = boto3.client("secretsmanager")
    try:
        response = client.get_secret_value(SecretId=secret_vault_name)
    except ClientError as e:
        logging.error("Sensitive Settings Error: ", e)
        raise e
    else:
        secret_vault = json.loads(response["SecretString"])
        return secret_vault[value_name]


def get_common_sensitive_value(value_name):
    use_secret_manager = env("USE_SECRET_MANAGER")
    if use_secret_manager:
        return _get_sensitive_value_from_secret_manager(
            secret_vault_name=env("COMMON_SECRET_VAULT"), value_name=value_name
        )
    return os.getenv(value_name)


def get_db_sensitive_value(secret_key, env_key):
    use_secret_manager = env("USE_SECRET_MANAGER", False)
    if use_secret_manager:
        return _get_sensitive_value_from_secret_manager(
            secret_vault_name=env("DB_SECRET_VAULT"), value_name=secret_key
        )
    return os.getenv(env_key)
