def run_length_encoding(s):
    
    prev_letter = s[0]
    prev_letter_count = 0
    output = ''
    for current_letter in s:
        if current_letter==prev_letter:
            
            prev_letter_count=prev_letter_count+1
            
        else:
            output = output + str(prev_letter_count) + prev_letter
            prev_letter=current_letter
            prev_letter_count = 1
            
    output = output + str(prev_letter_count) + prev_letter
    return output

s = input("Enter string value: ")
s = s.upper()
print(run_length_encoding(s))

