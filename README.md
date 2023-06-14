# Facebook Comment Scraping Tool

This is a Python script that uses Selenium WebDriver to extract comments from a specific Facebook post.

## Usage

1. Install the required dependencies by running the following command:

2. Update the following variables in the code according to your requirements:
- `email`: Your Facebook login email.
- `password`: Your Facebook login password.
- `post_url`: The URL of the specific Facebook post you want to extract comments from.

3. Run the code using Python:

4. The script will open a Chrome browser, log into Facebook, navigate to the specified post URL, extract the comments, and save them to a file named "comments.txt" in the same directory as the code file.

## Limitations

- This code assumes that the provided `post_url` is valid and points to a Facebook post with comments. Make sure to provide a valid URL.
- The code relies on the structure and elements present on the Facebook website. If there are any changes to the website structure or element locators, the code may need to be updated accordingly.

Feel free to customize and enhance the code according to your specific requirements. Happy extracting!

