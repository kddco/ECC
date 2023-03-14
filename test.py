from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import socket

curve = ec.SECP256K1()

# 從私鑰計算出公鑰
private_key = ec.generate_private_key(curve, default_backend())
public_key = private_key.public_key()


print(len("04e451d328600d64f04c98bb665ccca6fe94bdafd213c65aab1bceaed0baf13f071f90b44a885f9f0bb387bc0bc74b41f26d514a4d2c3fc2cb35a57d19966ac115"))