from invoke import task

APP_LOCATION = "test_back_end/main"


@task
def run(c):  # Runs flask in default mode
    c.run(f"flask --app {APP_LOCATION} run")


@task
def debug(c):  # Runs flask in debug mode
    c.run(f"flask --app {APP_LOCATION} --debug run")


@task
def test(c):  # Runs tests
    c.run("pytest")


@task
def generate_revisions(c):
    """Generates alembic revisions based on changes on models"""
    c.run("alembic revision --autogenerate")
