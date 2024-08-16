# https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/

import base64


# Encode
sample_string = "GeeksForGeeks is the best"
sample_string_bytes = sample_string.encode("utf-8")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("utf-8")

print(f"Encoded string: {base64_string}")


# Decode
base64_bytes = base64_string.encode("utf-8")

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("utf-8")

print(f"Decoded string: {sample_string}")
