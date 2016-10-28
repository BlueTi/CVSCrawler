package controller;

import java.util.List;

import javax.sql.DataSource;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
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
		builder.setType(EmbeddedDatabaseType.H2);
		builder.addScript("/DB/CU.sql");
		builder.addScript("/DB/GS.sql");
		//builder.addScript("/DB/GS_DUM.sql");
		EmbeddedDatabase db=builder.build();
		return db;
	}
	
	
	
	@RequestMapping("/")
	public String Home(Model model){
		List<prodEntity> list= listService.getList();
		JSONArray ar= new JSONArray();
		for(prodEntity p :list){
			JSONObject ob = new JSONObject();			
	        ob.put("prodImg",p.getProdImg());
			ob.put("prodName",p.getProdName());
			ob.put("prodPrice",p.getProdPrice());
			ob.put("prodTag",p.getProdTag());	
			if(p.getCVS().equals("CU"))
				ob.put("CVS", "image/CULogo.jpg");
			else if(p.getCVS().equals("GS"))
				ob.put("CVS", "image/GSLogo.gif");
			ar.add(ob);
		}
		model.addAttribute("list",ar);
		return "index";
	}
	
	@Autowired
	ListService listService;
	
	public static void main(String[] args) {
		ConfigurableApplicationContext context=SpringApplication.run(ProjectApplication.class, args);
		context.getBean(ListService.class);
	}
}
