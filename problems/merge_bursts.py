"""
Question:
Message Burst Merger

Given a list of chat messages, implement a solution to group messages by user and merge consecutive messages from the same user into "bursts". Messages sent within 30 seconds of each other belong to the same burst, while messages sent more than 30 seconds apart start a new burst.

Each burst should be represented as a tuple containing:

- The timestamp of the first message in the burst
- The timestamp of the last message in the burst
- The concatenated text of all messages in the burst (joined with spaces)
Input:

A list of dictionaries with keys: user_id, timestamp, text
Output:

A dictionary mapping each user_id to a list of their message bursts

Input: [
    {"user_id": 1, "timestamp": 100, "text": "Hello"},
    {"user_id": 1, "timestamp": 120, "text": "How are you?"},
    {"user_id": 1, "timestamp": 200, "text": "Goodbye"}
]

Output: {
    1: [(100, 120, "Hello How are you?"), (200, 200, "Goodbye")]
}
"""


from collections import defaultdict

    
def merge_bursts(messages: list[dict]):
    """
    Groups messages by user ID and merges consecutive messages into bursts.
    
    Args:
        messages: A list of message dictionaries containing user_id, timestamp, and text.
    
    Returns:
        A dictionary mapping user_id to their list of merged message bursts.
    """
    # Create a dictionary to store messages grouped by user ID
    user_msgs = {}
    bursts = {}
    
    # Group all messages by their user_id
    for msg in messages:
        user_id  = msg["user_id"]
        if user_id not in user_msgs:
            user_msgs[user_id] = []
        
        user_msgs[user_id].append(msg)
    
    # For each user, merge their messages into bursts
    for user_id, user_msg_list in user_msgs.items():
        bursts[user_id] = merge_msgs(user_msg_list)
    
    return bursts


def merge_msgs(msg_list: list[dict]):
    """
    Merges messages within a 30-second window into bursts.
    
    Messages sent within 30 seconds of each other are considered part of the same burst
    and their text is concatenated. Messages sent more than 30 seconds apart start a new burst.
    
    Args:
        msg_list: A list of message dictionaries for a single user.
    
    Returns:
        A list of tuples, each containing (start_timestamp, end_timestamp, merged_text).
    """
    # Sort messages by timestamp to process them chronologically
    msg_list = sorted(msg_list, key=lambda x: x["timestamp"])
    
    last_msg = None
    merged_bursts = []
    burst_text = ""
    end_ts = None
    
    # Iterate through each message and group them into bursts
    for msg in msg_list:
        # Initialize the first message of a burst
        if last_msg is None:
            last_msg = msg
            burst_text = msg["text"]
            start_ts = msg["timestamp"]
            continue
        
        # If the message is within 30 seconds of the last message, add it to the current burst
        if msg["timestamp"] - last_msg["timestamp"] <= 30:
            burst_text += " " + msg["text"]
            end_ts = msg["timestamp"]
            last_msg = msg
        else:
            # If more than 30 seconds have passed, save the current burst and start a new one
            if end_ts is not None:
                burst = (start_ts, end_ts, burst_text)
                print(f"Merging messages from {start_ts} to {end_ts}: {burst_text}: {burst=}")
                merged_bursts.append(burst)
                
            last_msg = None
            burst_text = ""
            end_ts = None
    
    # Handle the last burst after the loop completes
    if end_ts is not None:
            burst = (start_ts, end_ts, burst_text)
            print(f"Merging messages from {start_ts} to {end_ts}: {burst_text}: {burst=}")
            merged_bursts.append(burst)
    
    return merged_bursts

if __name__ == "__main__":
    sample_messages_1 = [
        {"user_id": 1, "timestamp": 100, "text": "Hello"},
        {"user_id": 1, "timestamp": 120, "text": "How are you?"},
        {"user_id": 1, "timestamp": 200, "text": "Goodbye"},
        {"user_id": 2, "timestamp": 150, "text": "Hey"},
        {"user_id": 2, "timestamp": 170, "text": "What's up?"},
    ]
    
    sample_messages_2 = [
        {"user_id": 1, "timestamp": 320, "text": "Let me know."},
        {"user_id": 2, "timestamp": 400, "text": "See you later."},
        {"user_id": 2, "timestamp": 420, "text": "Take care."},
        {"user_id": 1, "timestamp": 300, "text": "Are you there?"},
        {"user_id": 2, "timestamp": 430, "text": "Bye!"},
        {"user_id": 2, "timestamp": 465, "text": "Buddy!"}
    ]

    for exm in [sample_messages_1, sample_messages_2]:
        print("Processing new example messages: =========================")
        merged = merge_bursts(exm)
        for user_id, bursts in merged.items():
            print(f"User {user_id}:")
            for burst in bursts:
                print(f"  Burst from {burst[0]} to {burst[1]}: {burst[2]}")
        