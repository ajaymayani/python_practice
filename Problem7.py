def matchingWord(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    sentences = ['This is good', 'Python is good', 'Python is not a python snake']

    query_string = input("Please input your query string : \n")
    scores = [matchingWord(query_string, sentence) for sentence in sentences]
    sortedSenScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore[0] != 0]
    print(f"{len(sortedSenScore)} results found")
    for score, item in sortedSenScore:
        print(item)
