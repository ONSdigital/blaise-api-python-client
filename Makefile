.PHONY: show-help
## This help screen
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)";echo;sed -ne"/^## /{h;s/.*//;:d" -e"H;n;s/^## //;td" -e"s/:.*//;G;s/\\n## /---/;s/\\n/ /g;p;}" ${MAKEFILE_LIST}|LC_ALL='C' sort -f|awk -F --- -v n=$$(tput cols) -v i=29 -v a="$$(tput setaf 6)" -v z="$$(tput sgr0)" '{printf"%s%*s%s ",a,-i,$$1,z;m=split($$2,w," ");l=n-i;for(j=1;j<=m;j++){l-=length(w[j])+1;if(l<= 0){l=n-i-length(w[j])-1;printf"\n%*s ",-i," ";}printf"%s ",w[j];}printf"\n";}'

.PHONY: format
## Format python
format:
	@poetry run black .
	@poetry run isort .

.PHONY: lint
## Run styling checks for python
lint:
	@poetry run black --check .
	@poetry run isort --check .
	@poetry run flake8 --max-line-length=120 --exclude=tests .
	@poetry run mypy .

.PHONY: test
## Run unit tests
test:
	@poetry run python -m pytest
