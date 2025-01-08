import os
from unittest import TestCase

from clockify.session import ClockifySession
from clockify.model.project_model import ProjectGetParams
from clockify.model.tag_model import TagGetParams
from clockify.model.time_entry_model import TimeEntryGetParams


class ClockifyTestCase(TestCase):
    KEY = os.environ.get('API_KEY')
    WORKSPACE = os.environ.get('WORKSPACE')

    CLIENT = '6263de4b5ca9a1421d1cdbaa'
    USER: str

    NON_EXISTING_CLIENT = '1234abcd'
    NON_EXISTING_WORKSPACE = '1234abcd'
    
    _TEST_NAME_PREFIX = 'Test'

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        cls.USER = cls.session.get_current_user().id_
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        projects = cls.session.project.get_projects(cls.WORKSPACE, ProjectGetParams(
            name=cls._TEST_NAME_PREFIX
        ))
        for project in projects:
            project.archived = True
            cls.session.project.update_project(project)
            cls.session.project.delete_project(cls.WORKSPACE, project.id_)
        tags = cls.session.tag.get_tags(cls.WORKSPACE, TagGetParams(
            name=cls._TEST_NAME_PREFIX
        ))
        for tag in tags:
            tag.archived = True
            cls.session.tag.update_tag(tag)
            cls.session.tag.delete_tag(cls.WORKSPACE, tag.id_)
        time_entries = cls.session.time_entry.get_time_entries(cls.WORKSPACE, cls.USER, TimeEntryGetParams(
            description=cls._TEST_NAME_PREFIX
        ))
        for time_entry in time_entries:
            cls.session.time_entry.delete_time_entry(cls.WORKSPACE, time_entry.id_)
        return super().tearDownClass()
