# 1.06 Hello Docker Hub

```
docker run --interactive --tty --name secret_message devopsdockeruh/pull_exercise
Give me the password: basics
You found the correct password. Secret message is:
"This is the secret message"
```

```
docker exec --interactive --tty secret_message sh
/usr/app # less README.md
This is the readme, use input "basics" to complete this exercise.
```
