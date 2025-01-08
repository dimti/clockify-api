from random import randint
from clockify.model.user_model import User, MemberProfile
from tests.test import ClockifyTestCase
from clockify.session import ClockifySession

class TestUsers(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_get_current_user(self):
        user = self.session.get_current_user()
        self.assertIsInstance(user, User)

    def test_get_list_of_users(self):
        users = self.session.user.get_users(self.WORKSPACE)
        for user in users:
            self.assertIsInstance(user, User)

    def test_get_member_profile(self):
        user = self.session.user.get_users(self.WORKSPACE).pop()
        member_profile = self.session.user.get_member_profile(self.WORKSPACE, user.id_)
        self.assertIsInstance(member_profile, MemberProfile)