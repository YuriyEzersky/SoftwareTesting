def test_delete_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.open_contact_page()
    app.contact.delete_first_contact()
    app.contact.go_home()
    app.session.logout()
