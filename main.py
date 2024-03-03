from fastapi import FastAPI
from news.new_list_crawler import initial_news_list_crawl

app = FastAPI()


@app.get("/news")
def get_today_news():
    return initial_news_list_crawl()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

