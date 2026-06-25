import requests


def fetch_linkedin_user(username):
    url = f"https://www.linkedin.com/in/{username}/"

    try:
        response = requests.get(url, timeout=5, allow_redirects=True)

        if response.status_code == 404:
            print("Invalid username: LinkedIn user not found.")
            return None

        response.raise_for_status()
        return url

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return None

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")
        return None


username = input("Enter LinkedIn username: ").strip()

if username == "":
    print("Username cannot be empty.")
else:
    account_url = fetch_linkedin_user(username)

    if account_url is not None:
        print(f"Username: {username}")
        print(f"Account URL: {account_url}")
