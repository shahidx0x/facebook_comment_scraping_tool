### Usage
Update the following variables in the code according to your requirements:

email: Your Facebook login email.
password: Your Facebook login password.
post_url: The URL of the specific Facebook post you want to extract the <ul> content from.
Run the code using Python.

The code will open a Chrome browser, log into Facebook, navigate to the specified post URL, extract the text from the <ul> element, and save it to a file named "comment.txt" in the same directory as the code file.

After executing, you can find the extracted text in the "comment.txt" file.

Limitations
This code assumes that the provided XPath for the <ul> element is correct and will successfully locate the desired element. Make sure to provide a valid XPath to ensure accurate results.
The code relies on the structure and elements present on the Facebook website. If there are any changes to the website structure or element locators, the code may need to be updated accordingly.
