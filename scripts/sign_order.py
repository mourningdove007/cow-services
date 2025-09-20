from eth_account import Account
from eth_account.datastructures import SignedMessage
import time
import json


## see https://docs.cow.fi/cow-protocol/reference/core/signing-schemes

DOMAIN_DATA = {
    "name": "Gnosis Protocol",
    "version": "v2",
    "chainId": 1,
    "verifyingContract": "0x9008D19f58AAbD9eD0D60971565AA8510560ab41"
}

ORDER_TYPE = {
    "Order": [
        {"name": "sellToken", "type": "address"},
        {"name": "buyToken", "type": "address"},
        {"name": "receiver", "type": "address"},
        {"name": "sellAmount", "type": "uint256"},
        {"name": "buyAmount", "type": "uint256"},
        {"name": "validTo", "type": "uint32"},
        {"name": "appData", "type": "bytes32"},
        {"name": "feeAmount", "type": "uint256"},
        {"name": "kind", "type": "string"},
        {"name": "partiallyFillable", "type": "bool"},
        {"name": "sellTokenBalance", "type": "string"},
        {"name": "buyTokenBalance", "type": "string"}
    ]
}

"0x82aF49447D8a07e3bd95BD0d56f35241523fBab1" ## weth
"0x0000000000000000000000000000000000000000" ## eth


ORDER_DATA = {
    "sellToken": "0x6b175474e89094c44da98b954eedeac495271d0f", ## dai
    "buyToken": "0x6810e776880c02933d47db1b9fc05908e5386b96", ## cow
    "receiver": "0x6810e776880c02933d47db1b9fc05908e5386b96",
    "sellAmount": "1",
    "buyAmount": "1",
    "validTo": int(time.time()) + 3600,  ## Valid for 1 hour from now
    "feeAmount": "0",
    "kind": "buy",
    "partiallyFillable": False,
    "sellTokenBalance": "erc20",
    "buyTokenBalance": "erc20",
    "appData": "0xc85ef7d79691fe79573b1a7064c19c1a9819ebdbd1faaab1a8ec92344438aaf4", ## keccak256("cow")
}


acct :Account = Account.from_key(
0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6)

signed_message:SignedMessage = acct.sign_typed_data(
    domain_data=DOMAIN_DATA, 
    message_types=ORDER_TYPE, 
    message_data=ORDER_DATA
    )

signature_hex = signed_message.signature.hex()

request_body = ORDER_DATA
request_body["signingScheme"] = "eip712"
request_body["signature"] = signature_hex


print(f"Generated Signature:\n{signature_hex}")
print(f"Generated Request Body: {request_body}")

json_string = json.dumps(request_body, indent=4)

print("--- JSON String Output ---")
print(json_string)


