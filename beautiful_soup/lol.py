import base64

final = open("Encoded File.b64", "rb")

encode = final.read()

data = base64.decodestring(encode)

decode = open("decodedfile.pdf", "wb")
decode.write(data)
