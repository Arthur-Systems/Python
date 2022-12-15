text = 'Friends, Romans, countrymen, lend me your ears: I come to bury Caesar, not to praise him.'
punctuation_marks = '.,?!:;"\'+=%$#@*&^|\/()[]{}'
refined_text = ''.join(
    [char for char in text if char not in punctuation_marks])
d = {w: refined_text.count(w) for w in refined_text.split()}

print(d if d else 'No words found')
print(refined_text)
print(d)
