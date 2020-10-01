from collections import Counter
import re
import pandas as pd

NUM_OF_SPEAKERS_RU = 5
NUM_OF_SPEAKERS_HE = 7
NUM_OF_SPEAKERS_KR = 1

def add_mock_speaker(df):
    df['sp_mock'] = ''
    clips = df.pop('clip')
    for i, row in enumerate(df.iterrows()):
        new_row = row[1].str.strip().str.replace('\\', '/')
        for j, options in enumerate(row[1].str.split('/')):
            if len(options) > 1:
                new_row[j] = options[0]
                new_row['sp_mock'] = options[1]
            else:
                new_row['sp_mock'] = Counter(new_row).most_common()[0][0]
        df.iloc[i] = new_row
    df.insert(loc=0, column='clip', value=clips)
    return df

def extract_affixes_ru(df):
    df['prefixes'] = ''
    reflexive_suf = 'ся'
    prefixes = ['раз',
                'рас',
                'об',
                'от',
                'по',
                'над',
                'на',
                'вы',
                'с',
                'о',
                'про',
                'при']
    clips = df.pop('clip')
    for row in df.iterrows():
        for j, verb in enumerate(row[1][:-1]):
            if verb.endswith(reflexive_suf): # remove reflexive suffix
                verb = verb[:-2]
            for prefix in prefixes:
                if verb.startswith(prefix):
                    verb = verb[len(prefix):] # remove prefix
                    prefix = 'раз' if prefix == 'рас' else prefix
                    df.iloc[row[0]]['prefixes'] += prefix + ','
                    if verb.startswith('о') or verb.startswith('ъ'):
                        verb = verb[1:] # remove intermediate o if presents
                    break
            df.iloc[row[0], j] = verb # update processed verb
    df.insert(loc=0, column='clip', value=clips)
    return df

def preprocess_russian():
    df = pd.read_excel(f'../data/cb_russian.xlsx')
    df.drop(['Description', 'Note'], axis=1, inplace=True)

    # dealing with multiple values

    df = add_mock_speaker(df)

    # remove reflexive suffix, extract prefixes, clean them from the stems

    df = extract_affixes_ru(df)

    return df

def extract_root_he(verb):
    if verb == 'להכות': # להכות
        return verb
    elif re.fullmatch(r'ל..ו.', verb): # פעל
        return verb[1] + verb[2] + verb[4]
    elif re.fullmatch(r'לה..י.', verb): # הפעיל
        if(verb[2] == 'ו'): # להוריד
            return 'י' + verb[-3] + verb[-1]
        else:
            return verb[-4] + verb[-3] + verb[-1]
    elif re.fullmatch(r'לה.י.', verb): # להסיר
        return verb[-3:]
    elif re.fullmatch(r'להי?ת.?...', verb): # התפעל
        return verb[verb.find('ת') + 1] +  verb[-2:]
    elif re.fullmatch(r'להי?.ת..', verb): # להשתמש
        return verb[verb.find('ת') - 1] +  verb[-2:]
    elif re.fullmatch(r'להי?...?.', verb): # נפעל
        if verb[-4] not in ['ה', 'י']: # להשפשף
            return verb[-4:]
        else:
            return verb[-3:]
    elif re.fullmatch(r'ל.ו?..', verb): # פיעל
        if('ו' in verb):
            return verb[1] + verb[-2:]
        else:
            return verb[1:]
    elif re.fullmatch(r'ל....', verb): # לקמפל
        return verb[1:]
    else:
        return verb

def extract_roots(df):
    clips = df.pop('clip')
    for row in df.iterrows():
        df.iloc[row[0]] = row[1].apply(lambda x: extract_root_he(x))
    df.insert(loc=0, column='clip', value=clips)
    return df

def preprocess_hebrew():
    df = pd.read_excel(f'../data/cb_hebrew.xlsx')

    df.drop(['Description', 'Note', 'Sp7'], axis=1, inplace=True) # sp7 = sp5

    df.rename(columns={"Sp1": "sp1",
                       "Sp2": "sp2",
                       "Sp3": "sp3",
                       "Sp4": "sp4",
                       "Sp5": "sp5",
                       "Sp6": "sp6"}, inplace=True)

    # cleaning transcriptions of the second speaker

    df['sp2'] = df['sp2'].str.split('-').apply(lambda x: x[0])

    # dealing with multiple values

    df = add_mock_speaker(df)

    # extracting roots

    df = extract_roots(df)

    return df

def preprocess_korean():
    df = pd.read_excel(f'../data/cb_korean.xlsx')
    df.drop(['transcription'], axis=1, inplace=True)
    return df

def encode_clip_by_prefixes_ru(df):
    prefixes_set = set()
    df['prefixes'].apply(lambda x: prefixes_set.update(set(x.split(',')[:-1]))) # construct a set of prefixes
    encoded_df = pd.DataFrame()
    for prefix in list(prefixes_set):
        encoded_df[prefix] = df['prefixes'].apply(lambda x: x.count(prefix) / NUM_OF_SPEAKERS_RU)
    return encoded_df.set_index(df['clip'])#.to_numpy() # todo or fit the df directly

def encode_clip_by_verb(df):
    df_verbs = df.loc[:, df.columns != 'clip']
    verbs_set = set(df_verbs.stack().array) # extract the vocabulary
    verbs = list(verbs_set)
    encoded_df = pd.DataFrame(columns=verbs)
    for row in df_verbs.iterrows():
        encoded_df = encoded_df.append(Counter(row[1]), ignore_index=True)
    encoded_df = encoded_df.fillna(0).div(encoded_df.sum(axis=1), axis=0)
    return encoded_df.set_index(df['clip'])#.to_numpy() # todo or fit the df directly

def encode_russian():
    russian_df = preprocess_russian()
    clip_by_prefix = encode_clip_by_prefixes_ru(russian_df[['clip', 'prefixes']])
    clip_by_verb = encode_clip_by_verb(russian_df.loc[:, russian_df.columns != 'prefixes'])
    return clip_by_prefix, clip_by_verb

def encode_hebrew():
    hebrew_df = preprocess_hebrew()
    clip_by_verb = encode_clip_by_verb(hebrew_df)
    return clip_by_verb

def encode_korean():
    korean_df = preprocess_korean()
    clip_by_verb = encode_clip_by_verb(korean_df)
    return clip_by_verb

if __name__ == '__main__':
    r = encode_russian()
    h = encode_hebrew()
    k = encode_korean()
