"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""
import random

class Codec:
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.letter = string.ascii_letters + '0123456789'
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            shortUrl = ''.join(random.choice(self.letter) for _ in range(6))
            if shortUrl not in self.url2code.values():
                self.url2code[longUrl] = shortUrl
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return  self.url2code.keys()[self.url2code.values().index(shortUrl[-6:])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))