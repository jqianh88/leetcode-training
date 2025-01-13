'''
Twitter System Design Problem Statement
Problem:
Design a system like Twitter that allows users to:

Post tweets.
Follow and unfollow other users.
Retrieve a user’s news feed with the 10 most recent tweets from users they follow, sorted by recency.
Constraints:

The system should support millions of users and handle high read/write operations.
Each user can follow many users, and each user can also have millions of followers.
News feed generation should be efficient and quick.

My Answer:
Requirements:
- Post tweets, Follow and unfollow other users, Search for top 10 relevant tweets by users followed

Non-functional Requirements:
- Global, support millions of users, connection between users and followers, responsive UI and news search

Frontend:
- Mobile and Web
-- Post Tweets
-- Delete Tweets
-- Follow
-- Unfollow
-- Search Tweets

API Gateway: To redirect traffic based on IP address to different regions based on the user's location and to avoid hotspotting as well as security
- Multiple load balancers for fault tolerance and durability

Microservices
- UserService: User and followers information
-- APIs: get_user, get_user_followed_by, get_user_following
- TweetsService: For posting and deleting tweets
-- APIs: post_tweet, delete_tweet, update_tweet
- NewsfeedAlgorithmService: Shows the news feed based on timestamp and chooses the 10 most recent from users they follow
--APIs: get_top_10: uses deque to pop when retrieving news feed and continues to add most recent tweets to the queue.
- SearchService: Keyword search of tweets
--APIs: get_tweets(keyword: text)

Databases
- UserService: MongoDb for the flexible schema and to allow users to have a list of followers
-- Properties: user_id, email, name, IP, followed_by: [users], following: [users]
- Tweets: Cassandra because it is natively distributed with high write with horizontal scaling.
-- Properties: tweet_id, tweet_content, timestamp, status, likes

There will a master db for writes for each region and replicas for read for each region to ensure durability and fault tolerance.

Analysis of my answer:
Strengths
Clear Functional and Non-Functional Requirements:

You've outlined both user-facing requirements (e.g., posting tweets, following/unfollowing) and technical constraints (e.g., global scalability, responsiveness).
Separation of Concerns with Microservices:

You’ve structured the services logically (UserService, TweetsService, NewsfeedAlgorithmService, SearchService), which will help scale each independently.
Database Selection:

Using MongoDB for user data makes sense because of its schema flexibility, and Cassandra for high-write operations on tweets is a good choice for scalability.
Use of API Gateway and Load Balancers:

These ensure fault tolerance, avoid hotspotting, and improve latency.
Newsfeed Algorithm and Search:

Incorporating a deque for real-time updates and a search index for keyword retrieval aligns well with the problem requirements.


Areas for Improvement
1. User Service Enhancements
Add metadata to users, such as profile creation date, bio, and profile picture.
Include APIs for updating user profiles and fetching user metadata.
Introduce rate limiting to prevent spam-like behavior (e.g., mass follows/unfollows).
2. Database Schema Improvements
Tweets Table: Include a partition key for users (e.g., user_id), enabling efficient retrieval of tweets by specific users. The schema could look like:
mathematica

Partition Key: user_id
Clustering Key: timestamp (DESC)
Columns: tweet_id, tweet_content, status, likes
User Table: Use a bidirectional graph approach for following/followed-by relationships.
- Example: user_id | followers_count | following_count | followers_set | following_set
3. Newsfeed Algorithm
Your deque-based approach works but can be enhanced:
Store pre-computed timelines in a Redis cache for fast retrieval.
Use a fanout-on-write approach:
Push tweets from a user directly to the timelines of their followers.
Cache the top 100 recent tweets per user.
4. Search Service
Keyword search needs full-text indexing:
Use Elasticsearch for real-time indexing and querying of tweets.
Add metadata for tweets (e.g., hashtags, mentions, language) to improve search relevance.
5. Global Architecture
Region-Based Sharding: Shard data (users, tweets) by geographic region to minimize latency.
Cross-Region Replication: Use tools like DynamoDB Global Tables or Cassandra’s multi-region replication to ensure availability.
6. Fault Tolerance
Introduce a message queue (Kafka) for events like posting/deleting tweets, ensuring consistency even during failures.
Include retries and Dead Letter Queues (DLQs) for processing failed events.
7. Non-Functional Aspects
Latency SLAs: Ensure <50ms latency for newsfeed retrieval.
Caching: Use Redis for frequently accessed data (e.g., user metadata, trending tweets).
Monitoring and Alerts: Implement tools like Prometheus and Grafana for system health monitoring


Updated High-Level Design

API Gateway: Routes traffic by region.
Microservices:
- UserService: Handles user data and relationships.
-- APIs: get_user, update_user, follow_user, unfollow_user.
- TweetsService: Handles tweets.
-- APIs: post_tweet, delete_tweet, like_tweet.
- NewsfeedService: Pre-computes timelines for efficiency.
-- APIs: get_newsfeed(user_id).
- SearchService: Uses Elasticsearch for full-text indexing.

Databases:
- User DB (MongoDB): Stores user profiles and relationships.
- Tweets DB (Cassandra): Stores tweets by user.
- Cache (Redis): Pre-computed timelines, user metadata.
- Search Index (Elasticsearch): Enables keyword-based tweet retrieval.

Messaging:
Kafka: Event-driven architecture for tweet posting/deletion.

Caching Strategy
Objective: Minimize latency for frequently accessed data like user profiles, newsfeeds, trending tweets, and search results.

Pre-Computed Timelines for Newsfeed:

What: Cache the most recent 100-200 tweets for each user in a Redis cluster.
Why: Newsfeeds are one of the most accessed features, so caching reduces database queries and improves response time.
How:
Use a key-value store structure: newsfeed:{user_id} → List of recent tweets.
Update this cache with a fanout-on-write approach:
When a user posts a tweet, push it directly to the timelines of their followers.
This ensures that retrieval is just a cache read operation.
Trending Tweets:

Use Redis Sorted Sets to maintain trending tweets by hashtag or topic.
Key: trending:{region}.
Value: List of hashtags/topics with scores (e.g., the number of mentions).
Periodically update this set via a batch job that scans recent tweets.
User Metadata:

Cache user profile data (user_id, name, followers_count, etc.).
Store in a key-value format: user:{user_id} → User Profile.
Search Results:

Cache recent search queries in Redis with a time-to-live (TTL) of a few minutes.
Key: search:{query} → List of tweet IDs.
Eviction Policy: Use an LRU (Least Recently Used) eviction policy to ensure popular items remain in the cache.

Monitoring and Alerts
Objective: Ensure system reliability, performance, and fault detection.

Metrics Collection:

Use Prometheus for metrics collection.
Key metrics to monitor:
API latency (e.g., GET /newsfeed, POST /tweet).
Database query latency and throughput.
Cache hit/miss rates for Redis.
Queue processing latency for Kafka.
Error rates (e.g., 4xx and 5xx responses).
Visualization:

Use Grafana for dashboards:
Display real-time graphs of API latency, cache performance, and throughput.
Create heatmaps to identify regional traffic spikes.
Alerts:

Use tools like PagerDuty or OpsGenie to set up alerts for critical metrics.
Examples:
Redis cache hit rate <90%.
Kafka consumer lag >100 messages.
Cassandra write latency >50ms.
Distributed Tracing:

Use Jaeger or Zipkin to trace API requests across microservices.
Helps in identifying bottlenecks or failures in distributed transactions.
Algorithm Specifics
Newsfeed Algorithm (Fanout-on-Write):
Steps:

When a user posts a tweet:
Push the tweet directly to the timelines of their followers.
For each follower:
Fetch their newsfeed:{user_id} cache.
Prepend the new tweet to the list.
If the list exceeds 100 tweets, pop the oldest tweet.
Store the tweet in Cassandra with user_id as the partition key.
Trade-Off:

Pro: Faster read times as timelines are precomputed.
Con: Higher write amplification due to multiple cache updates.
Optimization:

Use batch processing to push updates for users with a large number of followers (e.g., celebrities).
Search Algorithm:
Indexing:

Use Elasticsearch to index tweets by text content, hashtags, mentions, and language.
Store each tweet with metadata like tweet_id, user_id, timestamp, and relevance_score.
Relevance Scoring:

Combine factors like:
Keyword match score.
Recency (e.g., give more weight to newer tweets).
User interaction (e.g., likes, retweets).
Query Execution:

When a user searches for a keyword:
Query Elasticsearch with the keyword.
Apply filters (e.g., tweets only from followed users).
Sort results by relevance score and timestamp.
Fault Tolerance and Disaster Recovery
Global Architecture:
Active-Active Deployment:

Deploy services in multiple regions.
Use geo-DNS routing to send users to the nearest region.
In case of regional failure, reroute traffic to another region.
Cross-Region Data Replication:

Use Cassandra’s multi-region replication for tweets.
For MongoDB, use replica sets to synchronize user data globally.
Kafka Durability:

Enable message replication across brokers.
Use Dead Letter Queues (DLQs) to handle failed messages.
Backups:

Regularly back up databases and store snapshots in cloud storage (e.g., AWS S3).


'''

# Ideal Answer
'''
1. Requirements Analysis
Functional Requirements:
Post tweets.
Follow/unfollow users.
Retrieve a user's feed (tweets from followed users).
Support for search (e.g., trending hashtags, keywords).
Non-Functional Requirements:
Low latency (<200ms for feed retrieval).
Scalable to handle millions of users.
High availability (99.99% uptime globally).
Fault tolerance and disaster recovery.
2. High-Level Architecture
Frontend:
Mobile and Web applications.
Use a CDN for static content (e.g., images, videos).
API gateway to route requests to the backend services.
Backend Services (Microservices):
User Service:

Manages user profiles and follow relationships.
APIs: get_user, follow_user, unfollow_user.
Tweet Service:

Handles posting, deleting, and retrieving tweets.
APIs: post_tweet, delete_tweet, get_tweets.
Feed Service:

Generates personalized newsfeeds.
Implements fanout-on-write for regular users and fanout-on-read for celebrities.
APIs: get_feed.
Search Service:

Handles keyword and hashtag searches.
APIs: search_tweets.
Notification Service:

Sends notifications for events like new followers or likes.
Uses Kafka for message queues.
3. Data Storage
User Database:

MongoDB for flexibility (user schema includes dynamic fields for preferences).
Schema: {user_id, username, email, followers: [], following: []}.
Tweet Database:

Cassandra for high write throughput and scalability.
Schema: {tweet_id, user_id, content, timestamp, likes}.
Partition Key: user_id.
Feed Cache:

Redis for storing precomputed feeds.
Key: feed:{user_id}, Value: List of tweet IDs.
Search Index:

Elasticsearch for full-text search.
Stores tweet content, hashtags, and metadata.
4. Key Algorithms
Newsfeed Generation:
Fanout-on-Write:
When a user posts a tweet, push the tweet ID to the Redis feed of their followers.
Limits: For users with millions of followers (e.g., celebrities), use fanout-on-read.
Search Ranking:
Combine:
Relevance (keyword match).
Recency (timestamp).
Engagement (likes, retweets).
5. Caching and Optimization
Redis for:

User profiles: user:{user_id}.
Precomputed newsfeeds: feed:{user_id}.
Trending hashtags: trending:{region}.
Eviction Policy: Use LRU for caching with dynamic TTL.

6. Fault Tolerance
Global Deployment:

Use geo-replicated databases (e.g., Cassandra and MongoDB).
Active-active setup for regional failover.
Kafka Durability:

Enable replication across brokers.
Use Dead Letter Queues (DLQs) for failed events.
7. Monitoring and Alerts
Metrics:

API latency and throughput.
Cache hit/miss rates.
Kafka consumer lag.
Tools:

Use Prometheus for monitoring and Grafana for visualization.
Set up alerts for anomalies (e.g., high latency, 5xx errors).
8. Scalability and Future Enhancements
Shard MongoDB and Cassandra by user region.
Optimize search by precomputing trending hashtags.
Improve newsfeed relevance using machine learning for personalized recommendations.

'''

'''
Algorithms and Implementation
1. Fanout Algorithms: Fanout-on-Write and Fanout-on-Read
In a social media system like Twitter, fanout refers to the process of delivering a user’s post (tweet) to the newsfeeds of their followers.

- Fanout-on-Write
Approach: When a user posts a tweet, the system immediately "fans out" the tweet by pushing it to the feeds of all their followers.
How It Works:
Post a Tweet:

A user posts a tweet.
The tweet is saved in the Tweet Database (Cassandra) with metadata (e.g., tweet_id, user_id, timestamp, etc.).
Push to Followers’ Feeds:

Retrieve the list of followers for the user from the User Database (MongoDB or Redis cache).
For each follower:
Append the tweet_id to the follower's feed stored in Redis.
Key: feed:{follower_id}, Value: List of tweet_ids.
Update Notifications (Optional):

    Notify followers about the new tweet using a Notification Service and a message queue like Kafka.
    Pros:
    Fast reads: Newsfeeds are precomputed and ready in Redis, making retrieval instantaneous.
    Efficient for normal users: Most users have a manageable number of followers.
Cons:
-- Expensive writes: For users with millions of followers (e.g., celebrities), writing to all feeds simultaneously can overload the system.
-- Storage overhead: Duplicates the same tweet_id in multiple feeds.

- Fanout-on-Read
Approach: Instead of pushing tweets to followers' feeds, the system computes a user’s feed in real-time when requested.
How It Works:
Retrieve Followed Users:

When a user opens their feed, retrieve the list of users they follow from the User Database.
Fetch Recent Tweets:

For each followed user:
Query the Tweet Database (Cassandra) to fetch the most recent tweets (e.g., last 10 tweets).
Merge and Sort:

Merge all retrieved tweets and sort by timestamp to generate a chronological feed.
Pros:
Efficient writes: No need to push tweets to followers, reducing write amplification.
Storage-efficient: No duplication of tweet_ids across feeds.
Cons:
Slow reads: Computing the feed in real-time adds latency, especially for users following many accounts.
Complexity: Merging and sorting tweets dynamically can be resource-intensive.
When to Use Each:
Fanout-on-Write: Use for regular users with a manageable number of followers.
Fanout-on-Read: Use for celebrity accounts with millions of followers to avoid overwhelming the system.
2. Search Ranking Algorithm
Search functionality must handle keyword searches efficiently while ensuring relevant and timely results.

Key Metrics for Ranking Tweets:
Relevance:

Does the tweet contain the keyword(s) being searched?
Use TF-IDF (Term Frequency-Inverse Document Frequency) to measure keyword importance.
TF: How frequently the keyword appears in the tweet.
IDF: How unique the keyword is across all tweets (rare keywords are more valuable).
Recency:

Recent tweets are more likely to be relevant.
Apply a time decay function to reduce the weight of older tweets:
Recency Score=e−time_difference/τ
τ: Decay constant (e.g., 1 day).
Engagement:

Tweets with more likes, retweets, and replies should rank higher.
Combine engagement metrics into a single score:
Engagement Score=α⋅likes+β⋅retweets+γ⋅replies
Adjust weights (
α,β,γ) based on importance.
Steps to Rank Tweets:
Search Query Parsing:

Tokenize the search query into keywords and hashtags.
Handle special characters (e.g., #, @) and synonyms.
Fetch Candidate Tweets:

Query the Elasticsearch Index for tweets containing the keywords/hashtags.
Use Elasticsearch's reverse index for efficient retrieval.
Calculate Relevance:

Compute the TF-IDF score for each candidate tweet.
Apply Recency Weight:

Adjust the relevance score using the time decay function.
Incorporate Engagement:

Multiply the adjusted relevance score by the engagement score:
Final Score
=
Relevance Score
⋅
Recency Weight
⋅
Engagement Score
Final Score=Relevance Score⋅Recency Weight⋅Engagement Score.
Sort and Return:

Sort tweets by their final scores in descending order.
Return the top n tweets (e.g., top 10).
Example Walkthrough:
Search Query: "AI technology".
Elasticsearch Query: Retrieve all tweets containing "AI" or "technology".
Scores:
Tweet A:
Relevance: 0.8, Recency: 0.9, Engagement: 1.2
Relevance: 0.8, Recency: 0.9, Engagement: 1.2
Tweet B:
Relevance: 0.7, Recency: 0.95, Engagement: 0.9
Relevance: 0.7, Recency: 0.95, Engagement: 0.9
Final Scores:
Tweet A: 0.8⋅0.9⋅1.2=0.864.
Tweet B: 0.7⋅0.95⋅0.9=0.5985.
Sorted Output: Tweet A, Tweet B.
This process ensures relevance, timeliness, and engagement are prioritized, creating a highly optimized search experience.
'''