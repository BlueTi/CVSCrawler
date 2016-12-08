package cvs.controll;

import java.io.PrintWriter;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import cvs.service.SearchService;

@Controller
@AutoConfigurationPackage
public class SearchControll {
	@Autowired
	SearchService search;

	@ResponseBody
	@RequestMapping(value="/ajax/searchWord",method=RequestMethod.POST)
	public void SearchWord(HttpServletResponse resp,@RequestParam(value="word")String word) throws Exception{		
		resp.setCharacterEncoding("utf-8");
		PrintWriter out = resp.getWriter();
		out.print(search.searchWord(word));
	}	
	

	@RequestMapping(value="/test")
	@ResponseBody
	public void test(HttpServletResponse resp) throws Exception{	
		System.out.println("test");
		resp.setCharacterEncoding("utf-8");
		PrintWriter out = resp.getWriter();
		out.print("TEST");
	}
}
