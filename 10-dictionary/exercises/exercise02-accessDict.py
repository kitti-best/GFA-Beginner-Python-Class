play_roblox_info =  {"event_name": "Play roblox", "event_date": "22/3/2024", "event_location": "Online"}
exam_prepare_info = {"event_name": "Exam prepare", "event_date": "23/3/2024", "event_location": "Library"}
movie_night_info =  {"event_name": "Movie night", "event_date": "22/3/2024", "event_location": "John's house"}

print("Play roblox event details:")
print("Event name:", play_roblox_info["event_name"])
print("Event date:", play_roblox_info["event_date"])
print("Event location:", play_roblox_info["event_location"])

print("\nExam prepare event details:")
print("Event name:", exam_prepare_info["event_name"])
print("Event date:", exam_prepare_info["event_date"])
print("Event location:", exam_prepare_info["event_location"])

print("\nMovie night event details:")
print("Event name:", movie_night_info["event_name"])
print("Event date:", movie_night_info["event_date"])
print("Event location:", movie_night_info["event_location"])

# # or a shorter version
# # List of event dictionaries
# events_info = [play_roblox_info, exam_prepare_info, movie_night_info]

# # Iterate through each event dictionary
# for event_info in events_info:
#     print("\nEvent details:")
#     # Iterate through key-value pairs in the event dictionary
#     for key, value in event_info.items():
#         print(f"{key}: {value}")