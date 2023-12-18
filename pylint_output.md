(venv) yahoo@enine027:~/newDay4/math-004-e9kwagh$ pylint solver.py
************* Module solver
solver.py:3:21: C0303: Trailing whitespace (trailing-whitespace)
solver.py:18:34: C0303: Trailing whitespace (trailing-whitespace)

------------------------------------------------------------------
Your code has been rated at 8.89/10 (previous run: 8.89/10, +0.00)

(venv) yahoo@enine027:~/newDay4/math-004-e9kwagh$ pylint answer.py
************* Module answer
answer.py:14:0: C0301: Line too long (110/100) (line-too-long)
answer.py:1:0: C0114: Missing module docstring (missing-module-docstring)
answer.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.12/10 (previous run: 8.12/10, +0.00)

(venv) yahoo@enine027:~/newDay4/math-004-e9kwagh$ git add .
(venv) yahoo@enine027:~/newDay4/math-004-e9kwagh$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   answer.py
	new file:   answer_test.py
	new file:   solver.py
	new file:   solver_test.py
