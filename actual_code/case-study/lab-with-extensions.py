import requests
import json
import csv
import os
import shutil
import time
from datetime import datetime

# API endpoints
posts_url = "https://jsonplaceholder.typicode.com/posts"
users_url = "https://jsonplaceholder.typicode.com/users"


# Backup JSON file with timestamp
def backup_json_file(filename):
    if os.path.exists(filename):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = f"{filename.split('.')[0]}_backup_{timestamp}.json"
        shutil.copy(filename, backup_filename)
        print(f"Backup created: {backup_filename}")


# Fetch data from an API with error handling
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
        return []


# Parse and filter post data
def parse_posts(data):
    return [
        {
            "userId": post["userId"],
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        for post in data
    ]


# Fetch and combine user data with post data
def add_usernames_to_posts(posts, users):
    user_map = {user["id"]: user["username"] for user in users}
    for post in posts:
        post["username"] = user_map.get(post["userId"], "Unknown")


# Write data to JSON file
def write_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")


# Write data to CSV file
def write_csv(data, filename):
    headers = ["userId", "id", "title", "body", "username"]
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")


# Main function to fetch, process, and save data
def main():
    backup_json_file("posts.json")  # Backup existing JSON file if it exists

    # Step 1: Fetch posts and users
    print("Fetching posts...")
    posts_data = fetch_data(posts_url)

    print("Fetching users...")
    users_data = fetch_data(users_url)

    # Step 2: Parse posts and add usernames
    filtered_posts = parse_posts(posts_data)
    add_usernames_to_posts(filtered_posts, users_data)

    # Step 3: Write JSON and CSV outputs
    write_json(filtered_posts, "posts.json")
    write_csv(filtered_posts, "posts.csv")


# Run the main function repeatedly with delay
if __name__ == "__main__":
    while True:
        main()
        print("Waiting for the next fetch cycle...")
        time.sleep(300)  # Fetch data every 5 minutes
