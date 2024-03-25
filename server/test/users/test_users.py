from test.client import client

# Example
def test_get_users():
  response = client.get("/users")
  assert response.status_code == 404