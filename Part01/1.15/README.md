# 1.15 Homework

[Docker Hub - Python3 BMI calculator](https://hub.docker.com/r/6a6d73/py-bmi) - Allows user to calculate their BMI using the metric system.

```
Calculate BMI (metric system) in the terminal.

# How to use this image

```
docker run --rm --interactive --tty 6a6d73/py-bmi <weight> <height>
```

Only two arguments are allowed.

The `<weight>` and `<height>` arguments only accepts 0-9 (numbers)  and . (dot) for decimal.
```