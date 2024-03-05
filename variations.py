def cipher_func(secret_msg:str, cipher:dict): # call the message and the cipher which is now a dic
    decoded_messages = [] # create a list to store the decoded messages

    def decode(message, current=""): #create a new method that takes the secret message, and empty string to be filled with the decoded message
        if not message:
            decoded_messages.append(current) # after the decoding add the message to the list of decoded messages, if it is not already added
            return 1
        count = 0
        for letter, number in cipher.items(): # iterate cipher(dict)
            if message.startswith(str(number)): #use the function startswith to check secrete message starts with the value of the dict on the specific key:value pair
                count += decode(message[len(str(number)):], current + letter) # count the number of messages that occur, and also recursevely take the numbers after the last checked, and add to the "current" string key from the dict which represents the letter
        return count
    
    total_count = decode(secret_msg) # assign the number of messages to a variable
    print(total_count) #print the count
    
    for decoded_msg in decoded_messages:
        print(decoded_msg) # print the messages on a new line

scr_msg = input()
cipher = input()
dict = {}
# Convert the cipher string into a dictionary
for i in range(len(cipher)):
    if cipher[i].isalpha():
        letter = cipher[i]
        number = ""
        
        for j in range(i+1, len(cipher)):
            if cipher[j].isalpha():
                break
            number+=cipher[j]
            
        dict[letter] = int(number) #match the letter witht the digit

cipher_func(scr_msg, dict)