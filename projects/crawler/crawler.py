def main():
	print("I am a webscraper")

if __name__ == "__main__":
    return main()

class Website(object):
	#create a function that gets URL (def URL)
	#create a function that turns HTML elements into an array of strings based on white space or '<> (def elements)
	#create a function that uses REGEX to find links that matches URL through <href> (def Pages)
	pass


class Page(Website):
	#set URL to one of the stuff that will come out from def Pages (inherit def Pages)
	#create a function that gets all elements from the page (inherit def elements)
	pass

class Email(Page):
	#source the elements from page and find elements with '@' through regex
	pass

class Name(Page):
	#set to find a page that has %ABOUT% (use REGEX)
	#set to find %string string% (use REGEX)
	pass

class Contact(Page):
	#set to find a page that has %Contact% (use REGEX)
	#filter to find digits (use REGEX)
	pass 
