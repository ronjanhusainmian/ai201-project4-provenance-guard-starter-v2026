import time
from unittest.mock import patch
from app import app

def slow_detector(text):
    time.sleep(2)
    return 0.5

def test_timeout():
    with app.test_client() as client:
        with patch("detector.model_signal", side_effect=slow_detector):
            response = client.post("/submit", json={
                "text": "Test submission",
                "creator_id": "test_user"
            })
            assert response.status_code == 504

if __name__ == "__main__":
    test_timeout()
    print("Timeout test passed")