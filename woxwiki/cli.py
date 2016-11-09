from woxwiki import app, db

@app.cli.command('createdb')
def createdb_cli():
    db.create_all()
