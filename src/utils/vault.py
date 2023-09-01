import logging
import os

import boto3
import botocore
import hvac
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)


class Vault:
    def __init__(self, role: str, hvac_path: str, url: str):
        self.role = role
        self.hvac_path = hvac_path
        self.url = url

    def _get_boto3_session(self) -> boto3.session.Session:
        """Get boto3 session
        Parameters
        ----------
        Returns:
        -------
            session: boto3.session.Session
                The boto3 session.
        """
        logger.info("Getting boto3 session")
        session = boto3.session.Session()
        return session

    def _get_client(
        self,
        credentials: botocore.credentials.Credentials,
    ) -> hvac.Client:
        """Get hvac client
        Parameters
        ----------
            credentials: botocore.credentials.Credentials:
                The credentials.
            url: str
                The url.
        Returns:
        -------
            client: hvac.Client
                The hvac client.
        """
        logger.info("Getting hvac client")
        client = hvac.Client(self.url, verify=False)
        client.auth.aws.iam_login(
            access_key=credentials.access_key,
            secret_key=credentials.secret_key,
            session_token=credentials.token,
            role=self.role,
        )
        if not client.is_authenticated():
            logger.error("Vault authentication failed")
            raise Exception("Vault authentication failed")
        return client

    def _parse_secrets(
        self,
        client: hvac.Client,
        secrets_dict_key: str,
    ) -> str:
        """Parse secrets
        Parameters
        ----------
            client: hvac.Client:
                The hvac client.
            secrets_dict_key: str
                The secrets dict key.
        Returns:
        -------
            secrets: str
                The secrets.

        """
        logger.info("Parsing secrets")
        response = client.secrets.kv.v2.read_secret_version(
            path=self.hvac_path,
        )

        data = response["data"]["data"]
        if secrets_dict_key in data:
            secrets = data.get(secrets_dict_key)

            if not secrets:
                logger.error("No secrets found")
                raise Exception("No secrets found")

            logger.info("Secrets found")

        else:
            logger.error("No secrets found")
            raise Exception("No secrets found")

        return secrets

    def get_secret(self, secrets_dict_key: str) -> str:
        """Get secrets
        Parameters
        ----------
            secrets_dict_key: str
                The secrets dict key.
        Returns:
        -------
            secret: str
                The secret.

        """
        logger.info("Getting secrets")
        session = self._get_boto3_session()
        credentials = session.get_credentials()
        client = self._get_client(credentials)
        secrets = self._parse_secrets(client, secrets_dict_key)
        return secrets
