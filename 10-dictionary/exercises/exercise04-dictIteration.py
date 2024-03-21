user_infos = [
    {"first_name":"Nero", "last_name":"Gomm", "email":"ngomm0@disqus.com", "gender":"Male"}, 
    {"first_name":"Elwood", "last_name":"Lebel", "email":"elebel1@upenn.edu", "gender":"Male"}, 
    {"first_name":"Clare", "last_name":"Luca", "email":"cluca2@creativecommons.org", "gender":"Male"}, 
    {"first_name":"Townsend", "last_name":"Taye", "email":"ttaye3@devhub.com", "gender":"Male"}
]

# loop through user infos to get each info
for user_info in user_infos:
    # loop through the info and get each key
    for key in user_info:
        # print each key
        print(key, ":", user_info[key])
    print()