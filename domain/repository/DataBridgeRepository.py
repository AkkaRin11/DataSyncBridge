from botocore.client import BaseClient
from pyrebase.pyrebase import Firebase

from data.S3Api import S3Api
from data.StorageFileDao import StorageFileDao


class DataBridgeRepository:
    __instance = None
    __dao: StorageFileDao = None
    __s3_api: S3Api = None

    @classmethod
    def initialize(cls, firebase: Firebase, s3_client: BaseClient, s3_main_bucket: str):
        cls.__dao = StorageFileDao(firebase)
        cls.__s3_api = S3Api(s3_client, s3_main_bucket)
        cls.__instance = DataBridgeRepository()

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = DataBridgeRepository()
        return cls.__instance

    def save_file(self, file_name: str, user_id):
        self.__s3_api.s3_upload_file(file_name)
