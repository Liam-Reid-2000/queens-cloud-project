<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('functions.inc.php');

$output = array(
	"error" => false,
	"string" => "",
	"answer" => 0
);

$t = $_REQUEST['text'];

$answer=wordcount($t);

$output['string']="Contains ".$answer." words";
$output['answer']=$answer;

if (strlen($t)<1) {
	$output['error']=true;
	$output['string']="Error: String Empty";
}

echo json_encode($output);
exit();
