from playwright.sync_api import sync_playwright
import time 

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
        print('page:',page_num,'- hrefs:',len(hrefs))
        
        for href in hrefs:
            page.goto(href)
            
            page.go_back()

    while True:
        pass


