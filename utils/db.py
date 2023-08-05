

def config(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Fernanflo23'
    app.config['MYSQL_DB'] = 'cinex'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    return app

