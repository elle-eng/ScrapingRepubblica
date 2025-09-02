from playwright.sync_api import sync_playwright

website = 'https://www.eni.com/'

def scraping_section_details(page):
    titolo = page.query_selector('h1').inner_text()
    print(titolo)
    pass

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    base_url = f'{website}it-IT/media/comunicati-stampa.html?data-date-from=1577833200&data-date-to=1756850399&'
    url = base_url + 'page=0'
    page.goto(url)

    page.wait_for_selector('ul.pagination li.page-item')
    pages = int(page.query_selector_all('ul.pagination li.page-item')[-2].inner_text())
    print('pages:',pages)
    page.close()

    for page_num in range(pages):
        page = context.new_page()
        url = base_url + f'page={page_num}'
        page.goto(url)

        page.wait_for_selector('a.container-card')
        contents = page.query_selector_all('a.container-card')
        
        urls = [node.get_attribute('href') for node in contents]
    
        for url in urls:
            full_url = website + url
            print('page:',page_num,'url:',full_url)
            page.goto(full_url)
            scraping_section_details(page)
        page.close()

        