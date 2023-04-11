def cipher(plaintext):
  ciphertext = ""
  for p in plaintext:
    if ord("a") <= ord(p) <= ord("z"):
      ciphertext += chr(219 - ord(p))
    else:
      ciphertext += p
  return ciphertext

plaintext = "Now Let's Start The Game!"
ciphertext = cipher(plaintext)
print("plaintext: '{0}'".format(plaintext))
print("Encryption: '{0}' => '{1}'".format(plaintext, ciphertext))
print("Decryption: '{0}' => '{1}'".format(ciphertext, cipher(ciphertext)))
