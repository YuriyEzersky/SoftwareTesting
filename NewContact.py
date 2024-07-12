# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_contact(app):
        app.login("admin", "secret")
        app.create_new_contact(Contact("Yurii", "Ezerskii", "Sergeevich",
                                       "Nickname", "Title", "Solar", "Street",
                                       "HomeNum", "999", "Work", "fax",
                                       "test@gmail.com", "1", "January", "2024"))
        app.go_home()
