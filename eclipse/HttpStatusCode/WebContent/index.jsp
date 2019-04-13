<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>发送HTTP状态码</title>
</head>
<body>
    <%
        // Set error code and reason.
        response.sendError(403, "不给张云志看!!!");
    %>
</body>
</html>