"""
    Main module for collecting Amazon Review data.
"""

import logging

from typing import List

import pandas as pd

from amazon_review_scraper.models import Review
from amazon_review_scraper.scraper import AmazonReviewScraper


DEFAULT_OUTPUT_FILE = "amazon_reviews.csv"


class AmazonReviewDataCollector:
    """Data collector class for Amazon Reviews"""

    def __init__(
        self,
        output_file: str | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._scraper = AmazonReviewScraper()
        self._output_file = output_file if output_file else DEFAULT_OUTPUT_FILE
        self._logger = logger if logger else logging.getLogger(__name__)

    def _save_to_csv(self, reviews: List[Review]) -> None:
        """Saves given list of product reviews to a CSV file."""
        self._logger.info(f"Writing {len(reviews)} reviews to {self._output_file}..")
        review_obejcts = [review.model_dump() for review in reviews]
        df = pd.DataFrame(review_obejcts)
        df.to_csv(self._output_file)

    def collect_amazon_review_data(self, asin_code: str) -> None:
        """
        Scrapes reviews from a given Amazon product page based on given ASIN code and stores it into a CSV file.

        Args:
            asin_code (str): The ASIN code of the Amazon product for which to scrape reviews.
        """
        self._logger.info(f"Getting Amazon reviews for ASIN code {asin_code}..")
        try:
            reviews = self._scraper.scrape_amazon_reviews(asin_code)
        except Exception:
            self._logger.exception(
                f"Error when scraping Amazon reviews for product {asin_code}."
            )
            return

        if not reviews:
            self._logger.info(f"No reviews found for given product {asin_code}.")
            return

        self._save_to_csv(reviews)
