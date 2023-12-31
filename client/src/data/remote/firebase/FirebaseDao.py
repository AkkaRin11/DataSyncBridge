from typing import Union

from pyrebase.pyrebase import Firebase


class FirebaseDao:

    def __init__(self, firebase: Firebase):
        self.__db = firebase.database()

    def get_user(self, user_id: Union[str, int]) -> dict:
        return self.__db.child('users').child(user_id).get().val()

    def delete_user_file_node(self, user_id, node):
        self.__db.child('users').child(user_id).child('photo').child(node).remove()
