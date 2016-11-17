package cvs.controll;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import cvs.service.SearchService;

@Controller
@AutoConfigurationPackage
public class SearchControll {
	@Autowired
	SearchService search;

	@RequestMapping(value="/searchWord",method=RequestMethod.POST)
	public void SearchWord(HttpServletResponse resp,@RequestParam(value="word")String word) throws Exception{		
		resp.setCharacterEncoding("utf-8");
		search.searchWord(word);
	}	
}
