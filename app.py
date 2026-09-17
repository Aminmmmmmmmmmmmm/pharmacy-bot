from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

drugs = {
    "آموکسی سیلین": {"english": "Amoxicillin", "category": "آنتی بیوتیک", "description": "درمان عفونت های باکتریایی"},
    "ایبوپروفن": {"english": "Ibuprofen", "category": "ضد درد", "description": "کاهش درد و تب"},
    "متفورمین": {"english": "Metformin", "category": "ضد دیابت", "description": "کنترل قند خون"},
}

HTML = """<!DOCTYPE html>
<html dir="rtl">
<head><meta charset="UTF-8"><title>جستجوی دارو</title></head>
<body>
<h1>جستجوی دارو</h1>
<input type="text" id="q" placeholder="اسم دارو...">
<button onclick="search()">جستجو</button>
<div id="result"></div>
<script>
function search(){
fetch('/search?q='+document.getElementById('q').value)
.then(r=>r.json()).then(d=>{
document.getElementById('result').innerHTML=d.found?
'دسته: '+d.category+' | '+d.description:'یافت نشد';
});}
</script>
</body></html>"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/search')
def search():
    q = request.args.get('q','').strip()
    for name, info in drugs.items():
        if q in name or q.lower() in info['english'].lower():
            return jsonify({"found": True, "name": name, **info})
    return jsonify({"found": False})

if __name__ == '__main__':
    app.run()
