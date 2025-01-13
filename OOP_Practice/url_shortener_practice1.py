'''
Problem Statement: Shorten URL
You need to design a service that shortens URLs. The service should:

Encode a given URL into a shortened version.
Decode the shortened URL back to the original URL.
Ensure that shortened URLs are unique and consistent (a given URL should always result in the same shortened URL).
Constraints:

The service should handle billions of URLs.
The shortened URL should be as short as possible.
Optimize for fast encoding/decoding.
Assume no special character constraints in URLs.

Class:
- ShortenUrl
    - url: str
    - shortened_url: str
    - url_map: {shortened: original}

shorten_url: shortens url
get_original_url: get back original
_generate_alternative

'''

import random


class ShortenUrl:
    def __init__(self,):
        self.url = ""
        self.shortened_url = ""
        self.url_map = {}

    def shorten_url(self, url: str) -> str:
        shorten = hash(url)
        shortened_url = f"https://{shorten}"
        while shortened_url in self.url_map and len(shortened_url) < len(url):
            random_character = random.choice(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"])
            shortened_url = shortened_url + random_character
        self.url_map[shortened_url] = url
        return shortened_url

    def get_original_url(self, shortened_url: str) -> str:
        if shortened_url not in self.url_map:
            raise Exception

        return self.url_map[shortened_url]


if __name__ == '__main__':
    shortenurl = ShortenUrl()
    url = "https://chatgpt.com"
    shortenedurl = shortenurl.shorten_url(url=url)
    original = shortenurl.get_original_url(shortened_url=shortenedurl)


'''
Shows missing knowledge about encoding and decoding.
Naive and not useful approach for hashing (not consistent for security resasons) and also the random.choice. --> Should be using base62 encoding and decoding
The encoding and decoding methods you referenced deal with Base62, which is a numeral system that uses 62 characters (A-Z, a-z, 0-9). It’s commonly used in applications like URL shortening because it produces short, human-readable strings.

Here’s a step-by-step explanation of the code:

_encode(num: int)
This method converts an integer into a Base62-encoded string.

How it Works:
Characters List:

characters = string.ascii_letters + string.digits:
Contains all 62 possible characters: ['A', ..., 'Z', 'a', ..., 'z', '0', ..., '9'].
These characters serve as the "digits" of the Base62 system.
Repeated Division by 62:

To convert a number from base 10 (decimal) to base 62:
Append the remainder (num % 62) to the result (maps to a character in characters).
Divide the number by 62 (num //= 62) to reduce the number.
Repeat until the number becomes 0.
Reverse the Result:

Since division gives the digits in reverse order, reverse the list at the end.
Example:
Encoding the number 12345:

Step 1: 12345 % 62 = 13 → characters[13] = 'N'
Step 2: 12345 // 62 = 199
Step 3: 199 % 62 = 13 → characters[13] = 'N'
Step 4: 199 // 62 = 3
Step 5: 3 % 62 = 3 → characters[3] = 'D'
Step 6: Result is ['D', 'N', 'N'], reverse it to get 'NN'.
_decode(short: str)
This method converts a Base62 string back into a base 10 (decimal) number.

How it Works:
Characters List:

Same as in _encode.
Calculate the Base 62 Value:

Treat the string as a number in base 62.
For each character:
Multiply the running total by the base (62).
Add the index of the current character from the characters list.
Example:
Decoding the string 'DNN':

Step 1: Initialize num = 0.
Step 2: For char = 'D': num = 0 * 62 + characters.index('D') = 3.
Step 3: For char = 'N': num = 3 * 62 + characters.index('N') = 199.
Step 4: For char = 'N': num = 199 * 62 + characters.index('N') = 12345.
Result: 12345.

Why Use Base62?
Compact Representation:

Base62 uses fewer characters compared to base 10 or hexadecimal, producing shorter strings.
Human-Readable:

The encoded string is alphanumeric, making it easy to read and type.
No Special Characters:

Base62 avoids characters like /, = (used in Base64), which can cause issues in URLs.
Base62 is a lightweight, efficient way to represent unique IDs or numbers in a compact format, ideal for URL shortening or generating unique identifiers. This implementation ensures that:

Each number corresponds to a unique string (deterministic).
Encoding and decoding are efficient (O(log(num)) due to repeated division).

'''