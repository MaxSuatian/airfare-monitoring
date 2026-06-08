# -*- coding: utf-8 -*-
import os

html = """<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Loopy 机票监控</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:Arial,Microsoft YaHei,sans-serif;background:#FFF0F5;color:#3D2C3D;}
.topbar{background:linear-gradient(135deg,#FFB3C6,#E8608C);padding:16px 24px;display:flex;align-items:center;gap:14px;}
.topbar img{width:48px;height:48px;border-radius:50%;border:3px solid rgba(255,255,255,.85);object-fit:cover;}
.topbar h1{color:#fff;font-size:20px;}
.hero{text-align:center;background:#fff;border-radius:16px;padding:28px 20px;margin-bottom:24px;box-shadow:0 8px 32px rgba(200,130,160,.12);}
.hero img{width:120px;height:120px;border-radius:50%;object-fit:cover;border:4px solid #fff;box-shadow:0 8px 28px rgba(232,96,140,.35);margin-bottom:12px;}
.hero h2{font-size:24px;color:#E85A7A;}
.card{background:#fff;border-radius:16px;padding:20px;margin-bottom:16px;box-shadow:0 6px 24px rgba(200,130,160,.1);}
.card h3{font-size:15px;color:#E8608C;margin-bottom:12px;}
.price-item{display:flex;justify-content:space-between;padding:10px 14px;border-bottom:1px solid #f5e6ea;}
.price{color:#E85A7C;font-weight:700;}
.footer{text-align:center;padding:16px;color:#8C6B7A;font-size:11px;border-top:1px solid #f0d4dc;margin-top:8px;}
</style>
</head>
<body>
<div class="topbar">
  <img src="loopy.jpg" alt="L" />
  <h1>Loopy 机票监控</h1>
</div>
<div class="hero">
  <img src="loopy.jpg" alt="Loopy" />
  <h2>\u2661 和 Loopy 一起出发吧 \u2661</h2>
  <p>粉色小浣熊帮你盯着机票价格</p>
  <p id="clock" style="font-size:12px;color:#ccc;margin-top:8px;">加载中...</p>
</div>
<div class="card">
  <h3>\u2708 实时价格</h3>
  <div class="price-item"><span>北京 \u2192 上海</span><span class="price">\u00a5480</span></div>
  <div class="price-item"><span>北京 \u2192 广州</span><span class="price">\u00a5650</span></div>
  <div class="price-item"><span>北京 \u2192 成都</span><span class="price">\u00a5520</span></div>
  <div class="price-item"><span>北京 \u2192 杭州</span><span class="price">\u00a5390</span></div>
  <div class="price-item"><span>北京 \u2192 三亚</span><span class="price">\u00a5780</span></div>
</div>
<div class="footer">Loopy 机票监控 \u2661 每日更新</div>
<script>
var d=new Date();document.getElementById("clock").textContent=d.toLocaleString("zh-CN");
setInterval(function(){var d=new Date();document.getElementById("clock").textContent=d.toLocaleString("zh-CN");},1000);
</script>
</body>
</html>
"""

fpath = r'C:\Users\x1 nano\Desktop\机票实时监控\index.html'
with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK! 写入完成, 大小:', len(html), 'bytes')
