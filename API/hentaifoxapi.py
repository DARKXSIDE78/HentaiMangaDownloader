from bs4 import BeautifulSoup
import requests

class hentaifoxapi():  
    def __init__(self, code):
        self.code = code

    def get_chapter_by_code(code):  # Returns list of image links of pages of the full chapter [imglink1, imglink2, ...]
        url = f"https://hentaifox.com/g/{code}/1"  # Base URL for the chapter
        response = requests.get(url)
        if response.status_code != 200:  # Handle HTTP errors
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return []
        response_html = response.text
        soup = BeautifulSoup(response_html, 'lxml')
        page_count_tag = soup.find("span", class_="total_pages")
        if page_count_tag:
            page_count = int(page_count_tag.text.strip())  # Extract page count
        else:
            print("Couldn't find page count.")
            return []
        list_of_pages = []
        for i in range(1, page_count + 1):
            img_tag = soup.find("img", class_="lazy")
            if not img_tag or 'data-src' not in img_tag.attrs:
                print("Couldn't find image link on page", i)
                continue
            img_url = img_tag['data-src']  # Lazy-loaded image URL
            list_of_pages.append(img_url)
            next_page_url = f"https://hentaifox.com/g/{code}/{i+1}"
            response = requests.get(next_page_url)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'lxml')
        return list_of_pages
