from bs4 import BeautifulSoup

def extract_usernames_from_html(file_path):
    """
    Extracts usernames from the HTML file.
    Usernames are found in the text content of <a> tags with href containing 'instagram.com'.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    usernames = {a_tag.text.strip() for a_tag in soup.find_all('a', href=True) if 'instagram.com' in a_tag['href']}
    return usernames

# File paths
file1_path = 'file1.html'  # Replace with your Following HTML file path
file2_path = 'file2.html'  # Replace with your Followers HTML file path

# Extract usernames
following_usernames = extract_usernames_from_html(file1_path)
followers_usernames = extract_usernames_from_html(file2_path)

# Identify non-reciprocal follows
not_following_back = sorted(following_usernames - followers_usernames)
total_accounts = len(following_usernames)
not_compliant_count = len(not_following_back)

# Display results
print("Usernames you follow but who don't follow you back:\n")
for idx, username in enumerate(not_following_back, start=1):
    print(f"{username} ({idx}/{not_compliant_count})")

# Summary
print(f"\n{not_compliant_count}/{total_accounts} accounts not compliant")
