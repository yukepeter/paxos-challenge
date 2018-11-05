# Paxos Challenge

Challenge description can be find [here](https://drive.google.com/file/d/1KAx8-5oZxOo_6YnlOMiH-gj5Ouvf2-m6/view?usp=sharing) 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Two scripts both writen in Python3 and run on Python3 

## Running the tests

Follew instructions to run test for two challenges

## Challenge 1

Make sure port 8000 is not being used and run the server use
```
$ ./msg-hashing-server
```
Then open a new terminal as client, then run to post a message to our server, you can change the content of the message.
```
$ curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http://localhost:8000/
```
You can then query your service for the original message:
```
$ curl http://localhost:8000/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f9
8a5e886266e7ae
```
You can calculate that your result is correct on the command line:
```
$ echo -n "foo" | shasum -a 256 2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae -
```
If you send a request to a non-existent <hash>, you should expect to receive a 404 error:
```
$ curl -i http://localhost:8000/messages/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaa
```
### Performance Question
What would the bottleneck(s) be in your implementation as you acquire more users? How you might scale your microservice?

In my implementation, I did everything in-memory because it achieved all functional requirements and provided the ultimate in low latency. But the disadvantage would be lost of historical user data when the server went down. If time permits and this is a real project, I would definitely use web framework to implement our backend and a database to solve this problem.(A NoSQL database, such as MongoDB and Redis, would better suit our needs due to the key-value nature of our data)

Assume we have adopted NoSQL database in our implementation and given thousands of concurrent users hitting our web server, it would require our server side maintain the session data each time a user interact with it. If not handled properly, we would face single point of failure(SPOF). With a growing amount of work, we need increase the capability of our database to handle growth in the amount of data and users. In this instance our centralized transactional database would be the most bottleneck. 

There are multiple ways to increase the ability of our server to perform more total work in the same elapsed of time to accommodate the growth. 
We can adopt memcach and Redis to provide a fast, in-memory caching of the frequently queried hashing message. Otherwise, we could use sharding  to partition user on to different severs along with their hashed messages. 


## Challenge 2

Big O Notation for this script is O(N)
### Bonus Question 
To run test
```
python3 find-pair.py prices.txt 2500
```
#### Big O notation for your program?
```
Big O Notation for this script is `O(N)`. It will scale linearly proportional
to the length of the prices list.
```

You can run the previous command plus an extra parameter to get the result.

```
python3 find-pair.py prices.txt 2500 3
```
#### Big O notation for your bonus program?
```
Big O Notation for this script is `O(N^2)`. It will scale linearly proportional
to the length of the prices list.
```
