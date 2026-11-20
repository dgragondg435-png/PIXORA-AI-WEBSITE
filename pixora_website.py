
import os

from flask import Flask, redirect, render_template_string

app = Flask(__name__)

DOWNLOAD_URL = (
    "https://github.com/dgragondg435-png/"
    "PIXORA-AI-WEBSITE/releases/download/"
    "v1.0.0/PIXORA_AI_Full.zip"
)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>PIXORA AI | AI Image Processing</title>

    <meta name="description"
          content="PIXORA AI - Image enhancement, compression,
          upscaling and conversion for Windows.">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #080d1b;
            color: white;
            line-height: 1.6;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 24px 9%;
            border-bottom: 1px solid #202b43;
        }

        .logo {
            font-size: 27px;
            font-weight: bold;
            color: #54d6ff;
            letter-spacing: 2px;
        }

        nav a {
            color: #d4dbea;
            text-decoration: none;
            margin-left: 25px;
        }

        nav a:hover {
            color: #54d6ff;
        }

        .hero {
            min-height: 590px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 80px 20px;
            background:
                radial-gradient(
                    ellipse at top,
                    #163b70 0%,
                    transparent 65%
                );
        }

        .hero-content {
            max-width: 850px;
        }

        .tag {
            color: #54d6ff;
            font-weight: bold;
            letter-spacing: 3px;
            margin-bottom: 20px;
        }

        h1 {
            font-size: clamp(42px, 7vw, 76px);
            line-height: 1.1;
            margin-bottom: 25px;
        }

        h1 span {
            color: #54d6ff;
        }

        .hero p {
            color: #b8c4d8;
            font-size: 18px;
            max-width: 650px;
            margin: auto;
        }

        .download-btn {
            display: inline-block;
            margin-top: 35px;
            padding: 17px 38px;
            border-radius: 10px;
            background: linear-gradient(90deg, #1689ff, #43d5ef);
            color: #061222;
            font-weight: bold;
            font-size: 17px;
            text-decoration: none;
            transition: 0.3s;
        }

        .download-btn:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 35px #1689ff55;
        }

        .download-note {
            color: #8796af;
            font-size: 13px;
            margin-top: 14px;
        }

        section {
            padding: 75px 9%;
        }

        .section-title {
            text-align: center;
            font-size: 36px;
            margin-bottom: 45px;
        }

        .section-title span {
            color: #54d6ff;
        }

        .features {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(220px, 1fr));
            gap: 22px;
        }

        .feature {
            background: #111b30;
            border: 1px solid #253652;
            border-radius: 15px;
            padding: 30px;
            transition: 0.3s;
        }

        .feature:hover {
            transform: translateY(-5px);
            border-color: #54d6ff;
        }

        .icon {
            font-size: 35px;
            margin-bottom: 15px;
        }

        .feature h3 {
            margin-bottom: 12px;
            color: #54d6ff;
        }

        .feature p {
            color: #aab7cc;
            font-size: 15px;
        }

        .about {
            text-align: center;
            background: #0d1527;
        }

        .about p {
            max-width: 750px;
            margin: auto;
            color: #b8c4d8;
            font-size: 17px;
        }

        .requirements {
            text-align: center;
            color: #aab7cc;
        }

        footer {
            padding: 30px 15px;
            text-align: center;
            border-top: 1px solid #202b43;
            color: #8190a8;
            font-size: 14px;
        }

        @media(max-width: 650px) {
            header {
                flex-direction: column;
                gap: 15px;
            }

            nav a {
                margin: 0 8px;
                font-size: 14px;
            }

            section {
                padding: 55px 7%;
            }
        }
    </style>
</head>

<body>

<header>
    <div class="logo">PIXORA AI</div>

    <nav>
        <a href="#home">Home</a>
        <a href="#features">Features</a>
        <a href="#about">About</a>
        <a href="#download">Download</a>
    </nav>
</header>

<main>

    <section class="hero" id="home">
        <div class="hero-content">

            <div class="tag">
                NEXT GENERATION IMAGE TOOL
            </div>

            <h1>
                Transform Your Images
                <span>With AI</span>
            </h1>

            <p>
                Enhance image quality, compress files,
                increase resolution and convert image formats
                with PIXORA AI.
            </p>

            <a class="download-btn" href="/download">
                Download PIXORA AI
            </a>

            <div class="download-note">
                Windows · Complete ZIP Package
            </div>

        </div>
    </section>

    <section id="features">

        <h2 class="section-title">
            Powerful <span>Features</span>
        </h2>

        <div class="features">

            <div class="feature">
                <div class="icon">✨</div>
                <h3>AI Enhancement</h3>
                <p>
                    Improve image quality using PIXORA AI tools.
                </p>
            </div>

            <div class="feature">
                <div class="icon">🔍</div>
                <h3>Image Upscaling</h3>
                <p>
                    Increase image resolution with supported tools.
                </p>
            </div>

            <div class="feature">
                <div class="icon">⚡</div>
                <h3>Fast Compression</h3>
                <p>
                    Reduce image file sizes with convenient controls.
                </p>
            </div>

            <div class="feature">
                <div class="icon">🔄</div>
                <h3>Format Conversion</h3>
                <p>
                    Convert images between supported formats.
                </p>
            </div>

            <div class="feature">
                <div class="icon">📁</div>
                <h3>Batch Processing</h3>
                <p>
                    Process multiple images in one workflow.
                </p>
            </div>

            <div class="feature">
                <div class="icon">💻</div>
                <h3>Windows Desktop</h3>
                <p>
                    A desktop application designed for Windows.
                </p>
            </div>

        </div>
    </section>

    <section class="about" id="about">

        <h2 class="section-title">
            About <span>PIXORA AI</span>
        </h2>

        <p>
            PIXORA AI is an image processing application
            designed to make enhancement, compression
            and conversion easier through a desktop interface.
        </p>

    </section>

    <section class="requirements" id="download">

        <h2 class="section-title">
            Get <span>PIXORA AI</span>
        </h2>

        <p>
            Download the complete Windows application package.
        </p>

        <a class="download-btn" href="/download">
            Download Full Package
        </a>

        <p style="margin-top:20px;font-size:14px;">
            Extract the ZIP file and run ui.exe from the
            extracted folder. Keep all package files together.
        </p>

    </section>

</main>

<footer>
    © 2026 PIXORA AI. All rights reserved.
    <br>
    Image processing made simple.
</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/download")
def download():
    return redirect(DOWNLOAD_URL, code=302)


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
