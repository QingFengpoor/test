<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.io.*,java.util.*" %>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>服务器响应示例</title>
</head>
<body>
    <div style="margin: auto; width: 80%;">
        <h2>自动刷新HTTP标头示例</h2>
        <%
            // Set refresh, autoload time as 5 seconds
            response.setIntHeader("Refresh", 1);

            // Get current time
            Calendar calendar = new GregorianCalendar();

            String am_pm;
            int hour = calendar.get(Calendar.HOUR);
            int minute = calendar.get(Calendar.MINUTE);
            int second = calendar.get(Calendar.SECOND);

            if (calendar.get(Calendar.AM_PM) == 0)
                am_pm = "AM";
            else
                am_pm = "PM";
            String CT = hour + ":" + minute + ":" + second + " " + am_pm;
            out.println("Current Time is: " + CT + "\n");
        %>
    </div>
</body>
</html>