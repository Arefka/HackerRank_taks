'''
===============================================================

    Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

    One fine day, a finite number of tourists come to stay at the hotel.
    The tourists consist of:
    → A Captain.
    → An unknown group of families consisting of K members per group where   K ≠ 1.

    The Captain was given a separate room, and the rest were given one room per group.

    Mr. Anant has an unordered list of randomly arranged room entries.
    The list consists of the room numbers for all of the tourists.
    The room numbers will appear K times per group except for the Captain's room.

    Mr. Anant needs you to help him find the Captain's room number.
    The total number of tourists or the total number of groups of families is not known to you.
    You only know the value of K and the room number list.

===============================================================
'''

group_len = input()
rooms_string = input()
rooms_number_list = rooms_string.split(' ')


all_unique_rooms = set();
all_rooms_without_capitan_room = set();
for room in rooms_number_list:
    if room in all_unique_rooms:
        all_rooms_without_capitan_room.add(room);
    else:
        all_unique_rooms.add(room);
result_set=all_unique_rooms.difference(all_rooms_without_capitan_room);
print(list(result_set)[0])