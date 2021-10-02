team = { 
    "name" : "Elevation Fight Team",
    "location" : "Denver, Colorado",
    "address" : "1304 S Santa Fe Drive",
    "email" : "elevationfightteamco@gmail.com",
    "Founded" : "2013",
    "athletes": [
        {
            "id" : 1,
            "name" : "Corey Sandhagen", 
            "win": "14", 
            "loss" : "3", 
            "draw": "0" 
        },
        {
            "id" : 2,
            "name" : "Neil Magny", 
            "win": "25", 
            "loss" : "8", 
            "draw": "0" 
        },
        {
            "id" : 3,
            "name" : "Curtis Blaydes", 
            "win": "15", 
            "loss" : "3", 
            "draw": "0" 
        },  
    ]
}

print("The entire list: ", team)
print()
print("The the athlete at index 1 : ", team["athletes"][1])