from app import app

def test_home_page():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    # Check a fragment of the heading text
    assert b"End-to-End DevOps Pipeline" in resp.data

def test_health_endpoint():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "healthy", "service": "devops-mini-project"}
