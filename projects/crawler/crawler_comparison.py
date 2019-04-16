
# no need to use (Object) syntax - it usually just bogs down the readability.
# if it doesn't inherit from anything, make that clear by omitting the (...) bit
class Website:
    def __init__(self, entry_url):
        self.url = entry_url
        self.pages = []

    #create a function that gets URL (def URL)
    #create a function that turns HTML elements into an array of strings based on white space or '<> (def elements)
    #create a function that uses REGEX to find links that matches URL through <href> (def Pages)


# page does not inherit from website, you're website contains pages, so you should have
# pages be a property of website, not `class Page(Website)`
class Page:
    def __init__(self, url):
        self.url = url

    #set URL to one of the stuff that will come out from def Pages (inherit def Pages)
    #create a function that gets all elements from the page (inherit def elements)


# I'm going to add an extra class, PageElement to serve as a parent for email and name
class PageElement:
    def __init__(self, content):
        self.content = content

# same as above-  ClassA(ClassB) indicates classA inherits all of classB's methods,
# properties, etc.
class Email(PageElement):
    def __init__(self, address):
        self.address = address
    #source the elements from page and find elements with '@' through regex

class Name(PageElement):
    def __init__(self, name):
        self.name = name
    #set to find a page that has %ABOUT% (use REGEX)
    #set to find %string string% (use REGEX)

class Contact:
    def __init__(self, email, name=None):
        self.email = email
        self.name = name
    #set to find a page that has %Contact% (use REGEX)
    #filter to find digits (use REGEX)



# NOTE: usually these will be found at the end of the file, so everything else is
#       declared first
def main():
    base_url = "www.somewebsite.com"
    print("I am a webscraper")

    website = Website(base_url)
    # proceed to initiate crawling, parsing, etc.

if __name__ == "__main__":
    return main()

