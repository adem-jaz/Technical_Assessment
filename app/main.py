from facebook_page_scraper import Facebook_scraper
from facebook_scraper import get_posts
import json as _json
from fastapi import FastAPI
import databases
import sqlalchemy
from sqlalchemy import Column, String, Integer, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import sqlite3

app = FastAPI()


@app.get('/')
def index():
    return "Hello, Go to /scrape/page_name to try out the API"


def scrap(page_name):
    '''
    This function would do the first step of scraping: it uses facebook_page_scraper to get several information
    about each post, espacially their ids.
    However, this does not retrieve the comments.
    '''

    posts_count = 10
    browser = "firefox"
    proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
    timeout = 100
    headless = True
    meta_ai = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

    json_data = meta_ai.scrap_to_json()
    real_json_data = _json.loads(json_data)

    return real_json_data


def get_posts_info(page_name):
    '''
    This function uses the function get_posts from facebook_scraper to get more information about each post,
    espacially it is able to get the comments.
    '''

    data = scrap(page_name)

    posts_ids = data.keys()
    MAX_COMMENTS = 100
    posts = dict()

    for post_id in posts_ids:
        try:
            gen = get_posts(post_urls=[post_id], options = {"comments": MAX_COMMENTS, "progress":True})

            post = next(gen)
            posts[post_id] = post

        except:
            continue

    return posts


@app.get('/scrap/{page_name}')
def get_data(page_name, return_data = True):

    print("Scrapping the data, this may take few minutes..")
    data = get_posts_info(page_name)

    # SQLite database setup
    database_url = "sqlite:///./database/test.db"
    database = databases.Database(database_url)
    metadata = sqlalchemy.MetaData()

    Base = declarative_base()

    class FacebookScrapingData(Base):
        __tablename__ = "fb_data"

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        post_id = Column(String)
        post_url = Column(String)
        text = Column(String)
        time = Column(String)
        image = Column(String)
        video = Column(String)
        likes = Column(Integer)
        comments = Column(Integer)
        shares = Column(Integer)
        comments_full = Column(JSON)

    DATABASE_URL = "sqlite:///./database/test.db"

    engine = create_engine(DATABASE_URL)

    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:

        for post_id in data.keys():
            print(data[post_id])

            post_data = dict()
            columns = ["post_id", "post_url", "text", "time", "image",
                       "video", "likes", "comments", "shares", "comments_full"]
            for col in columns[:-1]:
                try:
                    post_data[col] = data[post_id][col]
                except:
                    print(f"{col} is not available for this post")

            try:
                json_comments = _json.dumps(data[post_id]["comments_full"], default=str)
                post_data["comments_full"] = json_comments
            except KeyError:
                print("We cannot get the comments of this post")
            scraping_data = FacebookScrapingData(**post_data)
            session.add(scraping_data)
            session.commit()

    if return_data:
        con = sqlite3.connect('./database/test.db')
        cur = con.cursor()
        full_data = [x for x in cur.execute("Select * from fb_data")]
        con.close()
        return full_data