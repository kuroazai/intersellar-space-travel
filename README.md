
# Interstellar Route Planner
![](https://img.shields.io/badge/Flaskb-blue) 
![](https://img.shields.io/badge/Python-green)
![](https://img.shields.io/badge/Mongodb-blue)
![](https://img.shields.io/badge/Requests-blue)


## Solution to problem 

Initially tried using bfs(breadth first search) to solve the shortest path but yielded the wrong results since our dataset has rules on one way system and the path found wasn't nessarily the shortest path or cheapest path to be recommended. 
Used Djisktra Algorithim without overcomplicating the process to find the shortest path which should be the cheapest path due to travelling less amount of distance.  


## Docker Commands // Installation
---------------
Commands are in sequential order in order to setup the project successfully. should be processed in this projects root directory. 
```
docker-compose up -d
```

[Postman API documentation Link](https://documenter.getpostman.com/view/12223839/2s93z6ejh7)

