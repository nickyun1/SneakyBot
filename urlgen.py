#Example URL: https://www.adidas.ca/en/mens-nmd_c2-shoes/BY3011.html

#Base URL = https://www.adidas.ca/en/

Model = raw_input("Model #\n")
Size = raw_input("Size #\n")

def URLGen(model, size):
	# Model and Size may need to be altered before inputting in html
	url = 'https://www.adidas.com/en/' + Model + '.html?forceSelSize=' + Size 
	return url

Find_it = URLGen(Model, Size)

print(str(Find_it))