package cvs.repository;

import java.util.ArrayList;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import cvs.entity.prodEntity;

@Repository
@AutoConfigurationPackage
public class repository {
	private JdbcTemplate temp;
	
	@Autowired
	public repository(DataSource ds){
		temp= new JdbcTemplate(ds);
	}
	
	public List<prodEntity> getList(){
		List<prodEntity>list = new ArrayList<prodEntity>();
		String sql = "select * from CU";
		list.addAll(temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),
				rs.getString(3),rs.getString(4),"CU",rs.getString(5))));
		sql = "select * from GS";
		list.addAll(temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),
				rs.getString(3),rs.getString(4),"GS",rs.getString(5))));		
		return list;
	}

}
