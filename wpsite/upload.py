import requests




def uploadPost():
    # Authenticate with WordPress
    response = requests.post(
     "https://example.com/wp-json/jwt-auth/v1/token",
     json={"username": "your_username", "password": "your_password"}
    )

# Get the authorization token from the response
    token = response.json().get("token")

# Create a new post in WordPress
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {
        "title": "My New Post",
        "content": "This is the content of my new post.",
        "status": "publish" 
    }
    
    response = requests.post(
        "https://example.com/wp-json/wp/v2/posts",
        headers=headers,
        json=data
    )

# Get the ID of the new post from the response
    post_id = response.json().get("id")