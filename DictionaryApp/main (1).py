#for each friend store the number

dic = {}

dic2 = {}

dic3 = {
    "First Item": "Get Groceries",
    "Second Item": "Do Homework",
    "Third Item": "Hangout with friends"
}

#add 4th item to dic3 - order a mattress on amazon

#("Fourth Item":"Order a mattress on Amazon")
#Add school each friend goes to in dic
#dic.update({"friend1":"Hawkins HS","friend2":"John Evans HS","friend3":"John Evans HS"})
#add start date to dic2

dic2["CS101"] = {
    "name": "Computer Science Introduction",
    "Start Date": "01/01/2024"
}
dic2["IT203"] = {
    "name": "Data Management and Information",
    "Start Date": "01/01/2024"
}

dic["friend1"] = {"number": 1234, "School": "Hawkins HS"}
dic["friend2"] = {"number": 1234, "School": "John Evans HS"}
dic["friend3"] = {"number": 1234, "School": "John Evans HS"}

dic3["Fourth Item"] = "Order a mattres on Amazon"

dic3["Fifth Item"] = "Call your parents"

#print(dic)

#print(dic2)

basketball_players = {
    "Lebron James": {
        "height": "6'8",
        "weight": "250 pounds",
        "wingspan": "7'",
        "age": 38
    },
    "Chris Paul": {
        "height": "6'1",
        "weight": "200 pounds",
        "wingspan": "6'4",
        "age": 38
    }
}
basketball_players["Russel Westbrook"] = {
    "height": "6'6",
    "weight": "230 pounds",
    "wingspan": "6'8",
    "age": 36
}

#print(basketball_players["Lebron James"]["wingspan"])

# Lebron james's contract worth: $200 million, starts: 2021, ends: 2024
basketball_players["Lebron James"]["contract"] = {
  "amount":"$200 million",
  "start":2021,
  "ends":2024
}
#print(basketball_players)

dir={Mom:'1234567',Dad:'55567785'}

