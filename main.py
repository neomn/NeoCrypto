from neocrypto.neocrypto import NeoCrypto

nc = NeoCrypto(23)
print(f'private key: {nc.key}', "\n")
print(f'public key: {nc.pub_key}, "\n"')

print(f"encrypt message (hi) ==> {nc.encrypt('hi')}", "\n")
