from fastapi.testclient import TestClient
from main import app, connectAndRoute
import os

client = TestClient(app)
connectAndRoute()

# Testing Broker API Endpoints
def test_broker():

    # Checking if the routes has properly there!
    try: # Github
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print(str(app.routes), file=fh)
    except: # Local
        print(client.base_url)
        print(app.routes)
        pass

    # Post
    sample_broker = {
        "First_Name": "Harry",
        "Last_Name": "Potter",
        "Email_Address": "harrypotter@temp.com",
        "Username": "harry",
        "Pass": "potter123"
    }

    response = client.post("/broker", json=sample_broker)
    
    try:
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print(response.json(), file=fh)
    except:
        pass

    assert response.status_code == 200

    broker_id = response.json().get('Id')
    assert isinstance(broker_id, int)

    # Get
    response = client.get(f"broker/{broker_id}")
    assert response.status_code == 200

    broker_name = response.json().get('First_Name')
    assert broker_name == 'Harry'

    # Put
    sample_broker["First_Name"] = "Henrietta"

    response = client.put(f"broker/{broker_id}", json=sample_broker)
    assert response.status_code == 200

    response = client.get(f"broker/{broker_id}")
    broker_name = response.json().get('First_Name')
    assert broker_name == 'Henrietta'

    # Delete
    response = client.delete(f"broker/{broker_id}")
    assert response.status_code == 200