# re Library

import re

def re_demo():
    text = """
    Hello my name is Krisha.
    My email is krisha123@gmail.com
    Alternate email: test.user@company.co.in
    Contact number: 9876543210
    Another number: 9123456789
    """

    print("ORIGINAL TEXT:")
    print(text)

    print("\n1. re.search()")
    result = re.search(r"email", text)
    if result:
        print("Found 'email' at index:", result.start())

    print("\n2. re.match()")
    result = re.match(r"Hello", text.strip())
    print("Match found:", bool(result))

    print("\n3. re.findall()")
    emails = re.findall(r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z.]+", text)
    print("Emails found:", emails)

    print("\n4. re.sub()")
    masked_text = re.sub(r"\b[6-9][0-9]{9}\b", "XXXXXXXXXX", text)
    print(masked_text)

if __name__ == "__main__":
    re_demo()
