from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centered Box</title>
    <style>
        // _sass/main.scss
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }

        .centered-box {
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 255, 0.2);
            padding: 20px;
            max-width: 300px;
            text-align: center;
        }

    </style>
</head>
<body>
    <div class="centered-box">
        <p>This is a centered box with rounded corners and a blue shadow.</p>
    </div>
</body>
</html>'''

if __name__ == "__main__":
    app.run()
