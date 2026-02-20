from newspaper import Article, Config


def get_content(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 5
    article = Article(url, config=config)
    try:
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Could not get content\n{e}")
        return None

