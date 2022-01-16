import hashlib
import requests

seckey = "FLWSECK_TEST-88ebd2a6edb534bbc663d33efcd1211a-X"
hashedseckey = hashlib.md5(seckey.encode("utf-8")).hexdigest()
hashedseckeylast12 = hashedseckey[-12:]
seckeyadjusted = seckey.replace('FLWSECK-', '')
seckeyadjustedfirst12 = seckeyadjusted[:12]

# print(seckeyadjustedfirst12 + hashedseckeylast12)


resp = requests.post("https://tnttukbbvmi.sandbox.verygoodproxy.com/post",
                    headers={"Content-type": "application/json"},
                    json={ "secret_key": "4pXY0grBDyaqeiAAwQ7T5g=="})

print(str(resp.text))
