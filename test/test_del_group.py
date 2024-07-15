def test_delete_first_group(app):
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.delete_first_group()
    app.group.go_home()
    app.session.logout()
