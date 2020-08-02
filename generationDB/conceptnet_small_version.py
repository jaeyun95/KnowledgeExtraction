import csv
from pymongo import MongoClient
import re
import json
client = MongoClient('localhost',27017)
db = client.conceptnet5
collections = db.conceptnet5_small_version

check_list = []
concepts = []

with open('keyword.json','r',encoding="UTF8") as f:
    keyword_list = [json.loads(s) for s in f]
    keywords = keyword_list[0]['keyword']

with open('conceptnet/conceptnet.json','r',encoding="UTF8") as f:
    concept_list = [json.loads(s) for s in f]

keywords = [keyword for keyword in keywords if not keyword.isdigit() and len(keyword)>3]
keywords += ['up','go','pro','pap','tip','vow','bmw','gps','aim','fur','may','out','guy','bro','log','ben','cal','dis','hew','jot','lid','fox','awl','sin','law','ask','gin','bun','hop','dam','ems','ton','shy','vex','cop','pay','ego','jaw','tho','low','jug','gee','cue','inn','tux','age','bog','car','den','put','doc','que','owe','tie','fun','ron','sow','nag','gun','tow','sue','soy','abs','cog','run','rag','ans','bot','rat','eye','spa','dip','cob','jab','mud','hog','cab','wry','ufc','con','mob','hut','sit','icy','tub','rum','hos','din','gui','cod','hoe','lie','flu','dim','sob','pig','wax','wet','yen','pot','new','foe','eve','vet','fro','owl','job','hem','bet','lot','mad','pug','bar','fib','tab','rug','tea','wit','lop','hue','oak','lei','sen','rad','rig','ooh','eon','van','wow','due','ave','ago','say','ken','cow','ceo','pin','ale','dig','men','lob','bee','bib','bow','egg','kid','lax','hit','fix','red','yet','lag','far','man','ope','toe','hen','pub','wad','fly','pus','tit','hug','spy','toy','jay','aye','mod','mis','fez','sex','bag','duo','pen','pal','tel','hay','ids','dun','dye','wag','set','pad','zip','one','pit','six','jog','jut','max','bus','fax','moo','key','bat','gum','big','opt','pas','era','mat','use','coy','yea','bbq','lap','tag','ost','ufo','vip','lug','fin','sir','rub','nap','dna','kit','mom','mop','sly','boo','neo','god','bon','mac','com','peg','dan','caw','med','obi','hub','ail','pep','dad','rib','via','own','pat','inc','gut','bin','lad','fry','tad','beg','pip','die','air','ten','gon','chi','rip','jam','ram','nod','dub','cat','oil','sap','per','fat','maw','joy','pop','orb','gas','gel','urn','rev','bad','fit','sky','cps','ted','sox','non','bur','hey','woo','bey','win','hip','tug','doz','sop','bra','nsa','ion','rep','gem','ons','hag','par','act','apt','oar','gap','nay','hum','mow','gay','pee','hep','let','rim','lip','war','cub','nun','haw','get','pax','bud','arc','gig','usa','son','tom','tap','sun','fir','tic','rod','aha','bis','gab','etc','kfc','rid','ski','sag','ref','tin','doe','pie','dvd','boy','rpg','git','cam','odd','goo','ash','end','bay','saw','las','fee','way','wig','foo','ant','pod','ocd','old','ink','rot','rap','cry','nog','hot','dry','chu','top','sum','shh','cpu','day','sub','nab','jet','tan','keg','jag','box','vat','fan','two','pry','try','ssh','hod','yin','zap','mar','tee','tob','cot','mid','pew','bid','tun','nut','map','pac','cap','ear','mix','lay','ned','bod','fog','ads','sup','jig','nit','huh','lab','ham','ray','pan','fag','jew','sci','viz','add','row','net','tar','app','hap','sea','ban','aka','web','vcr','var','fer','wan','ply','bio','bed','bye','mot','dot','ops','leg','rob','bob','don','see','buy','mas','wok','raw','vas','arm','bum','wed','cup','rec','bop','gag','sip','jar','fob','mvp','ape','elf','awe','dab','hat','paw','kin','aid','sad','sew','zoo','pos','pet','atm','bug','vie','art','sty','ark','gat','mao','boa','eat','tax','mug','gym','can','rem','dog','cut','off']
pre_len = len(concept_list)
k = 0
count = 0
for concept in concept_list:
    del concept['_id']
    start = concept['e1']
    end = concept['e1']
    for keyword in keywords:
        #print(keyword)
        if keyword in start or keyword in end:
            if concept['text'] not in check_list:
                check_list.append(concept['text'])
                count += 1
                collections.insert(concept)
    k += 1
    print('now : ',k)
print('pre_len : ',pre_len)
print('after_len : ',count)