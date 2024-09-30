from bottle import run, route
import os

@route('/')
def index():
    page =  f'''
                <h1>Ping web app</h1>
                <p>Please add a host to the url to begin pinging.</p>
                <p>Such as http://127.0.0.1:8080/cnn.com</p>
            '''
    return page

@route('/<host>')
def index(host):
    host_list = host.split(',')
    body = ''
    for value in host_list:
        value = value.strip()
        try:
            response = os.popen(f'ping -c 1 {value}').read()
        except:
            response = 'Problem connecting.'
        finally:
            if response == '':
                response = 'Host could not resolve.'
            
            body = f'''
                    {body}
                    <h1>{value}</h1>
                    <pre>{response}</pre>
                    '''
    header = '<meta http-equiv="refresh" content = "5">'
    page = f'''
            {header}
            {body}
            '''    
    return page
    

run(host= '127.0.0.1', port=8080)