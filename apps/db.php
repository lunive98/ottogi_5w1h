<?php
$server = "54.199.5.46:0";
$user = "root";
$password = "1234";
$dbname = "team3";

$conn = new mysqli($server, $user, $password, $dbname);

if($conn->connect_error) echo "<h2>접속 실패</h2>";
else echo "<h2>접속 성공</h2>";
?>