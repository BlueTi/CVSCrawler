package cvs.controll;

import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import cvs.entity.prodEntity;
import cvs.repository.repository; 

@Controller
@AutoConfigurationPackage
public class Home {
	@Autowired
	repository repo;	
	
	@RequestMapping("/")
	public String Home(Model model){
		List<prodEntity>list=repo.getList();
		JSONArray ar = new JSONArray();
		for(prodEntity p :list){
			JSONObject ob = new JSONObject();			
	        ob.put("prodImg",p.getProdImg());
			ob.put("prodName",p.getProdName());
			ob.put("prodPrice",p.getProdPrice());			
			ob.put("prodTag",p.getProdTag());
			
			if(p.getCVS().equals("CU"))	ob.put("CVS", "image/CULogo.jpg");
			else if(p.getCVS().equals("GS")) ob.put("CVS", "image/GSLogo.gif");
			ar.add(ob);
		}
		model.addAttribute("list",ar);
		return "index";
	}
}
