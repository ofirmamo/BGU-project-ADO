<%@ page language="java" contentType="text/html; charset=windows-1255"
    pageEncoding="windows-1255"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1255">
	<title>My title</title>
</head>
<body>
	<%java.util.Date d = new java.util.Date(); %>
	<h1>
		Today's date is <%= d.toString() %> and it's working!!
	</h1>
</body>
</html>