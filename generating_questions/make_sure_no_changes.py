import json
import pdb

def main():
    """
    Make sure that chatgpt didn't fudge up the questions when filling them out
    """
    adulturated_questions = []
    # Load the original and filled questions
    with open('questions_unready.json', 'r') as originals_file:
        originals = json.load(originals_file)
    
    with open('./questions_chatgpt_filled.json', 'r') as filled_file:
        filled = json.load(filled_file)

    text_2_index = {originals[i]['text']:i for i in range(len(originals))}

    for q in filled:
        if q['text'] not in text_2_index:
            adulturated_questions.append({'question':q,'adulturations':['text']})
        else: 
            idx = text_2_index[q['text']]
            original_q = originals[idx]
            adulturations = []
            for key in original_q.keys():
                if original_q[key] != q[key]:
                    adulturations.append(key)
            if len(adulturations) > 0:
                adulturated_questions.append({'question':q,'adulturations':adulturations})
    print(json.dumps(adulturated_questions,indent=1))
if __name__ == "__main__":
    main()

