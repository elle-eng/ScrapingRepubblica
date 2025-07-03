from playwright.sync_api import sync_playwright, Error
from xml_utils import save_article_in_xml

def scraping_articolo_digitale(page):
    article = {
        "type": "digitale"
    }

    if page.query_selector('h1.story__title'):
        article["title"] = page.locator('h1.story__title').text_content()
    else:
        article["title"] = ""

    if page.query_selector('.story__summary p'):
        article["subtitle"] = page.locator('.story__summary p').first.text_content()
    else:
        article["subtitle"] = ""

    if page.query_selector('em.story__author'):
        article["author"] = page.locator('em.story__author').first.text_content()
    else:
        article["author"] = ""

    if page.query_selector('div time.story__date'):
        article["date"] = " ".join(page.locator('div time.story__date').text_content().split(' ')[:3])
    else:
        article["date"] = ""

    if page.query_selector('div.story__text'):
        article["content"] = page.locator('div.story__text').first.text_content()
    else:
        article["content"] = ""

    save_article_in_xml(article)

def scraping_articolo_cartaceo(page):
    article = {
        "type": "cartaceo"
    }

    article["title"] = page.locator('h1').first.text_content()
    article["subtitle"] = ""
    article["author"] = ""

    if page.query_selector('article .edizione'):
        article["date"] = page.locator('article .edizione').text_content().split(',')[0]
    else:
        article["date"] = ""

    paragraphs = []
    for p in page.query_selector_all('article p'):
        paragraph = p.text_content().strip()
        if paragraph:
            paragraphs.append(paragraph)
       
    print('paragraphs',paragraphs)

    article["content"] = "\n\n".join(paragraphs)

    save_article_in_xml(article)

link_ricerca = "https://ricerca.repubblica.it/ricerca/repubblica?query=climatico+climatica&fromdate=2020-01-01&todate=2025-06-29&sortby=score&author=&mode=any"
email_google = 'elena.zanet@uniupo.it'
pass_google = 'GiuniRusso_2024'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://ricerca.repubblica.it/ricerca/repubblica")

    #google login
    page.wait_for_selector("#iub_cmp_subscribe_custom_btn")
    page.click("#iub_cmp_subscribe_custom_btn")

    with context.expect_page() as google_popup_info:
        page.click("#Google_btn")

    google_popup = google_popup_info.value
    google_popup.fill('input[type="email"]',email_google)
    google_popup.click("text='Avanti'")
    google_popup.fill('input[type="password"]',pass_google)
    google_popup.click("text='Avanti'")

    page.wait_for_selector(".iubenda-cs-accept-btn")
    page.click('.iubenda-cs-accept-btn')
    
    page.wait_for_selector("text='Continua senza accettare'")
    page.click("text='Continua senza accettare'")

    page.goto(link_ricerca)

    pages  = int(page.locator('.pagination p').text_content().split(' ')[-1])
    for page_num in range(pages):
        page.goto(link_ricerca + '&page=' + str(page_num+1))

        page.wait_for_selector('section#lista-risultati article h1 a')
        links = page.locator('section#lista-risultati article h1 a')
        hrefs = links.evaluate_all("links => links.map(link => link.href)")
        # print('page:',page_num,'- hrefs:',len(hrefs))

        for href in hrefs:
            try:
                page.goto(href)
                isDigitale = page.locator('main article.story').count() > 0
                isCartaceo = page.locator('body.premium-template').count() > 0
                
                if isDigitale:
                    scraping_articolo_digitale(page)
                    print('articolo digitale')
                elif isCartaceo:
                    scraping_articolo_cartaceo(page)
                    print('articolo cartaceo')
                else:
                    print('altro tipo di articolo')
            except Error as e:
                print("Errore di playwright su ", href, "-", e)
            finally:
                page.go_back()

    while True:
        pass


