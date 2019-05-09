package com.yiibai.core;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.yiibai.customer.bo.*;

public class App{
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		ApplicationContext appContext=new ClassPathXmlApplicationContext(new String[] {"applicationContext.xml"});
		CustomerBo customer=(CustomerBo) appContext.getBean("customerBo");
		customer.addCustomer();
	}
}