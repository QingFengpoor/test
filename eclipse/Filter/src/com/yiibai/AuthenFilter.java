package com.yiibai;
import javax.servlet.*;

public class AuthenFilter implements Filter{

	public void init(FilterConfig config) throws ServletException {
		String testparam=config.getInitParameter("test-paramA");
		System.out.println("Test-param:"+testparam);
	}
	
	public void doFilter(ServletRequest request,ServletResponse response,FilterChain chain)
		throws java.io.IOException,ServletException{
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
		
		System.out.println("AuthenFilter doFilter");
		chain.doFilter(request, response);
		System.out.println("After AuthenFilter do Filter");
		
	}
	
	public void destroy() {
		System.out.println("destroy AuthenFilter");
	}
}
