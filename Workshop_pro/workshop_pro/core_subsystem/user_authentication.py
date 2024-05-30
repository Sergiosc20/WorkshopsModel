"""
This module has some classes related to users and authentication.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

import json


class User:
    """This is a data class to represent User information."""

    def __init__(self, username: str, grants: dict):
        """
        Initializes a User object.

        Args:
            username (str): The username of the user.
            grants (dict): Dictionary of user's grants.
        """
        self.__username = username
        self.__grants = grants

    def get_username(self):
        """
        Returns the username of the user.
        """
        return self.__username

    def is_grant(self, grant: str):
        """
        Checks if the user has a specific grant.

        Args:
            grant (str): The grant to check.

        Returns:
            bool: True if the user has the grant, False otherwise.
        """
        if  self.__grants[grant]:
            return True
        return False

class Authentication:
    """This class is used to validate user authentication."""

    def __init__(self, username: str, password: str):
        """
        Initializes Authentication object with username and password.

        Args:
            username (str): The username.
            password (str): The password.
        """
        self.__username = username
        self.__password = password
        self.__grants = None

    def authenticate(self) -> bool:
        """
        Validates user credentials.

        Returns:
            bool: True if authentication succeeds, False otherwise.
        """
        with open("E:/workshop_pro/workshop_pro/core_subsystem/users.json", "r", encoding="UTF-8") as file:
            users = json.load(file)

        for user in users:
            if (
                user["username"] == self.__username
                and user["password"] == self.__password
            ):
                self.__grants = user["grants"]
                return True
        return False

    def userdata(self) -> User:
        """
        Retrieves user data.

        Returns:
            User: The User object.
        """
        return User(self.__username, self.__grants)

    def register(self, new_username: str, new_password: str) -> bool:
        """
        Registers new users.

        Args:
            new_username (str): The username of the new user.
            new_password (str): The password of the new user.

        Returns:
            bool: True if registration succeeds, False otherwise.
        """
        with open("E:/workshop_pro/workshop_pro/core_subsystem/users.json", "r", encoding="UTF-8") as file:
            users = json.load(file)
        for user in users:
            if user["username"] == new_username:
                return False  # Username already exists
        default_grants = {
            "add_vehicle": False,
            "remove_vehicle": False,
            "search_vehicle": True
        }

        new_user = {
            "username": new_username,
            "password": new_password,
            "grants": default_grants
        }
        users.append(new_user)
        with open("E:/workshop_pro/workshop_pro/core_subsystem/users.json", "w", encoding="UTF-8") as file:
            json.dump(users, file, ensure_ascii=False, indent=4)
        return True
