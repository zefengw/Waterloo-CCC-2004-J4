def divide_string(l, n):
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def encode_string(keyword, string):
  #concatenates alphabetical words 
  only_alpha = ""
  for i in string:
    if i.isalpha():
      only_alpha += i
  #create list with the same number of elements for each sublist 
  l = [list(keyword)] + list(divide_string(list(only_alpha), len(keyword)))
  word = ""
  for rows in range(1, len(l)):
    for cols in range(len(l[rows])):
        res = ord(l[rows][cols])
        res += ord(l[0][cols])
        if res > 91:
          result = res - 65
          if result > 91 or result < 65:
            word += chr(abs(result - 91) + 65)
          else:
            word += chr(result)
        else:
          word += chr(res)
  return word
  
key = input("Enter keyword(all uppercase): ")
message = input("Enter message to encrypt(all uppercase): ")

print(f"Your key was {key} and your message was {message} and after being encrypted, your message is now {encode_string(key, message)}.")