import cv2
import sys

def str_to_binary(message):
  binary_string=''
  for char in message:
    num=ord(char)
    binary=format(num, '08b')
    binary_string+=binary
  return binary_string

def binary_to_str(binary_message):
  message=''
  for i in range(0, len(binary_message), 8):
    binary=binary_message[i:i+8]
    num=int(binary, 2)
    char=chr(num)
    message+=char
  return message
  

def encryption(name, message, result):
  img=cv2.imread(name)
  data=img
  data=data.reshape((-1))
  msg=str_to_binary(message)
  length=len(msg)
  binary_length=format(length, '016b')
  msg=binary_length+msg
  if data.size<len(msg):
    print("Image is too small")
    return
  for i in range(len(msg)):
    if data[i]%2==int(msg[i]):
      continue
    if data[i]==0 and msg[i]=='1':
      data[i]=1
    else:
      data[i]-=1
  data=data.reshape((img.shape))
  cv2.imwrite(result, data)
  
def decryption(name):
  img=cv2.imread(name)
  data=img.reshape((-1))
  msg=''
  length=''
  for i in range(16):
    length+=str(data[i]%2)
  length=int(length, 2)
  for i in range(16, length+16):
    msg+=str(data[i]%2)
  message=binary_to_str(msg)
  return message
  
  

if __name__=='__main__':
  # Instructions:
  #   usage: 
  #     for encryption: pass args: en   path_to_image   message_to_hide   path_for_final_image
  #     for decryption: pass args: de path_to_image
  #   the extension of final image extension should be png
  try:
    if len(sys.argv)<2:
      raise Exception('Invalid Arguments')
    if sys.argv[1]=='en':
      if len(sys.argv)!=5:
        raise Exception('Invalid Arguments')
      encryption(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1]=='de':
      if len(sys.argv)!=3:
        raise Exception('Invalid Arguments')
      print(decryption(sys.argv[2]))
  except:
    print("Wrong usage or invalid arguments")
