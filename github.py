import requests


def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            print("Invalid username: GitHub user not found.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return None

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")
        return None


username = input("Enter GitHub username: ").strip()

if username == "":
    print("Username cannot be empty.")
else:
    user = fetch_github_user(username)

    if user is not None:
        print(f"Login: {user['login']}")
        print(f"Followers: {user['followers']}")
        print(f"Public Repositories: {user['public_repos']}")
        print(f"Account URL: {user['html_url']}")
