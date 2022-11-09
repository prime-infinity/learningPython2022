message = input("> ").lower()
splited = message.split(" ")

expressions = {
    ":)": "happy_face_moji",
    ":(": "sad_face_moji",
}
new_st = ""
for w in splited:
    new_st += expressions.get(w, w) + " "

print(new_st)
