# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_groups(app):
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.create(Group("Ezerskii", "Header", "footer"))
    app.group.go_home()
    app.session.logout()


def test_empty_groups(app):
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.create(Group("", "", ""))
    app.group.go_home()
    app.session.logout()
