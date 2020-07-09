import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

# For previewing your goat channel
you_tube_embed = ''

class GoatHTTPRequestHandler(BaseHTTPRequestHandler):

    def read_state(self):
        cmd = "/bin/systemctl is-active goatstream"
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        is_active = p == b"active\n"
        return is_active

    def toggle_state(self):
        start_state = self.read_state()
        if start_state:
            cmd = "sudo /home/goatstream/stop.sh"
        else:
            cmd = "sudo /home/goatstream/start.sh"
        p3 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        return

    def do_GET(self):
        is_on = self.read_state()
        val = None
        if is_on:
            status = 'Everybody can see your goats'
            val = 'Hide the goats'
        else:
            status = 'The goats are invisible'
            val = 'Release the goats'
        pg = '<html><head><title>Goat media controller</title></head><body style="text-align:center; font-size:300%"><br /></br />'+you_tube_embed +'<div>' + status + '</div><br /><form method="post"><input style="font-size:100%" type="submit" value="' + val + '" /></body></html>'
        self.send_response(200)
        self.end_headers()
        self.wfile.write(pg.encode())

    def do_POST(self):
        is_on = self.read_state()
        self.toggle_state()
        if is_on:
            status = 'Turning off the goatstream'
        else:
            status = 'Turning on the goatstream'
        pg = '<html><head><meta http-equiv="refresh" content="3;url=/" /><title>Goat media controller</title></head><body style="text-align:center; font-size:300%"><br /><br />'+you_tube_embed+'<div>' + status + '</div></body></html>'
        self.send_response(200)
        self.end_headers()
        self.wfile.write(pg.encode())


httpd = HTTPServer(('0.0.0.0', 8000), GoatHTTPRequestHandler)
httpd.serve_forever()
import subprocess

