def are_you_playing_banjo(name: str):
    # Implement me!
    if name.startswith("R") or name.startswith("r"):
        #print (name)
        return name + " plays banjo"
    return name + " does not play banjo"


print(are_you_playing_banjo("aria"))
print(are_you_playing_banjo("raja"))

    