
from app import create_app
from config import config_options

app = create_app('development')
app.config.from_object(config_options['development'])

if __name__ == '__main__':
    app.run()
