"""
    Pydantic models for Amazon Review scraper.
"""

from pydantic import BaseModel


class Review(BaseModel):
    author: str
    content: str
    rating: int
    title: str
