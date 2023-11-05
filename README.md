# Post-Quantum Asymetric Cryptography For Python
## quick start:


```
# install the package using pip
pip install neocrypto
```

```Python
from neocrypto.NeoCrypto import NeoCrypto


nc = NeoCrypto(23) # enter a prime number in range 23-499 inclusive,
# now nc contains randomly-generate private and public keys

encrypted_message = nc.encrypt(' give me an sting to encrypt it for you :) ')
decrypted_message = nc.decrypt(encrypted_message)

# save keys into a file
nc.save_private_key(file_path) # example file path ==> '/home/$user/.neocrypto/private_key.txt'
nc.save_public_key(file_path)  # example file path ==> '/home/$user/.neocrypto/public_key.txt'

# read keys from a text file
nc.read_private_key(file_path)
nc.read_public_key(file_path)

# read keys from an string 
nc.read_private_key_from_string(private_key_in_string_format)
nc.read_public_key_from_string(public_key_in_string_format)

```

### NeoCrypto is a lightweight and easy to use package can be used for post quantum cryptography with python 
[how NeoCrypto works](https://github.com/neomn/harper-encrypt)
