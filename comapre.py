from bs4 import BeautifulSoup

def extract_usernames_from_html(file_path):
    """
    Extracts usernames from the HTML file.
    Usernames are found in the href attribute of <a> tags.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    # Extract usernames from <a> tags with href containing 'instagram.com'
    usernames = {a_tag.text for a_tag in soup.find_all('a', href=True) if 'instagram.com' in a_tag['href']}
    return usernames

# File paths
file1_path = 'file1.html'  # Replace with your first file path (Following)
file2_path = 'file2.html'  # Replace with your second file path (Followers)

# Extract usernames from both files
following_usernames = extract_usernames_from_html(file1_path)
followers_usernames = extract_usernames_from_html(file2_path)

# Find usernames you follow but who don't follow you back
not_following_back = following_usernames - followers_usernames

# Display results
print("Usernames you follow but don't follow you back:")
for username in not_following_back:
    print(username)
