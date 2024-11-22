from transformers import pipeline
import time


def compute_negativity(L):
    '''
    Return the ESG score of a company : negative scores are bad, positive score are good
    input : L, a list of strings
    output : a list of tuple (negative/positive/neutral,score)
    '''
    pipe = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
    results = pipe(L)

    scores = []
    for result in results:
        if result['label']=='positive':
            scores.append(result['score'])
        elif result['label']=='negative':
            scores.append(-1*result['score'])
        else:
            scores.append(0)    # neutral score

    return(scores)

def compute_ESG_bool(L):
    '''
    Return if the text is related to ESG or not
    input : a list of strings
    output : a list of TRUE/FALSE, TRUE if the text is ESG related, FALSE if it is not
    '''
    pipe = pipeline("text-classification", model="yiyanghkust/finbert-esg")
    results = pipe(L)
    scores = []

    for result in results:
        if result['label']=='None':
            scores.append(False)
        else:
            scores.append(True)
    return(scores)

def compute_ratings(L):
    '''
    compute the esg ratings of a list, as they are used in the app
    '''
    esg_bool = compute_ESG_bool(L)
    usefull_texts = [L[k] for k in range(len(L)) if esg_bool[k]]
    print("esg_bool",esg_bool)
    print("usefull_texts=",usefull_texts,len(usefull_texts))
    scored_texts = compute_negativity(usefull_texts)
    print("ici",scored_texts)
    scores = []
    for k in range(len(L)):
        if esg_bool[k]==False:
            scores.append(0)
        else:
            print("scores_texts=",scored_texts)
            scores.append(scored_texts[0])
            scored_texts = scored_texts[1:]
    return(scores)

# pipe_esg = pipeline("text-classification", model="yiyanghkust/finbert-esg")
# pipe_sentiment = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")

# texts = ["j'aime les pates","kill all jews","je sauve les animaux et je plante des arbres","Je suis fatigué"]
# start = time.time()
# print(compute_ratings(texts))
# print(pipe_esg(texts))
# print(pipe_sentiment(texts))
# print(time.time()-start)
