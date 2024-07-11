# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_groups(app):
    app.login("admin", "secret")
    app.create_new_group(Group("Ezerskii", "Header", "footer"))
    app.go_home()


def test_empty_groups(app):
    app.login("admin", "secret")
    app.create_empty_group(Group("", "", ""))
    app.go_home()
