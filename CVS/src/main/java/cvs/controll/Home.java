package cvs.controll;

import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping; 

@Controller
@AutoConfigurationPackage
public class Home {	
	@RequestMapping("/")
	public String Home(Model model){
		return "index";
	}
}
