from test_back_end import config, create_app

if __name__ == "__main__":
    app = create_app(config)
    app.run()
