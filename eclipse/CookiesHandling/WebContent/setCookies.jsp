<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>接收表单并设置Cookies</title>
</head>
<body>
    <%
        // Create cookies for first and last names.      
        Cookie cookie1 = new Cookie("username", request.getParameter("username"));
        Cookie cookie2 = new Cookie("email", request.getParameter("email"));

        // Set expiry date after 24 Hrs for both the cookies.
        cookie1.setMaxAge(60 * 60 * 24);
        cookie2.setMaxAge(60 * 60 * 24);

        // Add both the cookies in the response header.
        response.addCookie(cookie1);
        response.addCookie(cookie2);
    %>
    <div style="margin: auto; width: 80%;">
        <center>
            <h2>设置Cookies</h2>
        </center>
        <ul>
            <li><p>
                    <b>用户名:</b>
                    <%=request.getParameter("username")%>
                </p></li>
            <li><p>
                    <b>Email:</b>
                    <%=request.getParameter("email")%>
                </p></li>
        </ul>
    </div>
</body>
</html>