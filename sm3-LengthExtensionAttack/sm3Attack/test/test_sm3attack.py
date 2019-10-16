from gmssl import sm3attack, func

if __name__ == '__main__':
      print("please enter the string(length is 3):")
      strin=input()
      str1=strin.encode()
    
      y=sm3attack.sm3_hash(func.bytes_to_list(str1+b'\x80'+b'\x00'*59+b'\x18\x61\x62\x63'))

      print(y)
