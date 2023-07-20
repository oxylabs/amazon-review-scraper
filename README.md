# Amazon Review Scraper

Amazon Review Scraper is designed to extract localized Amazon ratings
and reviews in real-time without a hitch. This quick guide will walk you
through the process of scraping Amazon reviews using Oxylabs' Scraper
API.

## How it works

You can retrieve Amazon reviews by providing the **ASIN** number to our
service. Our API will return the results in **JSON** or **HTML** format.

### Python code example

The following example showcases how you can make a request to retrieve
product reviews for ASIN **B08238V32L** on the `amazon.nl` marketplace:

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_reviews',
    'domain': 'nl',
    'query': 'B08238V32L',
    'parse': True,
}


# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())

```

See code examples for other programming languages
[<u>here</u>](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/reviews#code-examples).

### Output Example

```json
{
  "results": [
    {
      "content": {
        "asin": "B08238V32L",
        "asin_in_url": "B08238V32L",
        "page": 1,
        "page_type": "Question",
        "pages": 1,
        "parse_status_code": 12000,
        "product_name": "VASAGLE bureau, computer bureau, 100 x 50 x 75 cm, eenvoudige constructie, industriële vormgeving, vintage bruin-zwart LWD41X",
        "reviews": [
          {
            "author": "jack ouwehand",
            "content": "de levering was eerder dan gepland ,dat was prettig.. Het wordt gebruikt als computertafel",
            "id": "R238HIUHAN7PFT",
            "is_verified": "True",
            "product_attributes": "Maat: 100 x 50 x 75 cmKleur: Honingbruin + Zwart",
            "rating": 4,
            "timestamp": "Beoordeeld in Nederland 🇳🇱 op 20 juni 2023",
            "title": "4,0 van 5 sterren dat het product eenvoudig met de gebruiksaanwijzing in elkaar kon worden gezet."
          },
          ...
          {
            "author": "mstf",
            "content": "A really solid table, I definitely recommend it, I bought this table as a result of my long research.",
            "id": "R13WDAOIY4YVXJ",
            "is_verified": "True",
            "product_attributes": "",
            "rating": 5,
            "timestamp": "Beoordeeld in Nederland 🇳🇱 op 5 mei 2022",
            "title": "5,0 van 5 sterren i think best price performance table"
          }
        ],
        "url": "https://www.amazon.nl/product-reviews/B08238V32L?reviewerType=all_reviews&pageNumber=1"
      },
      "created_at": "2023-07-19 14:04:35",
      "job_id": "7087432033898598401",
      "page": 1,
      "parser_type": "",
      "status_code": 200,
      "updated_at": "2023-07-19 14:04:38",
      "url": "https://www.amazon.nl/product-reviews/B08238V32L?reviewerType=all_reviews&pageNumber=1"
    }
  ]
}
```

Oxylabs’ Amazon Review Scraper will easily streamline your public data
extraction efforts. Get hassle-free access to Amazon review data, such
as rating scores, review titles and descriptions, author names, review
dates, and more.

You’ll also get access to a complete Amazon Scraper, so feel free to
check out [<u>this in-depth guide</u>](https://github.com/oxylabs/amazon-scraper) for more
information. In case you have any questions or need assistance, contact
our 24/7 support team via live chat or [<u>email</u>](mailto:support@oxylabs.io).
