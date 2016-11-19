package cvs.controll;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import cvs.service.SearchService; 

@Controller
@AutoConfigurationPackage
public class Home {	
	@Autowired
	SearchService searchService;
	
	
	@RequestMapping("/")
	public String Home(Model model){
		return "index";
	}
}