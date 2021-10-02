def me(name, about):
	print("- {}: {}".format(name, about))

def contributors():
	# How to add your name:
	#  insert same like below, in last of def contributors():
	#    me("your name", "your wish")
	#
	# Example:
	#
	# def contributors():
	#    me("first contributor", "happy hacktoberfest")
	#    me("your contributor", "i love cat~")  <-- your example pull request
	# 
	# More info check pull requests
	# 
	me("Ayra", "Feel free to pull request!")
	me("Hafitz", "Just wanna contribute")


print(" ")
print("Happy Hacktoberfest 2021!")
print("Here is our contributors from worldwide:")
contributors()
