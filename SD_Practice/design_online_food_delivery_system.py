'''
Problem: Design an Online Food Delivery System
You need to design an online food delivery system that includes the following functionalities:

Users can browse restaurants, place orders, and track their orders.
Restaurants can add/edit their menu and update order statuses.
The system should calculate the total price of an order, including taxes and delivery fees.
Support different payment methods (e.g., credit card, PayPal).
Ensure the system adheres to SOLID principles:
Open/Closed Principle: Adding new payment methods or user types should not require modifying existing code.
Liskov Substitution Principle: Subtypes should replace their parent types seamlessly.
Dependency Inversion: High-level modules should not depend on low-level modules.
'''

# answer
'''
Functional:
- User can browse restaurants
- User can place orders
- User can add to their order statuses
- user can edit to their order statuses
- User can track their orders
- calculate total price of an order with taxes and delivery fees
- Payment methods

Non-Functional Assumptions:
- Can handle across the globe
- Can scale to at least 1 million concurrent users


Frontend:
- Mobile
- Web

CDN
- Content delivery network for images and other content

API Gateway:
- Multiple load balancers to redirect traffic based on region for fault-tolerance

MicroServices
- UserService:
    GET get_user_by_user_id,
    GET get_user_profile
- OrderService:
    POST place_order --> push to kafka queue to send notification order placed,
    PUT edit_order --> push to kafka queue to send notification order edited,
    GET track_order --> Push to kafka queue when driver location at delivery location,
    GET get_order_summary
- BrowseService:
    GET browse(store_id: str)


Queue
- order_notifaction_topic: pushes to the frontend when order has been placed or edited
- order_delivered_topic: pushes to the frontnend when order has been delivered

Databases
- User: Postgresql + Postgis - For easier constant write and updates for latitude and longitude location updates
    -  user_id, username, email, billing_address, latitude, longitude, date_joined, last_ordered_date, user_type, rating
- Order: PostgreSql - For ACID compliance, durability, and consistency
    - order_id, num_items, base_cost, tax, delivery_fee, total_cost, user_id
- Store: MongoDB - Heavy read, flexible schema
    - store_id: {store_id, store_type, store_name, latitude, longitude, rating}
- Payment: Postgresql
    - payment_id, user_id, payment_method, payment_date

Optimizations:
- User and Order both have primary index of user_id, order_id respectively. Shard Store db with store_id.
- MasterServer for writes, multiple replicas per region for reads for fault-tolerance and durability.
- Kafka queue will have dead letter queue and retry mechanisms with TTL of 30min until it is deleted as it becomes irrelevant after a certain amount of time
'''



### Areas for Improvement
'''
Areas for Improvement
Frontend and API Gateway:

While you mention mobile/web clients and an API Gateway, you could elaborate on:
Authentication: How users will authenticate (e.g., OAuth, JWT).
Rate Limiting: Mechanisms to protect APIs from abuse.
API Gateway could include request throttling and caching for frequently accessed endpoints (e.g., restaurant browsing).
Payment Service:

You mentioned Payment as a database but did not elaborate on:
Payment gateway integrations (e.g., Stripe, PayPal) or abstractions for adding new payment providers.
Handling payment failures, retries, or edge cases like disputes.
Caching:

Frequently accessed data like restaurant details (e.g., menu, store info) could benefit from a caching layer (e.g., Redis).
Cached order summaries for faster repeated access could reduce load on OrderService.
OrderService Queue Details:

It's unclear if Kafka is handling event-driven processing for order updates or just notification delivery. Elaborate on:
How order placement triggers processing pipelines (e.g., notification to restaurant, assignment to a delivery driver).
Real-Time Tracking:

For real-time order tracking, consider using WebSockets or long-polling for bi-directional communication.
Storing and querying live driver locations might need Redis Streams or DynamoDB for low-latency writes/reads.
Monitoring and Observability:

Monitoring is critical for a system handling millions of users. Include tools like Prometheus for metrics and ELK/Datadog for logging and alerts.
Global Deployment:

While you mention global scalability, elaborate on deployment strategies:
Use of CDNs for static content (e.g., CloudFront).
Multi-region deployment with traffic routing (e.g., AWS Route 53) to minimize latency.
Additional Non-Functional Considerations:

High Availability: Mention how services will handle failures (e.g., active-active redundancy).
Security: Outline data encryption for sensitive information (e.g., payment details) and compliance (e.g., PCI DSS).
'''