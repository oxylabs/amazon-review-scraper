# Amazon Review Scraper

[![Amazon_scraper (1)](https://user-images.githubusercontent.com/129506779/249700804-abb11a97-9e0d-4f3c-bf2c-72991e8acd74.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=86)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

- [Amazon Review Scraper](#amazon-review-scraper)
    + [Free Amazon Scraper](#free-amazon-scraper)
    + [Prerequisites](#prerequisites)
    + [Installation](#installation)
    + [Retrieving the ASIN code of an Amazon product to scrape reviews from](#retrieving-the-asin-code-of-an-amazon-product-to-scrape-reviews-from)
    + [Scraping Amazon Review data](#scraping-amazon-review-data)
    + [Retrieved data](#retrieved-data)
    + [Notes](#notes)
- [Scraping Amazon with Oxylabs API](#scraping-amazon-with-oxylabs-api)
    + [Python code example](#python-code-example)
    + [Output Example](#output-example)

Amazon Review Scraper is designed to extract localized Amazon ratings and reviews in real-time without a hitch. In this guide, we'll demonstrate how to get this data for **free** on a small scale. If you need a bigger scale scraper, please refer to the 2nd part of the tutorial, where we'll scrape public Amazon data with Oxylabs API.

### Free Amazon Scraper

A free tool used to get Amazon review data for a provided Amazon product.

### Prerequisites

To run this tool, you need to have Python 3.11 installed in your system.

### Installation

Open up a terminal window, navigate to this repository and run this command:

```make install```

### Retrieving the ASIN code of an Amazon product to scrape reviews from

First off, open up a product you want to scrape reviews from in Amazon.

After the page has loaded, click on the URL of the page in your browser.

You should see something like this: `https://amazon.com/<product_info>/dp/<asin_code>`

For this example, let's take a cat bed from Amazon as a product.

The URL for this product looks like this: `https://www.amazon.com/Warming-Pets-Removable-Non-Slip-Washable/dp/B096S3QHWL`

<img width="1203" alt="image" src="https://github.com/user-attachments/assets/bf05be64-2ea4-464f-81a8-e62cc6262682">

Copy and save the ASIN code. We'll use it for scraping reviews for this product.

The ASIN code for this product is: `B096S3QHWL`. 

### Scraping Amazon Review data

To get reviews for a selected product, simply run this command in your terminal:

```make scrape ASIN_CODE="<your_selected_asin_code>"```

With the ASIN code we retrieved earlier, the command would look like this:

```make scrape ASIN_CODE="B096S3QHWL"```

Make sure to surround the code with quotation marks, otherwise the tool might have trouble parsing it.

After running the command, your terminal should look something like this:

<img width="741" alt="image" src="https://github.com/user-attachments/assets/ad46303b-c537-4b72-849a-c3770f94966a">

### Retrieved data

After the tool has finished running, you should see a file named `amazon_reviews.csv` in your directory.

The generated CSV file contains data with these columns inside it:

- `author` - The author of the review.
- `content` - The content of the review.
- `rating` - The rating for the product.
- `title` - The title of the review.

The data should look something like this:

<img width="960" alt="image" src="https://github.com/user-attachments/assets/a0bd8d85-c6be-4506-8ace-8a755e8c3702">

### Notes

In case the code doesn't work or your project is of bigger scale, please refer to the second part of the tutorial. There, we showcase how to scrape public data with Oxylabs Scraper API.

## Scraping Amazon with Oxylabs API

Now, we'll demonstrate how to scrape public Amazon review data with Oxylabs API. Bear in mind that you'll need an active subsciption to use this tool–you may get a free trial [here](https://dashboard.oxylabs.io/). 

You can retrieve Amazon reviews by providing the **ASIN** number to our service. Our API will return the results in **JSON** or **HTML** format.

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
Check out other tutorials on scraping Amazon data: [Amazon ASIN Scraper](https://github.com/oxylabs/amazon-asin-scraper), [Bypass Amazon CAPTCHA](https://github.com/oxylabs/how-to-bypass-amazon-captcha), [How to Scrape Amazon Prices](https://github.com/oxylabs/how-to-scrape-amazon-prices), [Scraping Amazon Product Data](https://github.com/oxylabs/how-to-scrape-amazon-product-data)
