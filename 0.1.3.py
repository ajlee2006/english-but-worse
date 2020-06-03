def conv(s, f, t):
    fs = ''
    for i in s:
        if i in f:
            fs += t[f.index(i)]
        else:
            fs += i
    return fs

def convOrtho(s, opp=False):
    f = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    t = ['g', 'V', 'm', 'e', 'W', 'z', 'h', 'Q', 'Y', 'E', 'T', 'o', 'M', 'Z', 'P', 'O', 't', 'X', 'f', 'c', 'U', 'R', 'v', 'J', 'I', 'H', 'S', 'q', 'K', 'k', 'A', 'j', 'F', 'B', 'u', 'D', 'i', 'C', 'N', 'd', 'n', 'w', 'b', 'x', 'G', 'L', 'y', 'p', 'l', 'r', 'a', 's']
    if opp:
        f,t = t,f
    return(conv(s,f,t))

def convPhono(s):
    f = ['p','t','ʈ','c','k','q','ɸ','f','θ','s','ʃ','ʂ','ç','x','χ','ħ','h','ɬ','i','ɨ','ɯ','ɪ','e','ɘ','ɤ','ɛ','ɜ','ʌ','a','ɑ','b','d','ɖ','ɟ','g','ɢ','β','v','ð','z','ʒ','ʐ','ʝ','ɣ','ʁ','ʕ','ɦ','ɮ','y','ʉ','u','ʏ','ø','ɵ','o','œ','ɞ','ɔ','ɶ','ɒ']
    t = ['b','d','ɖ','ɟ','g','ɢ','β','v','ð','z','ʒ','ʐ','ʝ','ɣ','ʁ','ʕ','ɦ','ɮ','y','ʉ','u','ʏ','ø','ɵ','o','œ','ɞ','ɔ','ɶ','ɒ','p','t','ʈ','c','k','q','ɸ','f','θ','s','ʃ','ʂ','ç','x','χ','ħ','h','ɬ','i','ɨ','ɯ','ɪ','e','ɘ','ɤ','ɛ','ɜ','ʌ','a','ɑ']
    return(conv(s,f,t))

def reverse(s):
    import re
    sentl = [i.strip() for i in s.split('.')]
    lis = []
    for i in sentl:
        l = re.findall(r"\w+|[^\w\s]", i, re.UNICODE)
        l.reverse()
        lis.append(' '.join(l))
    return '. '.join(lis)

def inputopt(q, o, t):
    inp = input(q + ' (' + o + '/' + t + ') [' + o + '] ')
    if inp == t:
        return False
    return True


# s = 'Our Father, which art in heaven,  \nhallowed be thy name;  \nthy kingdom come;  \nthy will be done,  \nin earth as it is in heaven.  \nGive us this day our daily bread.  \nAnd forgive us our trespasses,  \nas we forgive them that trespass against us.  \nAnd lead us not into temptation,  \nbut deliver us from evil.  \nFor thine is the kingdom,  \nthe power, and the glory,  \nFor ever and ever.  \nAmen.'
# s = 'ˈaʊər ˈfɑðər, wɪʧ ɑrt ɪn ˈhɛvən,  \nˈhæloʊd bi ðaɪ neɪm;  \nðaɪ ˈkɪŋdəm kʌm;  \nðaɪ wɪl bi dʌn,  \nɪn ɜrθ əz ɪt əz ɪn ˈhɛvən.  \ngɪv əs ðɪs deɪ ˈaʊər ˈdeɪli brɛd.  \nənd fərˈgɪv əs ˈaʊər ˈtrɛˌspæsɪz,  \nəz wi fərˈgɪv ðəm ðət ˈtrɛˌspæs əˈgɛnst ʌs.  \nənd lid əs nɑt ˈɪntə tɛmˈteɪʃən,  \nbət dɪˈlɪvər əs frəm ˈivəl.  \nfər ðaɪn əz ðə ˈkɪŋdəm,  \nðə ˈpaʊər, ənd ðə ˈglɔri,  \nfər ˈɛvər ənd ˈɛvər.  \neɪˈmɛn.'
# s = 'All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.'
# s = 'ɔl ˈhjumən ˈbiɪŋz ər bɔrn fri ənd ˈikwəl ɪn ˈdɪgnəti ənd raɪts. ðeɪ ər ɛnˈdaʊd wɪð ˈrizən ənd ˈkɑnʃəns ənd ʃəd ækt təˈwɔrdz wʌn əˈnʌðər ɪn ə ˈspɪrət əv ˈbrʌðərˌhʊd.'
ortho = inputopt('Convert orthography or phonology?','o','p')
ddd = inputopt('Disable or enable sentence reversal (beta)?','d','e')
if ortho:
    s = input('Enter English: ')
    if ddd:
      s = reverse(s)
    print(convOrtho(s))
else:
    s = input('Enter IPA: ')
    if ddd:
      s = reverse(s)
    print(convPhono(s))
