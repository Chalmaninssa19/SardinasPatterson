<?php 
    $output=null;
    $retval=null;
    $command = 'python /var/www/html/sardinasPatterson/python/traitement.py';
    exec($command, $output, $retval);
    $val = $output[0];
?>

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
                <h3>Taux de prediction</h3>
            </div>
            <p class="prediction"><strong><?php echo $val ?></strong></p>
        </div>
    </body>
</html>