"""
Find out which of the questions have been filled out by chatgpt and which are still not ready
"""
import json

def getUnfilledQuestions():
    with open('questions_chatgpt_filled.json') as f:
        questions_filled = json.load(f)
    with open('questions_unready.json') as f:
        questions_raw = json.load(f)

    filled_text_fields = {d['text'] for d in questions_filled}
    raw_text_fields = {d['text'] for d in questions_raw}

    unfilled_text_fields = raw_text_fields - filled_text_fields

    ret = [q for q in questions_raw if q['text'] in unfilled_text_fields]
    return ret

if __name__ == "__main__":
    unfilled_questions = getUnfilledQuestions()
    print(unfilled_questions)
