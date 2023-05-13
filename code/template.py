PROMPT_DICT = {
    "ag_news": (
        "A chat between a curious user and an artificial intelligence assistant. "
        "The assistant gives correctly answers to the user's questions. "
        "USER: {inputs}"
        "Which of the following options of a newspaper would this article likely appear in?\nA. World News\nB. Sports\nC. Business\nD. Science and Technology.\nI don't want any other words. "
        "ASSISTANT:"
    ),
    "imdb": (
        "A chat between a curious user and an artificial intelligence assistant. "
        "The assistant gives correctly answers to the user's questions. "
        "USER: {inputs}"
        "How does the you feel about the movie?\n A. positive\nB. negtive\nI don't want any other words. "
        "ASSISTANT:"
    ),
    "imdb_new": (
        "A chat between a curious user and an artificial intelligence assistant. "
        "The assistant gives correctly answers to the user's questions. "
        "USER: {inputs}"
        "Did the reviewer find this movie good or bad. "
        "ASSISTANT:"
    )
}

ANSWER_DICT = {
    "ag_news": {
        0 : "World News",
        1 : "Sports",
        2 : "Business",
        3 : "Science and Technology",
    },
    "imdb" : {
        0 : "Neg",
        1 : "Pos",
    },
    "imdb_new" : {
        0 : "bad",
        1 : "good",
    }
}

def Inputs_2_Instrcution(Inputs, dataset_ids):
    prompt_input = PROMPT_DICT[dataset_ids]
    return prompt_input.format(inputs = Inputs)

def Number_2_Word(Number, dataset_ids):
    prompt_output = ANSWER_DICT[dataset_ids]
    return prompt_output[Number]

if __name__=="__main__":
    example = {
    "inputs" : "Stocks Higher on Drop in Jobless Claims A sharp drop in initial unemployment claims and bullish forecasts from Nokia and Texas Instruments sent stocks slightly higher in early trading Thursday. "
    }

    inputs = example["inputs"]
    print(Inputs_2_Instrcution(inputs, "AG_News"))
    print(type(Inputs_2_Instrcution(inputs, "AG_News")))