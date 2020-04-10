# A bot to like, comment and scrape insta posts
# aimed to get more followers (companies like Instavast do this)
# https://github.com/timgrossmann/InstaPy
# def get_comments_on_post(
from instapy import InstaPy

# Use or nah headless browser
session = InstaPy(username='test', password='test', headless_browser=False)
session.login()
# ToDo scrape tags to like
session.like_by_tags(["linguistics"], amount=5)
# ToDo scrape words to avoid
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
# ToDo add comment generator
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
# Set quotas to avoid getting banned
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.end()
