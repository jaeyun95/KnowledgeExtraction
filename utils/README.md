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
    _mongoDB : find knowledge in MongoDB.
    _hash_table : find knowledge in json using hash talbe.
    get_knowledge : choosing your version and extract knowledge.
*usage
    extract = extractionKnowledge(number, max_len) #number is knowledge number, max_len is knowledge sentence length
    example_keyword = ["cute","sister","dog"]
    result = extract.get_knowledge(example_keyword)
```

# topKknowledge
I use BERT embedding for compare sentence and knowledge and using cosine similarity.
```
*class
    BERTembedding
*funcrtion
    get_embedding : get bert embedding result. shape is [your knowledge length, 768]
*usage
    embedder = BERTembedding() #I use bert-base pretrained model
    example_knowledge = ["sister is a woman"]
    result = embedder.get_embedding(example_knowledge)
----------------------------------------------------------------------------------------------
*class
    topKknowledge --> **modifying now**
*funcrtion
    embedding : embedding compare sentence and knowledge together. shape is [max length, 768]
    cosineSimilarity : cosine smiliarity compare sentence and knowledge.
    get_topKknowledge : extract top K knowledge.
*usage
    extract = topKknowledge(number, knowledge_max_len) #number is meaning K
    example_compared_sentence = ["what is this?"]
    example_knowledge = [["sister is a woman"],["dog is cute"],...]
    result = extract.get_topKknowledge(example_compared_sentence, example_knowledge)
```
