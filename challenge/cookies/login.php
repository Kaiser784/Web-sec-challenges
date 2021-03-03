<?php

error_reporting(-1); 
ini_set('display_errors', true);

$user='admin123';
$password='password';

$cook=$_COOKIE['admin'];

session_start();

if($cook=='True')
{
    echo '<script>location.href="not_flag/"</script>';
}
else
{
    if($_POST['user']==$user && $_POST['password']==$password)
    {
        $_SESSION['user']=$user;
        setcookie('admin','False');

        $_COOKIE['admin'] = 'False';

        echo '<script>location.href="obviously_flag/"</script>';
    }
    else
    {
        echo '<script>alert("Username or Password incorrect!!")</script>';
        echo '<script>location.href="index.html"</script>';
    }
}
?>