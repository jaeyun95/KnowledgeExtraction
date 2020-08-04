## This is knowledge extraction system


# extractKeyword
I use nltk library for extracting keyword.
```
*class
    extractionKeyword
*function
    _remove_stopword : remove unused keyword. (ex. how, why, what, ... )
    _prototype : find prototype word. (ex. running -> run)
    get_keyword : we use this function. First, remove unused keyword, Second, find prototype.
*usage
    extract = extractionKeyword()
    example_sentence = ["What","is","your","name","?"]
    result = extract.get_keyword(example_sentence)
```

# extractionKnowledge
I use mongoDB or json file for extraction knowledge.
```
*class
    extractionKnowledge
*funcrtion
    get_knowledge : find knowledge in MongoDB
*usage
    extract = extractionKnowledge(number, max_len) #number is knowledge number, max_len is knowledge sentence length
    example_keyword = ["cute","sister","dog"]
    result = extract.get_knowledge(example_keyword)
```

