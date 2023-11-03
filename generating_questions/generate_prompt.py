import json
import pdb
import random
from get_unfilled_questions import getUnfilledQuestions

with open('./questions_ready.json') as f:
    questions_ready = json.load(f)

with open('./categories.json') as f:
    categories = json.load(f)
    

# this function finds only the questions that have not been filled by chatgpt
questions_unready = getUnfilledQuestions()

# filter out any unfilled questions that have no answers
questions_unready = [q for q in questions_unready if 'correct' in q]

sample_ready = random.sample(questions_ready, 3)
sample_unready = questions_unready[:20]

text_ready = json.dumps(sample_ready, indent=1)
text_unready = json.dumps(sample_unready, indent=1)

prompt = f"""I am working on a database of trivia questions. I have a large number of question/answer pairs, but I need you to add some information.

Here are my unfinished questions:
{text_unready}

They are meant to be multiple choice, with answers A-D. Please add in the missing answers, and then add a categories field with a list of appropriate categories for the question.

Here is the list of categories:
{categories}

Change NOTHING ELSE."""
print(prompt)

