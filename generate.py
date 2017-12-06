import re
import json
from watson_developer_cloud import ToneAnalyzerV3
 
def analyze_tone():
    un = 'username'
    pw = 'password'
    v = '2017-09-21'
    data = input("Enter some text to be converted:\n")
    if len(data) < 1:
        return 'Empty'
    try:
        analyze = ToneAnalyzerV3(username = un, password = pw, version = v)
        result = json.dumps(analyze.tone(data, 'text/plain'))
        return result
    except:
        return 'Failed'
    
def get_data(text): #return a hashmap of tones and scores
    score_index = [m.start() for m in re.finditer('score', text)]
    tone_index = [m.start() for m in re.finditer('tone_id', text)]
    scores = []
    tones = []
    for i in score_index:
        scores.append(text[i+8:i+16])
    for i in tone_index:
        j = text.find('"', i+11)
        tones.append(text[i+11:j])
    data = dict(zip(tones, scores))
    return data

#def emojize(values): #takes in list of tuples
    
    
def main():
    data = analyze_tone()
    if data == 'Empty':
        print('Nothing to convert.')
        exit
    elif data == 'Failed':
        print('We\'re having technical difficulties...')
        exit
    print(get_data(data))

main()
