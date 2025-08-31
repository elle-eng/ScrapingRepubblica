from scrap_utils_leonardo import scrap_section

#NOTIZIE
leonardo_news_selectors = {
    "subtitle":"div.internal-header--description",
    "date":"div.hero-slide--content--description",
    "content": "div.check-html-content"
}
# scrap_section(
#     "news"
#     "div.news-stories-card",
#     leonardo_news_selectors,
#     "scraping/leonardo/news",
#     "https://www.leonardo.com/it/media-hub/news-stories?_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_formDate=1756653175484&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_filterDateTo=31.08.2025&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_filterTypeCategories=16624027%2C16624028&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_filterDateFrom=01.01.2020&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_dataFilterTypeReq=Year"
# )

#STAMPA
leonardo_stampa_selectors = {
    "subtitle":None,
    "date":"p.content-secondary",
    "content": "div.check-html-content",
}
scrap_section(
    "stampa",
    "h3.press-release-card--content--title",
    leonardo_stampa_selectors,
    "scraping/leonardo/stampa",
    "https://www.leonardo.com/it/media-hub/press-releases?_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_page=2&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_filterDateFrom=01.01.2020&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_filterDateTo=31.08.2025&_com_leonardocompany_list_content_viewer_portlet_ListContentViewerPortlet_dataFilterTypeReq=Year"
)