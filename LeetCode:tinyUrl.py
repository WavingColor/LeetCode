# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


class Codec:
    
    urls = {'0': 'url'}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        shortUrl = 'http://tinyurl.com/' + str(len(self.urls))
        self.urls[shortUrl] = longUrl
        print(shortUrl)
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
url1 = "https://leetcode.com/problems/design-tinyurl"
url2 = "https://leetcode.com/problems/deee"

codec = Codec()
codec.decode(codec.encode(url1))
codec.decode(codec.encode(url2))