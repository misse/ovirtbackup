from app import app

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True 
    app.run(host="0.0.0.0",)
