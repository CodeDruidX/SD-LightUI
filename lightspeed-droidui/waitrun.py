import socket
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ht=r"""
<div>
        <a href="/docs">API</a>
         • 
        <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">Github</a>
         • 
        <a href="https://gradio.app">Gradio</a>
         • 
        <a href="https://github.com/CodeDruidX">LightSpeed by droidx</a>
         • 
        <a href="/" onclick="javascript:gradioApp().getElementById('settings_restart_gradio').click(); return false">Reload LightSpeedUI </a>
</div>
<br />
<div class="versions">
{versions}
</div>
"""
with open(r"html\footer.html",'w',encoding="utf-8") as f:
    f.write(ht)
work=1
while work:
    work = sock.connect_ex(('127.0.0.1',7860))
sock.close()
os.system(r'lightspeed-droidui\electron.exe lightspeed-droidui\f\main.js"')