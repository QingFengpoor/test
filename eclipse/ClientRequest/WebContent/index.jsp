<%@ page import="java.util.*,java.io.*" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>客户端请求参数数据</title>
</head>
<body>
    <div style="margin: auto; width: 80%;">
        <h2>客户端请求头参数数据示例</h2>

        <table width="100%" border="1" align="center">
            <tr bgcolor="#949494">
                <th>Header Name</th>
                <th>Header Value(s)</th>
            </tr>
            <%
            	Enumeration headerNames = request.getHeaderNames();
                while (headerNames.hasMoreElements()) {
                    String paramName = (String) headerNames.nextElement();
                    out.print("<tr><td>" + paramName + "</td>\n");
                    String paramValue = request.getHeader(paramName);
                    out.println("<td> " + paramValue + "</td></tr>\n");
                }
            %>
        </table>
    </div>
</body>
</html>