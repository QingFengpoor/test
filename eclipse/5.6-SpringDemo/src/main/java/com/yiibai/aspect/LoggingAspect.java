package com.yiibai.aspect;

import org.aspectj.lang.JoinYiibai;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

@Aspect
public class LoggingAspect{
	@Before("execution(* com.yiibai.customer.bo.CustomerBo.addCustomer(..))")
	public void logBefore(JoinYiibai joinYiibai) {
		System.out.println("logBefore() is running!");
		System.out.println("hijacked : "+ joinYiibai.getSignature().getName());
		System.out.println("*******");
	}
}