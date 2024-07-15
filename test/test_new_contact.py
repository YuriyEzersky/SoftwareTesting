# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.open_contact_page()
    app.contact.create(Contact("Yurii", "Ezerskii", "Sergeevich",
                               "Nickname", "Title", "Solar", "Street",
                               "HomeNum", "999", "Work", "fax",
                               "test@gmail.com", "1", "January", "2024"))
    app.contact.go_home()
    app.session.logout()
