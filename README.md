### Problems
1. But there are multiple problem occurs inside both Manager and Operator dashboard: 1. When the operator logs in, the system will go and download city information ( .DXF, .CSV, .XML ) from the City module in Manager dashboard but if the city file is heavy or huge ( 20MB ), operator need to wait a long time before successful downloaded the file. 
2. When the operator successfully logs in and goes to the Navigation module, the operator will see their car position on screen in real time and at the same time in the Tracking module, the manager also can see the cars or operators. But if either operator or manager is having a bad internet connection, the operator or manager module will disconnect and when the internet connection is back, the connection is still disconnected. 
3. When the operator successfully logs in and goes to the Navigation module, the operator will see their car position on screen in real time and at the same time, every 1 second, the car position in the operator dashboard will send data to store in the database. But because of this, the database has huge transactions or many requests. 


### Solutions
1. Use celery for downloading the file in background and let operator logs in to the system. Operator will poll in every 5s if the task is done or not.
2. Use Websocket connection so that if network fails on restarting the connection it will load the map and reload the data again.
3. I am not well known about this, but i believe relational disk based database will be bottleneck in such case, in memory database help to handle these huge amount of data. I can study on how Uber and other ride sharing software are handling this data, so that can get a clear view.


### Project Structure
This is a very simple application to show how we can achieve the solutions of above problems.
I couldn't implement all the features correctly may be for lack of time and proper testing.
But I believe this way we can overcome these problems.
This draft application is just a pseudo solution of the given problems.


#RUN
``` bash
docker-compose up -d --build
```
``` bash
docker-compose up
```

For running the project

After successful running, access backend service bash by(in another terminal):
``` bash
docker-compose -exec backend bash
```

Run
```python
python manage.py createsuperuser
```

Follow the step and create a superuser for accessing the system. Login as superuser and create manager and operator.

### Project Description
1. Login with superuser to create manager. (Superuser can do everything as well as manager)
2. Login as manager. username: Party Email, Password: 1234
3. Login as manager, create car, city, assign car and operator in city.(No filter for already assigned car and operator. :3 sorry)
4. On assigning operator will get a code. See City Car List for Operator code.
5. Login with this code as operator.
6. The map is initialized with dummy data.


Thank you for the opportunity.
