'''
Problem Statement:
Design the backend of Twitter focusing on posting tweets, following/unfollowing users, and generating a user's feed.
Your design should handle:
- Posting a tweet.
- Following or unfollowing another user.
- Generating the feed of a user with the most recent tweets from the accounts they follow.
LLD Expectations:
Classes and Attributes:
- Define core entities and their attributes.
- Maintain relationships between entities.
Methods:
- Create clear APIs for each action (e.g., postTweet, followUser, getFeed).
- Ensure correctness and performance.
Key Requirements:
- Each tweet must have a unique ID, content, and timestamp.
- Users can follow/unfollow others.
- The feed should show tweets in reverse chronological order from followed users.
Task:
Using CARM (Classes, Attributes, Relationships, Methods), design and implement the system. Aim to complete in 20–30 minutes.
'''

# Answer
'''
Refined LLD for Twitter
CARM
Classes

Tweet: Handles tweet data and operations.
User: Manages user information and relationships (following/followers).
FeedService: Fetches feeds for users using fanout.
FanoutStrategyService (abstract class): Defines how feeds are generated (write-based for celebrities, read-based for regular users).
FanoutRead: Implements read-based fanout.
FanoutWrite: Implements write-based fanout.

Relationships
- User has a relationship with FeedService for fetching feeds.
- Tweet is independent and managed by FeedService and FanoutStrategyService.

Key Changes and Explanations

Separation of Concerns:

FeedService handles fetching feeds and posting tweets.
FanoutStrategyService encapsulates fanout logic.
User focuses on relationships.
APIs:
- post_tweet and get_feed provide clear entry points for the system.
Tweet Storage:
- Tweets are stored in FeedService (e.g., mocked with a list for simplicity).
Strategy Pattern:
- Different fanout behaviors (FanoutRead, FanoutWrite) encapsulate their own logic.


*****Relationships*****

User (independent) <---> Tweet (independent)

User ---> Feed (Feed depends on User)

Feed ---> FanoutStrategyService (Feed uses Strategy)

FanoutStrategyService ---> FanoutRead / FanoutWrite (Implementations of Strategy)

User (independent) <---> Tweet (independent)

User ---> Feed (Feed depends on User)

Feed ---> FanoutStrategyService (Feed uses Strategy)

FanoutStrategyService ---> FanoutRead / FanoutWrite (Implementations of Strategy)

'''

from abc import ABC, abstractmethod
from collections import defaultdict, deque
from enum import Enum
import time


# Enum for User Type
class UserType(Enum):
    REGULAR = "regular"
    CELEBRITY = "celebrity"


# Tweet Class
class Tweet:
    def __init__(self, tweet_id: int, content: str, user_id: int, timestamp=None):
        self.tweet_id = tweet_id
        self.content = content
        self.user_id = user_id
        self.timestamp = timestamp or time.time()

    def __repr__(self):
        return f"Tweet(id={self.tweet_id}, user={self.user_id}, time={self.timestamp})"


# User Class
class User:
    def __init__(self, user_id: int, username: str, user_type: UserType):
        self.user_id = user_id
        self.username = username
        self.user_type = user_type
        self.following = set()  # Users this user is following
        self.followers = set()  # Users following this user

    def follow(self, user_id: int):
        self.following.add(user_id)

    def unfollow(self, user_id: int):
        self.following.discard(user_id)

    def __repr__(self):
        return f"User(id={self.user_id}, username={self.username}, type={self.user_type})"


# Abstract Fanout Strategy
class FanoutStrategyService(ABC):
    @abstractmethod
    def fanout(self, user: User, tweet=None):
        pass


# Write-based Fanout (for celebrities)
class FanoutWrite(FanoutStrategyService):
    def __init__(self, user_feeds: dict):
        self.user_feeds = user_feeds  # Simulate a database of user feeds

    def fanout(self, user: User, tweet: Tweet):
        print(f"Performing write-based fanout for {user.username}.")
        for follower_id in user.followers:
            if follower_id not in self.user_feeds:
                self.user_feeds[follower_id] = deque(maxlen=100)  # Efficient, bounded feed
            self.user_feeds[follower_id].appendleft(tweet)
        print(f"Fanout complete for {len(user.followers)} followers.")


# Read-based Fanout (for regular users)
class FanoutRead(FanoutStrategyService):
    def __init__(self, tweets_db: dict):
        self.tweets_db = tweets_db  # Simulate a database of tweets

    def fanout(self, user: User):
        print(f"Performing read-based fanout for {user.username}.")
        feed = []
        for following_id in user.following:
            if following_id in self.tweets_db:
                feed.extend(self.tweets_db[following_id])
        # Sort feed by timestamp
        feed.sort(key=lambda tweet: tweet.timestamp, reverse=True)
        return feed


# Feed Service
class FeedService:
    def __init__(self):
        self.tweets_db = defaultdict(list)  # Simulate a DB: user_id -> list of tweets
        self.user_feeds = defaultdict(deque)  # Simulate a DB: user_id -> deque for feed tweets

    def post_tweet(self, user: User, content: str):
        tweet = Tweet(tweet_id=len(self.tweets_db[user.user_id]) + 1, content=content, user_id=user.user_id)
        self.tweets_db[user.user_id].append(tweet)

        # Determine fanout strategy
        strategy = FanoutWrite(self.user_feeds) if user.user_type == UserType.CELEBRITY else None

        # Perform fanout
        if strategy:
            strategy.fanout(user, tweet)
        return tweet

    def get_feed(self, user: User):
        print(f"Fetching feed for {user.username}.")
        if user.user_type == UserType.CELEBRITY:
            # Celebrity feed from pre-computed feed
            return list(self.user_feeds[user.user_id])
        else:
            # Regular user feed through read-based fanout
            strategy = FanoutRead(self.tweets_db)
            return strategy.fanout(user)


# Example Usage
if __name__ == "__main__":
    # Users
    user1 = User(1, "Alice", UserType.REGULAR)
    user2 = User(2, "Bob", UserType.CELEBRITY)

    user1.follow(2)  # Alice follows Bob
    user2.follow(1)  # Bob follows Alice

    # Feed Service
    feed_service = FeedService()

    # Post Tweets
    feed_service.post_tweet(user2, "Hello, this is Bob!")  # Bob posts a tweet
    feed_service.post_tweet(user1, "Hello, this is Alice!")  # Alice posts a tweet

    # Fetch Feed
    print(f"{user1.username}'s Feed: {feed_service.get_feed(user1)}")
    print(f"{user2.username}'s Feed: {feed_service.get_feed(user2)}")
