from waitress import serve
from woxwiki import app as wsgiapp

if __name__ == '__main__':
    serve(wsgiapp, listen='*:8080')

