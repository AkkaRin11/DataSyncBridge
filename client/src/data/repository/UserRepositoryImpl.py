from typing import Union

from data.remote.firebase.FirebaseDao import FirebaseDao
from domain.model.User import User
from domain.repository.UserRepository import UserRepository


class UserRepositoryImpl(UserRepository):
    __instance = None
    __dao: FirebaseDao = None

    @classmethod
    def initialize(cls, dao: FirebaseDao):
        cls.__dao = dao

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = UserRepositoryImpl()
        return cls.__instance

    def delete_user_file_node(self, user_id, node):
        self.__dao.delete_user_file_node(user_id, node)

    def get_user_by_id(self, user_id: Union[int, str]) -> User:
        user = self.__dao.get_user(user_id)
        return User.from_dto(
            user
        ) if user is not None else None
