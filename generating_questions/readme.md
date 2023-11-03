### This Directory Contains
scripts to help with asking chatgpt to fill out a questions database

generate\_prompt.py will generate a prompt for chatgpt
the generated responses must be stored in questions\_chatgpt\_filled.json, but not removed from the original list.

`make_sure_no_changes.py` will double-check chatgpt's work.
It's ok for very minor adulturations to exist, as long as it's nothing that changes the meaning of the question.
