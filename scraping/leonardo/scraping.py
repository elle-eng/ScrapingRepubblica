from playwright.sync_api import sync_playwright

url = "https://www.leonardo.com/it/media-hub/news-stories?_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_formDate=1756653175484&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_filterDateTo=31.08.2025&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_filterTypeCategories=16624027%2C16624028&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_filterDateFrom=01.01.2020&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_dataFilterTypeReq=Year&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_page=1"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)

    page = 1
    pages = 1

    try:
        page.wait_for_selector('div.journal-content-article')
        pages = page.query_selector_all('div.leo-pagination--item a.leo-pagination--item--link')[-2].inner_text()
        print('pages:',pages)
    except:
        print("selettore 'div.journal-content-article' non trovato.")

    contenuti = page.query_selector_all('div.news-stories-card')

    urls = [c.query_selector('a').get_attribute('href') for c in contenuti]
    print(urls)



    