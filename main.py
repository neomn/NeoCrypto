from neocrypto.neocrypto import NeoCrypto

nc = NeoCrypto(23)
print(f'private key: {nc.key}', "\n")
print(f'public key: {nc.pub_key}, "\n"')

encrypted = nc.encrypt('hi')
print(f"encrypt message (hi) ==> {encrypted}", "\n")
print(f"decrypt message  ==> {nc.decrypt(encrypted)}", "\n")
