str = "TEMPLE"

duplicate_char = []
for character in str:
   
      if str.count(character) > 1:

         if character not in duplicate_char:
            duplicate_char.append(character)
print(*duplicate_char)
