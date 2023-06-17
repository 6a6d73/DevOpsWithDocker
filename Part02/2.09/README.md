# 2.09 Fix buttons

The backend file was not changed but was still submitted since part of the exercise.

## Fix

In docker-compose.yml remove the `ports` sections for both frontend and backend.

Edit the Dockerfile for `frontend` from:

```
ENV REACT_APP_BACKEND_URL=http://localhost:8080
```

to:

```
ENV REACT_APP_BACKEND_URL=http://localhost/api/
```

## Alternative fix (not used)

Leave `ports` as they are in docker-compose.yml

In the `backend` change the Dockerfile line from:

```
ENV REQUEST_ORIGIN=http://localhost:5000
```

to:

```
ENV REQUEST_ORIGIN=http://localhost
```

And the buttons work again. Although, I feel like not exposing the ports is the better solution, which is why I used that one instead.

