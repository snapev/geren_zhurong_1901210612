from gmssl import sm3, func

if __name__ == '__main__':
      y=sm3.sm3_hash(func.bytes_to_list(b'\x61\x62\x63'))
      #y=sm3.sm3_hash(func.bytes_to_list(b'\x61\x62\x63'+b'\x80'+b'\x00'*59+b'\x18\x61\x62\x63'))

      print(y)
