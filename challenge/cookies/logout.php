<?php 

session_start();

if(isset($_SESSION['user']))
{
    session_destroy();
    setcookie('admin', '', time() - 3600);
    echo '<script>location.href="index.html"</script>';
}
else
{
    echo '<script>location.href="index.html"</script>';
}

?>