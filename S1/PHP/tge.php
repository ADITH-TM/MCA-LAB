<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Database Data</title>
<style>
table {
width: 50%;
border-collapse: collapse;
margin: 20px 0;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}
</style>
</head>
<body>
<?php
// Database credentials$servername = "localhost";
$username = "root";
$password = "";
$database = "mab";
// Create connection
$conn = new mysqli($servername, $username, $password, $database);
// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
// SQL query to retrieve data from the table
$sql = "SELECT * FROM pgm1";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
echo "<table><tr><th>ID</th><th>Name</th><th>Email</th></tr>";
// Output data of each row
while($row = $result->fetch_assoc()) {
echo "<tr><td>".$row["id"]."</td><td>".$row["name"]."</td><td>".$row["email"]."</td></tr>";
}
echo "</table>";
} else {
echo "0 results found";
}
// Close connection
$conn->close();
?></body>
</html>
