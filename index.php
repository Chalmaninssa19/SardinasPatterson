<!DOCTYPE html>
<html>
    <head>
        <title>Sardinas et Patterson</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="container">
            <div class="title">
                <h3>Veuillez entrer le langage pour verifier s'il est un code ou non</h3>
            </div>
            <div class="form">
                <form action="result.php" method="POST">
                    <labe>Langage</label>
                    <input type="text" name="language"/>
                    <button type="submit">Verifier</button>
                </form>
            </div>
            <p>
                <a href="prediction.php">Taux de precision du modele</a>
            </p>
        </div>
    </body>
</html>