<?php 
    $language = $_POST['language'];
    $output=null;
    $retval=null;
    $command = 'python /var/www/html/sardinasPatterson/python/prediction.py "'.$language.'"';
    exec($command, $output, $retval);
    $val = $output[0];
    $command1 = 'python /var/www/html/sardinasPatterson/python/sardinas.py "'.$language.'"';
    exec($command1, $output, $retval);
    $valSardi = $output[0];
?>


<!DOCTYPE html>
<html>
    <head>
        <title>Sardinas et Patterson</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="container-result">
            <div class="title">
                <h3>Resultat machine learning</h3>
                <?php echo $val ?>
            </div>
        </div>
        <div class="container-result">
            <div class="title">
                <h3>Resultat Sardinas patterson alogrithme</h3>
                <?php echo $valSardi ?>
            </div>
        </div>
    </body>
</html>