from bs4 import BeautifulSoup
"""
This script extracts usernames from two HTML files representing Instagram followers and following lists.
It identifies usernames that you follow but who do not follow you back.
"""
def extract_usernames_from_html(file_path):
    """
    Extracts usernames and URLs from the HTML file.
    Returns a dictionary mapping usernames to their full Instagram URLs.
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

# Extract usernames and URLs
following_data = extract_usernames_from_html(file1_path)
followers_data = extract_usernames_from_html(file2_path)

# Identify non-reciprocal follows
following_usernames = set(following_data.keys())
followers_usernames = set(followers_data.keys())
not_following_back = sorted(following_usernames - followers_usernames)

total_accounts = len(following_usernames)
not_compliant_count = len(not_following_back)

# Display results
print("Usernames you follow but don't follow you back:")
for username in not_following_back:
    print(f"https://www.instagram.com/{username}")
