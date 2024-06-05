from telethon import TelegramClient, events

# Declare your API credentials
API_ID = 28283237  # Replace with your actual API ID
API_HASH = "1eacca10748a190c5ffd05573e6d26d9"  # Replace with your actual API hash

# Initialize the Telethon client with the existing session file
client = TelegramClient('session_name', API_ID, API_HASH)

# This function will be called when a new message is received
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # Get the sender ID of the message
    sender = await event.get_sender()
    sender_id = sender.id

    # Reply to the message
    await client.send_message(sender_id, "no more pain and suffering")

async def main():
    print("Connecting to Telegram...")
    await client.start()
    print("Client is running...")
    
    # Keep the client running to listen for incoming messages
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
