'''
System Design Prompt: Design Uber
You are tasked with designing a ride-hailing service similar to Uber. The system should handle the following features:

Requirements
Functional Requirements
Rider Features:

Book a ride by providing their current location and destination.
View available drivers near their location.
Real-time tracking of their driver.
Driver Features:

Accept or reject ride requests.
Update their location in real-time.
Shared Features:

Handle payments after ride completion.
Provide notifications (e.g., ride confirmation, arrival time).
Non-Functional Requirements
Scalability: The system should handle millions of riders and drivers worldwide.
Availability: The system must ensure 99.99% uptime for critical features like booking rides.
Low Latency: Booking and matching should complete within seconds.
Constraints
Data Volume: Assume there are over 1 billion rides per year, with real-time location updates every 5 seconds.
Request Volume: Up to 1 million concurrent ride requests globally.

'''