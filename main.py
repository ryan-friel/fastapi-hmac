from fastapi import FastAPI, Body, HTTPException
import hmac
import hashlib
import json

app = FastAPI()


# Arbitrary secret key.
secret_key: str = "abc123"


async def validate_json(json_object: dict) -> bool:
    """
    Validate the JSON object from request.
    Ensure the json_object is indeed a dictionary.
    """
    if type(json_object) != dict:
        return False
    return True


@app.get("/")
async def read_root():
    return {"Message": "Welcome to my demo!"}


@app.post("/generate-token")
async def generate_token(request_body = Body(...)) -> str:
    """
    Generate a token from the request body.
    """

    valid_json: bool = await validate_json(request_body)

    if valid_json:
        payload: dict = request_body
        payload_hmac: str = json.dumps(payload)

        # Generate the token.
        encoded_key = str.encode(secret_key)
        new_hmac = hmac.new(encoded_key, payload_hmac.encode("UTF-8"), hashlib.sha256)
        token = new_hmac.hexdigest()

        # Add the signature token to the payload.
        payload["signature"] = token

        return json.dumps(payload)

    else:
        raise HTTPException(status_code=404, detail="Invalid JSON")


