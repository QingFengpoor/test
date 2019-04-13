<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>删除Cookies</title>
</head>
<body>
    <div style="margin: auto; width: 80%;">
        <center>
         <h1>删除Cookies</h1>
      </center>
      <%
         Cookie cookie = null;
         Cookie[] cookies = null;

         // Get an array of Cookies associated with the this domain
         cookies = request.getCookies();

         if( cookies != null ) {
            out.println("<h2>找到的Cookie名称和值</h2>");
            for (int i = 0; i < cookies.length; i++) {
               cookie = cookies[i];
               if(cookie.getName().equals("username")) {
                  cookie.setMaxAge(0);
                  response.addCookie(cookie);
                  out.print("Deleted cookie: " + cookie.getName( ) + "<br/>");
               }
               out.print("Name : " + cookie.getName( ) + ",  ");
               out.print("Value: " + cookie.getValue( )+" <br/>");
            }
         } else {
            out.println(
            "<h2>No cookies founds</h2>");
         }
      %>
    </div>
</body>
</html>