mood_responses = {
    "happy":{
        "emoji":"😊",
        "message":"That's awesome! keep smiling!"
    },
    "sad":{
        "emoji":"😢",
        "message":"It's okay to feel sad. Things will get better!"
    },
    "angry":{
        "emoji":"😡",
        "message":"Take a deep breath. Try to stay calm."
    },
    "excited":{
        "emoji":"🤩"
        "message" "Yay! That sounds exciting!"
    },
    "tired":{
        "emoji":"😴",
        "message":"Get some rest, you deserve it!"
    },
    "anxious":{
        "emoji":"😰",
        "message":"Take it one step at a time. You’ve got this!"
    },
    "bored":{
    "emoji":"😐",
    "message":"Maybe try something new or creative!"
    }
}
mood="sad"
response=mood_responses.get(mood.lower(),{"emoji":"🤔","message":"Mood is not recognized."})
print(f"{response['emoji']} {response['message']}")
