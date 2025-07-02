from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'dainergameplays_secret'

inicio = """
<div class="presentacion" id="inicio">
    <strong>¡Bienvenido a DainerGameplays!</strong><br>
    Aquí encontrarás los mejores gameplays, trucos, retos y diversión gamer.<br>
    Únete a la comunidad y vive la experiencia de los videojuegos como nunca antes.
</div>
"""

videos = """
<div class="video" id="videos">
    <h2>Último Video</h2>
    <iframe src="https://www.youtube.com/embed/8J4d7Zzovsw?start=2" allowfullscreen></iframe>
</div>
"""

juegos = """
<h2 id="juegos">Juegos Destacados</h2>
<div class="juegos">
    <div class="juego-card">
        <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/270880/header.jpg" alt="American Truck Simulator">
        <h3>American Truck Simulator</h3>
        <p>¡Recorre Estados Unidos al volante de los camiones más impresionantes y vive la experiencia del transporte!</p>
    </div>
    <div class="juego-card">
        <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/271590/header.jpg" alt="GTA V">
        <h3>GTA V</h3>
        <p>Acción, aventura y mundo abierto en Los Santos. Disfruta de mis mejores momentos y locuras en GTA V.</p>
    </div>
    <div class="juego-card">
        <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1551360/header.jpg" alt="Forza Horizon 5">
        <h3>Forza Horizon 5</h3>
        <p>Velocidad, autos increíbles y paisajes espectaculares en el mejor festival automovilístico.</p>
    </div>
</div>
"""

contacto = """
<h2 id="contacto" style="margin-top:40px;">Contacto</h2>
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <div class="flash">{{ messages[0] }}</div>
  {% endif %}
{% endwith %}
<form class="contacto-form" method="post" action="#contacto">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre" required>
    <label for="email">Correo electrónico:</label>
    <input type="email" id="email" name="email" required>
    <label for="mensaje">Mensaje:</label>
    <textarea id="mensaje" name="mensaje" rows="4" required></textarea>
    <button type="submit">Enviar mensaje</button>
</form>
<p>¿Tienes sugerencias o quieres colaborar? Escríbeme a 
<a href="mailto:dainerade@gmail.com" style="color:#26d0ce;">dainerade@gmail.com</a></p>
"""

HTML = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>DainerGameplays</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        body {{
            background: linear-gradient(135deg, #1a2980, #26d0ce);
            min-height: 100vh;
            margin: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #fff;
        }}
        header {{
            background: rgba(0,0,0,0.7);
            padding: 30px 0 20px 0;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }}
        h1 {{
            font-family: 'Orbitron', sans-serif;
            font-size: 3em;
            letter-spacing: 2px;
            margin: 0;
            color: #26d0ce;
            text-shadow: 2px 2px 8px #000;
        }}
        nav {{
            margin: 20px 0;
        }}
        nav a {{
            color: #fff;
            background: #26d0ce;
            padding: 10px 25px;
            margin: 0 10px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s;
        }}
        nav a:hover {{
            background: #1a2980;
        }}
        .container {{
            max-width: 900px;
            margin: 40px auto;
            background: rgba(0,0,0,0.6);
            border-radius: 18px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        }}
        .presentacion {{
            font-size: 1.4em;
            margin-bottom: 30px;
            line-height: 1.6;
        }}
        .video {{
            text-align: center;
            margin: 30px 0;
        }}
        .video iframe {{
            width: 80%;
            height: 400px;
            border-radius: 12px;
            border: none;
            box-shadow: 0 4px 24px rgba(0,0,0,0.5);
        }}
        .juegos {{
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            justify-content: center;
        }}
        .juego-card {{
            background: rgba(38,208,206,0.15);
            border: 2px solid #26d0ce;
            border-radius: 14px;
            padding: 20px;
            width: 220px;
            text-align: center;
            box-shadow: 0 2px 12px rgba(0,0,0,0.2);
            transition: transform 0.2s;
        }}
        .juego-card:hover {{
            transform: scale(1.05);
            background: rgba(38,208,206,0.25);
        }}
        .juego-card img {{
            width: 100%;
            border-radius: 10px;
            margin-bottom: 12px;
        }}
        .footer {{
            text-align: center;
            padding: 30px 0 10px 0;
            color: #eee;
            font-size: 1.1em;
            background: rgba(0,0,0,0.7);
            margin-top: 60px;
        }}
        .contacto-form {{
            background: rgba(38,208,206,0.10);
            border-radius: 12px;
            padding: 25px;
            max-width: 500px;
            margin: 30px auto;
            box-shadow: 0 2px 12px rgba(0,0,0,0.15);
        }}
        .contacto-form input, .contacto-form textarea {{
            width: 100%;
            padding: 10px;
            margin: 8px 0 16px 0;
            border-radius: 6px;
            border: none;
            font-size: 1em;
        }}
        .contacto-form button {{
            background: #26d0ce;
            color: #fff;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-size: 1.1em;
            cursor: pointer;
            transition: background 0.3s;
        }}
        .contacto-form button:hover {{
            background: #1a2980;
        }}
        .flash {{
            background: #26d0ce;
            color: #fff;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 20px;
            font-weight: bold;
        }}
        @media (max-width: 700px) {{
            .container {{ padding: 15px; }}
            .video iframe {{ width: 100%; height: 220px; }}
            .juegos {{ flex-direction: column; align-items: center; }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>DainerGameplays</h1>
        <nav>
            <a href="#inicio">Inicio</a>
            <a href="#videos">Videos</a>
            <a href="#juegos">Juegos</a>
            <a href="#contacto">Contacto</a>
        </nav>
    </header>
    <div class="container">
        {inicio}
        {videos}
        {juegos}
        {contacto}
    </div>
    <div class="footer">
        &copy; 2025 DainerGameplays. Todos los derechos reservados.<br>
        Sígueme en 
        <a href="https://www.youtube.com/@daineradegames" target="_blank" style="color:#26d0ce;">YouTube</a> | 
        <a href="https://www.facebook.com/dainer.agualimpia.1/" target="_blank" style="color:#26d0ce;">Facebook</a> | 
        <a href="https://www.tiktok.com/@dainer_563?is_from_webapp=1&sender_device=pc" target="_blank" style="color:#26d0ce;">Tiktok</a>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        # Aquí podrías guardar el mensaje en una base de datos o enviarlo por correo
        flash('¡Gracias por contactarme, {}! Te responderé pronto.'.format(nombre))
        return redirect(url_for('index') + '#contacto')
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)