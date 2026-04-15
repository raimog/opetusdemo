import requests
import time

BASE_URL = "http://localhost:5000"

def wait_for_app():
    for _ in range(15):
        try:
            r = requests.get(BASE_URL, timeout=2)
            if r.status_code == 200:
                return
        except requests.RequestException:
            pass
        time.sleep(2)
    raise RuntimeError("Sovellus ei käynnistynyt ajoissa")

def test_homepage():
    r = requests.get(BASE_URL, timeout=5)
    assert r.status_code == 200

def test_example_page():
    r = requests.get(f"{BASE_URL}/esimerkki", timeout=5)
    assert r.status_code == 200

if __name__ == "__main__":
    wait_for_app()
    test_homepage()
    test_example_page()
    print("Smoke test OK")
