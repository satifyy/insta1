from bs4 import BeautifulSoup

def extract_usernames_from_html(file_path):
    """
    Extracts usernames from the HTML file.
    Usernames are found in the href attribute of <a> tags.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    usernames = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if 'instagram.com' in href:
            # Strip trailing slash and grab the last path segment (works for both
            # /username and /_u/username URL formats)
            username = href.rstrip('/').split('/')[-1]
            if username:
                usernames.add(username)
    return usernames

# File paths
file1_path = 'following.html'  # Replace with your first file path (Following)
file2_path = 'followers_1.html'  # Replace with your second file path (Followers)

# Extract usernames from both files
following_usernames = extract_usernames_from_html(file1_path)
followers_usernames = extract_usernames_from_html(file2_path)

# Find usernames you follow but who don't follow you back
not_following_back = following_usernames - followers_usernames

# Display results
print("Usernames you follow but don't follow you back:")
for username in not_following_back:
    print(f"https://www.instagram.com/{username}")
