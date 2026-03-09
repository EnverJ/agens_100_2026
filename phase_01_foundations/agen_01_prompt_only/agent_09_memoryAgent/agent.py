store = "store"
ignore = "ignore"
project_info = ['system', 'agent complete', 'architecture']
trivial_info= ['hi','how are you', 'greeting']
def storageDecision(userInput):
    input_normalization= userInput.lower()
    isImportant = any(phrase.lower() in input_normalization for phrase in project_info)
    isTrivial = any (phrase.lower() in input_normalization for phrase in trivial_info)
    if(isImportant):
        return store
    elif (isTrivial):
        return ignore
    else:
        return ignore

decision_info = ['system', 'agent complete', 'architecture']
retrieve = 'retrieve' 
not_retrieve = 'non_retrieve'  
def retrievalDecision(userInput):
    decision_normalization = userInput.lower()
    isRetrieve = any (phrase.lower() in decision_normalization for phrase in decision_info)
    if (isRetrieve):
        return retrieve
    else :
        return not_retrieve