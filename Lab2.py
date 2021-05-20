def validate_url(url):
    """Validates the given url passed as string.
	
	Arguments:
    url -- String, A valid url should be of form <Protocol>://<hostmain>/<fileinfo>
	
	Protocol = [http, https, ftp]
	Hostname = string
	Fileinfo = [.html, .csv, .docx]
	"""

    # your code starts here.
    #print(url) # debug
    
    statusProtocol = False
    statusFileName = False
    index = 0

    valid_protocols = ["http","https","ftp"]
    valid_fileinfo = [".html",".csv",".docx"]

    #Extract the procol from the URL.
    workingString = url.split(":")

    #print(workingString[0]) #debug
    #print(workingString[1]) #debug

    """ Debug section 
    for protocol in valid_protocols:
        print(protocol)
        if protocol == workingString[0]:
            statusProtocol = True
    print(statusProtocol) # debug
    """
    
    # Compare each protocol to what was entered.
    if valid_protocols[0] == workingString[0]:
        statusProtocol = True
    if valid_protocols[1] == workingString[0]:
        statusProtocol = True
    if valid_protocols[2] == workingString[0]:
        statusProtocol = True

    #print(statusProtocol) # debug

    # Extract the file name type.
    workingString = url.split(".")
    numberOfElememtns = len(workingString) - 1
    #print (numberOfElememtns) # debug
    #print (workingString) #debug

    """ Debug section.
    workingString = url.split(".")
    index = len(workingString) - 1
    #print(workingString[index]) 
    for fileName in valid_fileinfo:
        #print(fileName) #debug
        if fileName == "." + workingString[index]:
            statusFileName = True
    print(statusFileName) 
    """
    
    # Match the form of the file type list.
    workingString[numberOfElememtns] = "." + workingString[numberOfElememtns]
    #print(workingString[numberOfElememtns]) #debug

    if (workingString[numberOfElememtns]) == valid_fileinfo[0]:
        statusFileName = True
    if (workingString[numberOfElememtns]) == valid_fileinfo[1]:
        statusFileName = True 
    if (workingString[numberOfElememtns]) == valid_fileinfo[2]:
        statusFileName = True  
    #print(statusFileName) # debug

    # return True if url is valid else retutn False.
    # Note that we are using an implicit comparison here.   
    if statusProtocol and statusFileName:
        return True
    else:
        return False
           
if __name__ == '__main__':
#	url = input("Enter an Url: ")
    url = "https://www.planetware.com/pictures/france-f.html"
    print(validate_url(url))
	



