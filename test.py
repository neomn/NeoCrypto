from neocrypto.neocrypto import NeoCrypto

nc = NeoCrypto(23)
private = nc.generate_private_key()
public = nc.generate_public_key(private)

print(private)
print(public)

