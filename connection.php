<?php

$firstName =  $_POST['firstName'];
$lastName = $_POST['lastName'];
$email = $_POST['email'];
$number = $_POST['number'];


$conn = new mysqli('localhost','root','','testing');
if($conn->connect_error){
    die('Connection Failed :' .$conn->connect_error);
}
else{
    $stmt =  $conn->prepare("insert into registration(firstName,lastName,email,number) 
        values(?,?,?,?)");
    $stmt->bind_param("sssi",$firstName,$lastName,$email,$number);
    $stmt->execute();
    echo "registration successfully";
    $stmt->close();
    $conn->close();

}

?>
