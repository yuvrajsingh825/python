import requests  # Import the requests library so we can send HTTP requests.


def api_get(url, headers=None, params=None, timeout=5):  # Create a reusable function for GET API requests.
    try:  # Start a try block so we can handle errors safely.
        response = requests.get(  # Send a GET request and store the server response.
            url,  # Pass the API URL to requests.get().
            headers=headers,  # Send custom headers, such as Authorization.
            params=params,  # Send query parameters, such as userId.
            timeout=timeout  # Stop waiting if the server takes too long.
        )  # End the requests.get() call.

        if response.status_code == 404:  # Check if the server returned a 404 Not Found error.
            print("Error: 404 Not Found")  # Print a helpful message for a missing page or endpoint.
            return None  # Return None because there is no useful data to process.

        response.raise_for_status()  # Raise an error for other bad status codes like 400 or 500.
        return response.json()  # Convert the JSON response into Python data and return it.

    except requests.exceptions.Timeout:  # Run this block if the request takes longer than the timeout.
        print("Error: Request timed out")  # Print a timeout error message.
        return None  # Return None because the request failed.

    except requests.exceptions.RequestException as error:  # Run this block for any other requests error.
        print(f"Error: {error}")  # Print the real error message to help with debugging.
        return None  # Return None because the request failed.


url = "https://jsonplaceholder.typicode.com/posts"  # Store the posts API endpoint.

headers = {  # Create a dictionary for custom request headers.
    "Authorization": "Bearer my-token"  # Add an Authorization header with a sample bearer token.
}  # End the headers dictionary.

params = {  # Create a dictionary for query parameters.
    "userId": 1  # Filter posts so the API only returns posts from userId 1.
}  # End the params dictionary.

posts = api_get(url, headers=headers, params=params, timeout=5)  # Call the reusable API function.

if posts is not None:  # Check that the API call worked before printing data.
    print(f"Total posts found: {len(posts)}")  # Print how many posts were returned.

    for post in posts:  # Loop through each post returned by the API.
        print(f"Post ID: {post['id']}")  # Print the post ID.
        print(f"User ID: {post['userId']}")  # Print the user ID to show the filter worked.
        print(f"Title: {post['title']}")  # Print the post title.
        print("-" * 30)  # Print a separator line between posts.
