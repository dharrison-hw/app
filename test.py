import json

import hyperwallet

data = {
    "profileType": "INDIVIDUAL",
    "clientUserId": "tkjkj3wkj9934",
    "firstName": "John",
    "lastName": "Developer",
    "email": "tkjkj3wkj9934@email.com",
    "dateOfBirth": "1991-02-15",
    "addressLine1": "575 Market St",
    "city": "San Francisco",
    "country": "US",
    "stateProvince": "CA",
    "postalCode": "94105",
    "programToken": "prg-15cefcdc-2363-4bf0-ab3e-b7d9959bcdd7"
}

client = hyperwallet.utils.ApiClient(
    "restapiuser@5046781612",
    "Password1$",
    "https://api.sandbox.hyperwallet.com"
)

response = client.doPost("users", data)

print json.dumps(response.json(), indent = 2)
