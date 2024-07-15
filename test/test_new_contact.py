# -*- coding: utf-8 -*-
from model.contact import Contact


def test_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.open_contact_page()
    app.contact.create(Contact("Yurii", "Ezerskii", "Sergeevich",
                               "Nickname", "Title", "Solar", "Street",
                               "HomeNum", "999", "Work", "fax",
                               "test@gmail.com", "1", "January", "2024"))
    app.contact.go_home()
    app.session.logout()
