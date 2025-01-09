import requests
from bs4 import BeautifulSoup

def search_storygraph_by_isbn(isbn):
    """
    Search TheStoryGraph for their unique book ID using an ISBN.
    Input is ISBN, returns the unique book ID if found, otherwise None.
    """
    url = f"https://app.thestorygraph.com/browse?search_term={isbn}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        book_link = soup.find("a", href=lambda href: href and "/books/" in href)
        if book_link:
            # Extract the book ID from the href
            book_id = book_link["href"].split("/books/")[-1]
            return book_id
        
    else:
        print("Failed to fetch data from StoryGraph")
        return None


    return None
