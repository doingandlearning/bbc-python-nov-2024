import requests
import json


def fetch_json(url):
    response = requests.get(url)  # get, post, patch, put, delete

    if response.status_code == 200:
        data = response.json()
        print("Data fetched successfully")
    else:
        print(f'Failed to fetch the data: {response.status_code}')
        data = []
    return data


def filter_by_user(id, posts):
    filtered_data = []
    for post in posts:
        if post["userId"] == id:
            filtered_data.append({
                "userId":  post["userId"],
                "postId":  post["id"],
                "title":  post["title"],
                "text": post["body"]
            })
    return filtered_data


def write_data_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"  # /users /photos /tasks
    posts = fetch_json(url)
    filtered_posts = filter_by_user(4, posts)
    write_data_to_file(filtered_posts, "user-4-posts.json")