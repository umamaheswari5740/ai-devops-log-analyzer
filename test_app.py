
from app import app


def test_home_page():
    app.config["TESTING"] = True
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"AI-Powered DevOps Log Analyzer" in response.data


def test_empty_submission():
    app.config["TESTING"] = True
    client = app.test_client()

    response = client.post("/", data={"logs": ""})

    assert response.status_code == 200
    assert b"Please upload a log file or paste some logs." in response.data


def test_unsupported_file():
    app.config["TESTING"] = True
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "logfile": (
                __import__("io").BytesIO(b"not a log"),
                "document.pdf"
            )
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Please upload a .log or .txt file." in response.data
