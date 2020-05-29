#s = 'Our Father, which art in heaven,  \nhallowed be thy name;  \nthy kingdom come;  \nthy will be done,  \nin earth as it is in heaven.  \nGive us this day our daily bread.  \nAnd forgive us our trespasses,  \nas we forgive them that trespass against us.  \nAnd lead us not into temptation,  \nbut deliver us from evil.  \nFor thine is the kingdom,  \nthe power, and the glory,  \nFor ever and ever.  \nAmen.'
#s = 'All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.'
s = input('Enter English: ')
f = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
t = ['g', 'V', 'm', 'e', 'W', 'z', 'h', 'Q', 'Y', 'E', 'T', 'o', 'M', 'Z', 'P', 'O', 't', 'X', 'f', 'c', 'U', 'R', 'v', 'J', 'I', 'H', 'S', 'q', 'K', 'k', 'A', 'j', 'F', 'B', 'u', 'D', 'i', 'C', 'N', 'd', 'n', 'w', 'b', 'x', 'G', 'L', 'y', 'p', 'l', 'r', 'a', 's']
fs = ''
for i in s:
    if i in f:
        fs += t[f.index(i)]
    else:
        fs += i
print(fs)
