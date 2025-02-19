import os
from azure.eventhub import EventHubConsumerClient

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Connection string and Event Hub name from environment variables
CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENTHUB_NAME = os.getenv("EVENT_HUB_NAME")
CONSUMER_GROUP = "$Default"

if not CONNECTION_STR or not EVENTHUB_NAME:
    raise ValueError("The environment variables EVENT_HUB_CONNECTION_STRING and EVENT_HUB_NAME must be set!")

# Function to process received messages
def on_event(partition_context, event):
    print(f"📡 Message received from Partition {partition_context.partition_id}: {event.body_as_str()}")
    partition_context.update_checkpoint(event)  # Save checkpoint to avoid re-reading messages

# Create the client
client = EventHubConsumerClient.from_connection_string(CONNECTION_STR, CONSUMER_GROUP, eventhub_name=EVENTHUB_NAME)

# Start receiving messages
with client:
    print("📡 Listening for messages from Event Hub...")
    client.receive(on_event=on_event, starting_position="@latest")  # "@latest" ensures new messages only
