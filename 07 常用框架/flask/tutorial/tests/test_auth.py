import pytest
from flask import g
from flask import session

from flaskr.db import get_db


def test_register(client, app):
    # testAPI that viewing the page renders without template errors
    assert client.get("/auth/register").status_code == 200

    # testAPI that successful registration redirects to the login page
    response = client.post("/auth/register", data={"username": "a", "password": "a"})
    assert "http://localhost/auth/login" == response.headers["Location"]

    # testAPI that the user was inserted into the Database
    with app.app_context():
        assert (
            get_db().execute("SELECT * FROM user WHERE username = 'a'").fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("testAPI", "testAPI", b"already registered"),
    ),
)
def test_register_validate_input(client, username, password, message):
    response = client.post(
        "/auth/register", data={"username": username, "password": password}
    )
    assert message in response.data


def test_login(client, auth):
    # testAPI that viewing the page renders without template errors
    assert client.get("/auth/login").status_code == 200

    # testAPI that successful login redirects to the index page
    response = auth.login()
    assert response.headers["Location"] == "http://localhost/"

    # login request set the user_id in the session
    # check that the user is loaded from the session
    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user["username"] == "testAPI"


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("a", "testAPI", b"Incorrect username."), ("testAPI", "a", b"Incorrect password.")),
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session
