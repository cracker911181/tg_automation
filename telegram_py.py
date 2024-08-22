from telethon import TelegramClient

# Replace these with your values
api_id = 26195706
api_hash = '4359e1140c7abff2979906877ac4b91d'
phone_number = '+8801824231993'  # Your phone number including country code
recipient_username = '@abdurrabbi321'  # The username of the recipient or a chat ID
message = 'google.com'

# Create a client instance
client = TelegramClient('session_name', api_id, api_hash)

async def send_message():
    await client.start(phone_number)
    # Send the message
    await client.send_message(recipient_username, message)
    print('Message sent!')

# Run the client
with client:
    client.loop.run_until_complete(send_message())
