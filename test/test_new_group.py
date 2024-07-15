# -*- coding: utf-8 -*-
from model.group import Group


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
