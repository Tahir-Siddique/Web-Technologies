import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_topics():
    """
    Returns a list of all names of course topics topics.
    """
    _, filenames = default_storage.listdir("topics")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_topics(title, content):
    """
    Saves a course topics topics, given its title and Markdown
    content. If an existing topics with the same title already exists,
    it is replaced.
    """
    filename = f"topics/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_topics(title):
    """
    Retrieves a course topics topics by its title. If no such
    topics exists, the function returns None.
    """
    try:
        f = default_storage.open(f"topics/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
