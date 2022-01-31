def translate(this_dict, s):
    
    swed = []
    for i in s:   
        swed.append(this_dict.get(i))
    return(" ".join(swed))

this_dict = {
        "merry":"god",
        "christmas":"jul",
        "and":"och",
        "happy":"gott",
        "new":"nytt",
        "year":"ar"
        }
s = input("Enter your wish ").lower().split()
print(translate(this_dict, s))