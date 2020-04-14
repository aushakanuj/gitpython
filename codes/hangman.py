def check(word,blank,wu):

    for w,bs in zip(word,blank):
        if len(word)!= len(blank):
            return False
        elif bs=="_" and w in wu:
            return False
        elif bs!="_" and bs!=w:
            return False
        else:
            return True

print(check("cat","_a_","sdawv"))


