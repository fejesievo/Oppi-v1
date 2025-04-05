# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC145c3e3a61bf764734dd152854f838f6"
auth_token = "aa3dc45136f08fa9e0d25671322d8649"
client = Client(account_sid, auth_token)

call = client.calls.create(
    record=True,
    from_="+18887075362",
    to="+12235337707", #
    url="https://7701-64-9-55-225.ngrok-free.app/incoming-call",
)

print(call.sid)