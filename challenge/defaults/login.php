<?php

error_reporting(-1); 
ini_set('display_errors', true);

$user='admin';
$password='admin';

session_start();

if(isset($_SESSION['user']))
{
    echo '<script>location.href="not_flag/"</script>';
}
else
{
    if($_POST['user']==$user && $_POST['password']==$password)
    {
        $_SESSION['user']=$user;

        echo '<script>location.href="not_flag/"</script>';
    }
    else
    {
        echo '<script>alert("Username or Password incorrect!!")</script>';
        echo '<script>location.href="index.html"</script>';
    }
}
?>