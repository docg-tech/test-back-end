from invoke import task

APP_LOCATION = "test-back-end/main"


@task
def run(c):
    c.run(f"flask --app {APP_LOCATION} run")


@task
def debug(c):
    c.run(f"flask --app {APP_LOCATION} --debug run")
