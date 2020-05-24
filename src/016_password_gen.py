#!../bin/python

"""016_password_gen.py

This is a Python learning project from:
http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, uppercase 
letters, numbers, and symbols. The passwords should be random, generating 
a new password every time the user asks for a new password. Include your 
run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak 
    passwords, pick a word or two from a list.


"""

print('Hello World! This is 016_password_gen.py\n')

import random
import string

words = ["sector","available","financial","process","individual","specific","principle","estimate","variables","method","data","research","contract","environment","export","source","assessment","policy","identified","create","derived","factors","procedure","definition","assume","theory","benefit","evidence","established","authority","major","issues","labour","occur","economic","involved","percent","interpretation","consistent","income","structure","legal","concept","formula","section","required","constitutional","analysis","distribution","function","area","approach","role","legislation","indicate","response","period","context","significant","similar","community","resident","range","construction","strategies","elements","previous","conclusion","security","aspects","acquisition","features","text","commission","regulations","computer","items","consumer","achieve","final","positive","evaluation","assistance","normal","relevant","distinction","region","traditional","impact","consequences","chapter","equation","appropriate","resources","participation","survey","potential","cultural","transfer","select","credit","affect","categories","perceived","sought","focus","purchase","injury","site","journal","primary","complex","institute","investment","administration","maintenance","design","obtained","restricted","conduct •comments","convention","published","framework","implies","negative","dominant","illustrated","outcomes","constant","shift","deduction","ensure","specified","justification","funds","reliance","physical","partnership","location","link","coordination","alternative","initial","validity","task","techniques","excluded","consent","proportion","demonstrate","reaction","criteria","minorities","technology","philosophy","removed","sex","compensation","sequence","corresponding","maximum","circumstances","instance","considerable","sufficient","corporate","interaction","contribution","immigration","component","constraints","technical","emphasis","scheme","layer","volume","document","registered","core","overall","emerged","regime","implementation","project","hence","occupational","internal","goals","retained","sum","integration","mechanism","parallel","imposed","despite","job","parameters","approximate","label","concentration","principal","series","predicted","summary","attitudes","undertaken","cycle","communication","ethnic","hypothesis","professional","status","conference","attributed","annual","obvious","error","implications","apparent","commitment","subsequent","debate","dimensions","promote","statistics","option","domestic","output","access","code","investigation","phase","prior","granted","stress","civil","contrast","resolution","adequate","alter","stability","energy","aware","licence","enforcement","draft","styles","precise","medical","pursue","symbolic","marginal","capacity","generation","exposure","decline","academic","modified","external","psychology","fundamental","adjustment","ratio","whereas","enable","version","perspective","contact","network","facilitate","welfare","transition","amendment","logic","rejected","expansion","clause","prime","target","objective","sustainable","equivalent","liberal","notion","substitution","generated","trend","revenue","compounds","evolution","conflict","image","discretion","entities","orientation","consultation","mental","monitoring","challenge","intelligence","transformation","presumption","acknowledged","utility","furthermore","accurate","diversity","attached","recovery","assigned","tapes","motivation","bond","edition","nevertheless","transport","cited","fees","scope","enhanced","incorporated","instructions","subsidiary","input","abstract","ministry","capable","expert","preceding","display","incentive","inhibition","trace","ignored","incidence","estate","cooperative","revealed","index","lecture","discrimination","overseas","explicit","aggregate","gender","underlying","brief","domain","rational","minimum","interval","neutral","migration","flexibility","federal","author","initiatives","allocation","exceed","intervention","confirmed","definite","classical","chemical","voluntary","release","visible","finite","publication","channel","file","thesis","equipment","disposal","solely","deny","identical","submitted","grade","phenomenon","paradigm","ultimately","extract","survive","converted","transmission","global","inferred","guarantee","advocate","dynamic","simulation","topic","insert","reverse","decades","comprise","hierarchical","unique","comprehensive","couple","mode","differentiation","eliminate","priority","empirical","ideology","somewhat","aid","foundation","adults","adaptation","quotation","contrary","media","successive","innovation","prohibited","isolated","highlighted","eventually","inspection","termination","displacement","arbitrary","reinforced","denote","offset","exploitation","detected","abandon","random","revision","virtually","uniform","predominantly","thereby","implicit","tension","ambiguous","vehicle","clarity","conformity","contemporary","automatically","accumulation","appendix","widespread","infrastructure","deviation","fluctuations","restore","guidelines","commodity","minimises","practitioners","radical","plus","visual","chart","appreciation","prospect","dramatic","contradiction","currency","inevitably","complement","accompany","paragraph","induced","schedule","intensity","crucial","via","exhibit","bias","manipulation","theme","nuclear","bulk","behalf","unified","commenced","erosion","anticipated","minimal","ceases","vision","mutual","norms","intermediate","manual","supplementary","incompatible","concurrent","ethical","preliminary","integral","conversely","relaxed","confined","accommodation","temporary","distorted","passive","subordinate","analogous","military","scenario","revolution","diminished","coherence","suspended","mature","assurance","rigid","controversy","sphere","mediation","format","trigger","qualitative","portion","medium","coincide","violation","device","insights","refine","devoted","team","overlap","attained","restraints","inherent","route","protocol","founded","duration","whereby","inclination","encountered","convinced","assembly","albeit","enormous","reluctant","posed","persistent","undergo","notwithstanding","straightforward","panel","odd","intrinsic","compiled","adjacent","integrity","forthcoming","conceived","ongoing","so-called","likewise","nonetheless","levy","invoked","colleagues","depression","collapse"]
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = "!#$%&()*+,-.:;<=>?@[]^_{|}~."


"""

The thought process behind this program is to create an pool array of either
printable ASCII character or English word candidates based upon the user's 
strength request.

From this candidate pool, use a while loop to append items to a raw password 
list until the minimum length requirement is met.  By using a minimum length, 
we are able to more simply accomodate the word candidates rather than having 
to match an  exact length.

Once the length requirement is met, then join the raw password list into a
string.  If the strength requirement is Level 1 (words only), join the 
words with a hyphen for readability.

Lastly, display the password to the user.

"""

# get the user's password specification
def get_input():
    res = []
    res.append(int(input('Please enter minimum password length: ')))
    res.append(int(input('Enter a complexity level 1-5: ')))
    return res

# generate a pool of characters/words based on the user strength entry
def make_char_set(level):
        global words, lower, upper, digits, special
        if level == 1:
            return words
        elif level == 2:
            return lower
        elif level == 3:
            return lower + upper
        elif level == 4:
            return lower + upper + digits
        elif level == 5:
            return lower + upper + digits + special
        else:
            return ""

# password maker
def gen_pwd(min_len, strength, pool):
    raw = [] # a list to hold the random characters

    # loop until the minimum length is met
    while len("".join(raw)) < min_len:
        # 1. generate a random integer
        # 2. use that integer as the index for the pool character/word
        # 3. append the result to raw[]
        raw.append(pool[random.randint(0, len(pool) - 1)])
        
    # handle the difference between characters and words
    if strength == 1:
        # if characters (strength 2-5), simply join into a string
        return "-".join(raw)
    else:
        # words, join with a hyphen
        return "".join(raw)


# ask the user for password specifiactions
spec = get_input()

# create a pool of characters
pool = make_char_set(spec[1])

# generate a new password based on the use spec
new_pasword = gen_pwd(spec[0], spec[1], pool)
print(f'Your new password is: {new_pasword}')

# breathing room for display
print()
