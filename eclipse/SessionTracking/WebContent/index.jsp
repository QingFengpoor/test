<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.io.*,java.util.*" %>

<%
    // Get session creation time.
    Date createTime = new Date(session.getCreationTime());

    // Get last access time of this Webpage.
    Date lastAccessTime = new Date(session.getLastAccessedTime());

    String title = "Welcome Back to my website";
    Integer visitCount = new Integer(0);
    String visitCountKey = new String("visitCount");
    String userIDKey = new String("userID");
    String userID = new String("ABCD");

    // Check if this is new comer on your Webpage.
    if (session.isNew()) {
        title = "Welcome to my website";
        session.setAttribute(userIDKey, userID);
        session.setAttribute(visitCountKey, visitCount);
        session.setMaxInactiveInterval(900);
    }
    visitCount = (Integer) session.getAttribute(visitCountKey);
    visitCount = visitCount + 1;
    userID = (String) session.getAttribute(userIDKey);
    session.setAttribute(visitCountKey, visitCount);
%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Session会话跟踪示例</title>
</head>
<body>
    <div style="margin: auto; width: 80%;">
        <center>
            <h2>
                Session会话跟踪示例
                </h1>
        </center>

        <table border="1" align="center">
            <tr bgcolor="#949494">
                <th>会话信息</th>
                <th>值</th>
            </tr>
            <tr>
                <td>id</td>
                <td>
                    <%
                        out.print(session.getId());
                    %>
                </td>
            </tr>
            <tr>
                <td>创建时间</td>
                <td>
                    <%
                        out.print(createTime);
                    %>
                </td>
            </tr>
            <tr>
                <td>最近一次访问时间</td>
                <td>
                    <%
                        out.print(lastAccessTime);
                    %>
                </td>
            </tr>
            <tr>
                <td>用户ID</td>
                <td>
                    <%
                        out.print(userID);
                    %>
                </td>
            </tr>
            <tr>
                <td>访问次数</td>
                <td>
                    <%
                        out.print(visitCount);
                    %>
                </td>
            </tr>
        </table>
    </div>
</body>
</html>