# Instagram Follower Comparison Tool

A simple Python script that analyzes your Instagram data to identify accounts you follow that don't follow you back.

## Description

This tool compares your Instagram followers and following lists from your downloaded Instagram data. It parses the HTML files and provides a clear list of accounts that don't follow you back, helping you manage your Instagram connections.

## Prerequisites

- Python 3.x
- BeautifulSoup4 library

## Installation

1. Clone or download this repository
2. Install the required dependency:
   ```bash
   pip install beautifulsoup4
   ```

## How to Get Your Instagram Data

1. Open Instagram on a web browser or mobile app
2. Go to **Settings** → **Privacy and Security** → **Data Download** (or **Request Download**)
3. Request your data by entering your email address
4. Wait for Instagram to send you a download link (usually takes a few hours to a couple of days)
5. Download and extract the ZIP file
6. Navigate to the folder containing your data

## Usage

1. Locate the HTML files from your Instagram data:
   - **Following list**: Usually named something like `following.html` or `followers_and_following.html`
   - **Followers list**: Usually named something like `followers.html` or `followers_1.html`

2. Rename the files and place them in the same directory as `comapre.py`:
   - Rename your **following list** to `file1.html`
   - Rename your **followers list** to `file2.html`

3. Run the script:
   ```bash
   python comapre.py
   ```

## Output

The script will display:
- A numbered list of usernames you follow but who don't follow you back
- A summary showing the total count of non-reciprocal follows

Example output:
```
Usernames you follow but who don't follow you back:

username1 (1/25)
username2 (2/25)
username3 (3/25)
...

25/150 accounts not compliant
```

## Notes

- The script only reads local HTML files; it does not access Instagram directly
- Your Instagram data remains private on your local machine
- File names must be exactly `file1.html` (following) and `file2.html` (followers) for the script to work

## Disclaimer

This tool is for personal use only. Use it responsibly and in accordance with Instagram's Terms of Service.
