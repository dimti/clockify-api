from typing import List
from clockify.model.user_model import User, UserGetParams, MemberProfile, MemberProfileGetParams
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper

class UserApi(Wrapper):
    def get_users(
        self, workspace_id: str, params: UserGetParams = UserGetParams()
    ) -> List[User]:
        """Return list of User objects.

        Args:
            workspace_id (str): ID of the clockify workspace.
            params (UserGetParams, optional): Path parameters. Defaults to UserGetParams().

        Returns:
            List[User]: List of User Objects
        """
        url = self.__url(workspace_id)
        return self._get_list(url, User, params)

    def get_member_profile(
        self, workspace_id: str, user_id: str
    ) -> MemberProfile:
        """Return one MemberProfile object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            user_id (str): ID of the clockify user.

        Returns:
            MemberProfile: MemberProfile object.
        """
        url = self.__url(workspace_id, user_id, True)
        return self._get_one(url, MemberProfile)

    # TODO: This api method is not allowed for free accounts and need be testing on paid clockify workspace
    def update_member_profile(
        self, workspace_id: str, user_id: str, params: MemberProfileGetParams = MemberProfileGetParams()
    ) -> MemberProfile:
        """Return one MemberProfile object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            user_id (str): ID of the clockify user.
            params (MemberProfileGetParams, optional): Path parameters. Defaults to MemberProfileGetParams().

        Returns:
            MemberProfile: MemberProfile object.
        """
        url = self.__url(workspace_id, user_id, True)
        return self._update_one(url, MemberProfile), params

    def __url(self, workspace_id: str, user_id: str = None, member_profile_model: bool = False) -> str:
        url = f"{BASE_URL}/workspaces/{workspace_id}/{'member-profile' if member_profile_model else 'users'}"
        if user_id:
            url += f"/{user_id}"
        return url
