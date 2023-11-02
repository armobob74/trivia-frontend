import json
import random
from get_unfilled_questions import getUnfilledQuestions

with open('./questions_ready.json') as f:
    questions_ready = json.load(f)

# this function finds only the questions that have not been filled by chatgpt
questions_unready = getUnfilledQuestions()

# filter out any unfilled questions that have no answers
questions_unready = [q for q in questions_unready if 'correct' in q]

sample_ready = random.sample(questions_ready, 3)
sample_unready = questions_unready[:20]

text_ready = json.dumps(sample_ready, indent=1)
text_unready = json.dumps(sample_unready, indent=1)

prompt = f"""I am working on a database of trivia questions. I have a large number of question/answer pairs, but I need to generate alternative answers as well. I want the questions to look like this when done:
{text_ready}

Here are my unfinished questions:
{text_unready}
Please fill out the alternate answers for each unfinished question, changing NOTHING ELSE."""
print(prompt)

