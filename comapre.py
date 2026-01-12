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
    username_dict = {}
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if 'instagram.com' in href:
            # Extract username from URL (e.g., from https://www.instagram.com/_u/1nickgarcia)
            parts = href.rstrip('/').split('/')
            username = parts[-1]
            username_dict[username] = href
    
    return username_dict

# File paths
file1_path = 'data/file1.html'  # Replace with your Following HTML file path
file2_path = 'data/file2.html'  # Replace with your Followers HTML file path

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
print("Usernames you follow but who don't follow you back:\n")
for idx, username in enumerate(not_following_back, start=1):
    print(f"{username}")
    print(f"{following_data[username]} ({idx}/{not_compliant_count})\n")

# Summary
print(f"{not_compliant_count}/{total_accounts} accounts not compliant")
