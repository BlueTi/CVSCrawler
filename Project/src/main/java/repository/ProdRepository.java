package repository;

import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import entity.prodEntity;

@Repository
public class ProdRepository {
	private JdbcTemplate temp;
	
	
	@Autowired
	public ProdRepository(DataSource ds){
		temp= new JdbcTemplate(ds);
	}
	
	public List<prodEntity> getList(){		
		String sql="select * from CU";		
		return temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4),"CU"));
	}
	public List<prodEntity> searchList(String word){
		String sql="select * from CU where prodName like '%"+word+"%'";
		return temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4),"CU"));
	}
}
