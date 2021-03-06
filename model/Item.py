#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class Item:
    """Class for Hacker News item"""

    by: str
    descendants: int
    kids: [int]
    score: int
    time: int
    title: str
    item_type: str
    url: str
    parent: int
    text: str

    def __init__(
            self,
            by: str,
            descendants: int,
            kids: [int],
            score: int,
            time: int,
            title: str,
            item_type: str,
            url: str,
            parent: int,
            text: str,
    ):
        super().__init__()
        self.by = by
        self.descendants = descendants
        self.kids = kids
        self.score = score
        self.time = time
        self.title = title
        self.item_type = item_type
        self.url = url
        self.parent = parent
        self.text = text


def get_item_from_data(comment_data):
    my_item = Item(
        comment_data.get("by"),
        comment_data.get("descendants"),
        comment_data.get("kids"),
        comment_data.get("score"),
        comment_data.get("time"),
        comment_data.get("title"),
        comment_data.get("type"),
        comment_data.get("url"),
        comment_data.get("parent"),
        comment_data.get("text"),
    )
    return my_item
