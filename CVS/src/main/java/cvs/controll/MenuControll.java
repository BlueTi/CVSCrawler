package cvs.controll;

import java.io.PrintWriter;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import cvs.service.MenuService;

@Controller
@AutoConfigurationPackage
public class MenuControll {
	@Autowired
	MenuService ms;
	
	@ResponseBody
	@RequestMapping(value="/ajax/menuFood",method=RequestMethod.POST)
	public void menuFood(HttpServletResponse resp) throws Exception{	
		resp.setCharacterEncoding("utf-8");
		PrintWriter out = resp.getWriter();
		out.print(ms.menuFood());
	}
}
