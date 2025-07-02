<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>DainerGameplays</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #1a2980, #26d0ce);
            min-height: 100vh;
            margin: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #fff;
        }
        header {
            background: rgba(0,0,0,0.7);
            padding: 30px 0 20px 0;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 3em;
            letter-spacing: 2px;
            margin: 0;
            color: #26d0ce;
            text-shadow: 2px 2px 8px #000;
        }
        nav {
            margin: 20px 0;
        }
        nav a {
            color: #fff;
            background: #26d0ce;
            padding: 10px 25px;
            margin: 0 10px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s;
        }
        nav a:hover {
            background: #1a2980;
        }
        .container {
            max-width: 900px;
            margin: 40px auto;
            background: rgba(0,0,0,0.6);
            border-radius: 18px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        }
        .presentacion {
            font-size: 1.4em;
            margin-bottom: 30px;
            line-height: 1.6;
        }
        .video {
            text-align: center;
            margin: 30px 0;
        }
        .video iframe {
            width: 80%;
            height: 400px;
            border-radius: 12px;
            border: none;
            box-shadow: 0 4px 24px rgba(0,0,0,0.5);
        }
        .juegos {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            justify-content: center;
        }
        .juego-card {
            background: rgba(38,208,206,0.15);
            border: 2px solid #26d0ce;
            border-radius: 14px;
            padding: 20px;
            width: 220px;
            text-align: center;
            box-shadow: 0 2px 12px rgba(0,0,0,0.2);
            transition: transform 0.2s;
        }
        .juego-card:hover {
            transform: scale(1.05);
            background: rgba(38,208,206,0.25);
        }
        .juego-card img {
            width: 100%;
            border-radius: 10px;
            margin-bottom: 12px;
        }
        .footer {
            text-align: center;
            padding: 30px 0 10px 0;
            color: #eee;
            font-size: 1.1em;
            background: rgba(0,0,0,0.7);
            margin-top: 60px;
        }
        @media (max-width: 700px) {
            .container { padding: 15px; }
            .video iframe { width: 100%; height: 220px; }
            .juegos { flex-direction: column; align-items: center; }
        }
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
        <div class="presentacion" id="inicio">
            <strong>¡Bienvenido a DainerGameplays!</strong><br>
            Aquí encontrarás los mejores gameplays, trucos, retos y diversión gamer.<br>
            Únete a la comunidad y vive la experiencia de los videojuegos como nunca antes.
        </div>
        <div class="video" id="videos">
            <h2>Último Video</h2>
            <iframe src="https://www.youtube.com/embed/8J4d7Zzovsw?start=2" allowfullscreen></iframe>
        </div>
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
        <h2 id="contacto" style="margin-top:40px;">Contacto</h2>
        <p>¿Tienes sugerencias o quieres colaborar? Escríbeme a 
        <a href="mailto:dainerade@gmail.com" style="color:#26d0ce;">dainerade@gmail.com</a></p>
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
