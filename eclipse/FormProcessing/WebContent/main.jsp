<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>使用GET方法读取URL请求数据</title>
</head>
<body>
    <h1>使用GET方法读取URL请求数据</h1>
    <ul>
        <li><p>
                <b>UserName:</b>
                <%=request.getParameter("username")%>
            </p></li>
        <li><p>
                <b>Email:</b>
                <%=request.getParameter("email")%>
            </p></li>
    </ul>
</body>
</html>