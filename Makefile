# Makefile for running Amazon review scraper


.PHONY: install
install:
	pip install poetry==1.8.2
	poetry install


.PHONY: scrape
scrape:
	@if [ -z "$(ASIN_CODE)" ]; then \
		echo 'Error: An asin code of an Amazon product is required. Use make scrape ASIN_CODE="<asin_code>"'; \
		exit 1; \
	else \
		poetry run python -m amazon_review_scraper --asin-code="$(ASIN_CODE)"; \
	fi
