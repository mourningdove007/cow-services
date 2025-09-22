from eth_account import Account
from eth_account.datastructures import SignedMessage
import time


def generate_order_request(private_key: str = "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d"):
    
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

    ## "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1" ## weth
    ## "0x0000000000000000000000000000000000000000" ## eth
    ## "0x6b175474e89094c44da98b954eedeac495271d0f", ## dai
    ## "0x6810e776880c02933d47db1b9fc05908e5386b96", ## cow


    ORDER_DATA = {
        "sellToken": "0x0000000000000000000000000000000000000000", ## dai
        "buyToken": "0x0000000000000000000000000000000000000000", ## cow
        "receiver": "0x6810e776880c02933d47db1b9fc05908e5386b96",
        "sellAmount": "1",
        "buyAmount": "1",
        "validTo": int(time.time()) + 3600,  ## Valid for 1 hour from now
        "feeAmount": "0",
        "kind": "buy",
        "partiallyFillable": False,
        "sellTokenBalance": "erc20",
        "buyTokenBalance": "erc20",
        "appData": "0x1ba2c7f5680dd17a4d852b9c590afa0969893c2b1052a7f553542697f5668171",
    }


    acct :Account = Account.from_key(
    private_key)

    signed_message:SignedMessage = acct.sign_typed_data(
        domain_data=DOMAIN_DATA, 
        message_types=ORDER_TYPE, 
        message_data=ORDER_DATA
        )

    signature_hex = signed_message.signature.hex()

    request_body = ORDER_DATA
    request_body["signingScheme"] = "eip712"
    request_body["signature"] = "0x" + signature_hex

    return request_body
