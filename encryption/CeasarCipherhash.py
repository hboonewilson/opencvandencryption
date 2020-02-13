     
def CaesarCipher(key, readfilename, writefilename):
     '''To properly encode this file you will need to have a key!'''
     #read filename to script and set to name message
     f = open(str(readfilename))
     message = f.read()
     #close read file
     f.close()
     #create encoded message string 
     encoded = ''
     #use HashForCoding() to determine numkey()
     numkey = HashForCoding(key)     
     #iterage message letters
     for let in message:
          #retrieve each letters numerical value
          val = ord(let)
          #code message using key
          code = val + numkey
          # if code is higher than list length
          if code > 65535:
          #subtract length of list from the code to reset
               code -= 65535
          #add coded letter to return str
          encoded += chr(code)
     #open a file to write on from writefilename
     codedmessage = open(writefilename, 'w')
     #write to file with string encoded
     codedmessage.write(encoded)
     #close file
     codedmessage.close()
     

def DecodeCaesarCipher(key, readfile, writefile):
     '''To decode this message you will need the key!'''
     #read encoded file
     f = open(readfile)
     message = f.read()
     #create decoded string
     decoded = ''
     #use HashForCoding() to find numeric key
     numkey = HashForCoding(key)     
     #iterage message letters
     for let in message:
          #retrieve each letter's original numerical value using ord() function
          val = ord(let)
          #decode using key
          decode = val - numkey
          #if decode is below 0 loop it to the charachters
          if decode < 0:
               decode += 65535
          #add decoded letter to retstr using chr()
          decoded += chr(decode)
     #open a new file to write on
     final = open(writefile, 'w')
     final.write(decoded)
     final.close()
     
def HashForCoding(publickey):
     ''' 
     NOT EXTREMELY SECURE ONLY FOR MATERIAL THAT IS NOT EXTREMELY VALUABLE 
     
     key is first passed through this function to create a hightened level
     of security that allows user to share key publicly. As long as the public 
     doesn't know the hash algorithm or isn't activley trying to crack the message 
     the only people who can understand the message are people with this function
     
     code will have 6535 different combinations so the encoding ins't fit for actual 
     security
     '''
     #hashsum
     hashsum = 0
     #for each character in key
     for i in range(0, len(publickey)):
          #hashsum += (character index + key length)^character... code (ord(letter))
          hashsum += (i + len(publickey)) ** ord(publickey[i])
          #then take final hash sum and % by 26 to determine number key for 
          #functions above
          rethash = hashsum % 65535 
     return rethash

#use input to determine wether person wants to encode/decode and what filenames 
#each will have



determine = True
#determine function
while determine:
     codeordecode = input('Would you like to encode or decode?\nEnter E/D: ')
     codeordecode.upper()
     if codeordecode =='E':
          filetoencode = input("What is the name of the file you would like to encode?\nInclude file extention: ")
          filefinish = input("What is the name of the file you would like to write?\nInclude file extention: ")
          thekey = input("What is the key? ")
          CaesarCipher(thekey, filetoencode, filefinish)
          print(f"File, {filefinish} has been encoded from {filetoencode}")
          break
     elif codeordecode=='D':
          filetodecode = input("What is the name of the file you would like to decode?\nInclude file extention: ")
          filedecoded  = input("What is the name of the file you would like to write?\nInclude file extention: ")
          key = input("what is the key? ")
          DecodeCaesarCipher(key, filetodecode, filedecoded)
          print(f"File, {filedecoded} has been decoded from {filetodecode}")
          break
     else:
          print('You must have typed somethig wrong. Try agian')
          print()