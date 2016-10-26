package controller;

import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabase;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseBuilder;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import entity.prodEntity;

@SpringBootApplication
@Controller
@ComponentScan({"controller","repository"})
public class ProjectApplication {
	@Bean
	public DataSource dataSource(){
		EmbeddedDatabaseBuilder builder = new EmbeddedDatabaseBuilder();
		EmbeddedDatabase db=builder.setType(EmbeddedDatabaseType.H2).addScript("/DB/CU.sql").build();
		return db;
	}
	
	
	
	@RequestMapping("/")
	public String Home(Model model){
		List<prodEntity> list= listService.getList();
		model.addAttribute("list",list);
		return "index";
	}
	
	@Autowired
	ListService listService;
	
	public static void main(String[] args) {
		ConfigurableApplicationContext context=SpringApplication.run(ProjectApplication.class, args);
		context.getBean(ListService.class);
	}
}
