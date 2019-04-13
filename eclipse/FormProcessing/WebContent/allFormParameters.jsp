<%@ page import="java.io.*,java.util.*" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>获取所有表单数据</title>
</head>
<body>
    <div style="margin: auto; width: 80%;">
        <h2>获取所有表单数据</h2>
        <table width="100%" border="1" align="center">
            <tr bgcolor="#949494">
                <th>Param Name</th>
                <th>Param Value(s)</th>
            </tr>
            <%
                Enumeration paramNames = request.getParameterNames();
                while (paramNames.hasMoreElements()) {
                    String paramName = (String) paramNames.nextElement();
                    out.print("<tr><td>" + paramName + "</td>\n");
                    String paramValue = request.getParameter(paramName);
                    out.println("<td> " + paramValue + "</td></tr>\n");
                }
            %>
        </table>
    </div>
</body>
</html>