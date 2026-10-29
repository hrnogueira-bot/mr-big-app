# Builds ../index.html (the published app) from the files in this folder.
import base64,json,re,sys
import os,time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
src=open('app.src.html').read()
b64=lambda f:'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
plan=json.load(open('planta.json'))
q=82  # room 3 quota so the gym totals 400 machines
html=src.replace('__EMBLEM__',b64('emblema.jpg')).replace('__LOGO__',b64('logo.jpg')).replace('__PLAN__',json.dumps(plan,ensure_ascii=False)).replace('__PHOTOS__',open('fotos.json').read()).replace("{room:'3',f:0,quota:999","{room:'3',f:0,quota:%d"%q)
head='''<!doctype html>
<html lang="pt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Mr Big">
<meta name="theme-color" content="#0B0B0B">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
'''
body=html.replace('<title>','</head>\n<body>\n<title>',0)
t=re.search(r'<title>.*?</title>',html).group(0); rest=html.replace(t,'',1)
# put style/link in head, rest in body
i=rest.index('</style>')+len('</style>')
pwa=head+t+'\n'+rest[:i]+'\n</head>\n<body>\n'+rest[i:]+'\n<script>\nif(\'serviceWorker\' in navigator){window.addEventListener(\'load\',function(){navigator.serviceWorker.register(\'sw.js\').catch(function(){});});}\n</script>\n</body>\n</html>\n'
pwa=pwa.replace('<meta name="claude:viewport-fit-sides" content="cover">','')
open('../index.html','w').write(pwa)
# bump the service-worker cache so phones pick up the new version
sw=open('../sw.js').read()
v='mrbig-'+time.strftime('%Y%m%d-%H%M%S')
sw=re.sub(r"const VERSION = '[^']*';","const VERSION = '%s';"%v,sw)
open('../sw.js','w').write(sw)
print('built index.html, cache',v)
