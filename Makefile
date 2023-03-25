initialize_git:
	@echo "initialization ..."
	git init 
	sleep 2
	git add . 
	sleep 2
	git commit -m "My first commit"
	sleep 2
	git branch -M main 
	sleep 2
	git remote add origin https://github.com/EDJINEDJA/City-.git
	sleep 2
	git push -u origin main

pushing:
	@echo "pushing ..."
	git add . 
	git commit -m $(COMMIT)
	git push -u origin main

pulling:
	@echo "pulling ..."
	git pull origin main

env: 
	@echo "env initialization ..."
	pipenv install
	pipenv run pre-commit install

run:
	python app.py

setup: initialize_git env


