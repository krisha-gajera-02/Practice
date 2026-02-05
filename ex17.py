# Requests Library

import requests

def requests_demo():

    print("1. GET Request")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    print("\n2. GET with Query Parameters")
    params = {"userId": 1}
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params
    )
    print("URL Used:", response.url)
    print("First Result:", response.json()[0])

    print("\n3. Headers")
    headers = {
        "User-Agent": "MyPythonApp/1.0"
    }
    response = requests.get(url, headers=headers)
    print("Headers Sent:", headers)

    print("\n4. Response Content")
    print("Text:", response.text[:100])
    print("JSON:", response.json())

    print("\n5. Timeout")
    try:
        requests.get(url, timeout=2)
        print("Request successful")
    except requests.exceptions.Timeout:
        print("Request timed out")

if __name__ == "__main__":
    requests_demo()
