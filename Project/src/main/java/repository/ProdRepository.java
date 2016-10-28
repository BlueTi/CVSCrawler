package repository;

import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import entity.CUprodEntity;
import entity.GSprodEntity;

@Repository
public class ProdRepository {
	private JdbcTemplate temp;
	
	
	@Autowired
	public ProdRepository(DataSource ds){
		temp= new JdbcTemplate(ds);
	}
	
	public List<CUprodEntity> getCUList(){		
		String sql="select * from CU";		
		return temp.query(sql, (rs,no)->new CUprodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4)));
	}
	
	public List<GSprodEntity> getGSList(){		
		String sql="select * from GS";		
		return temp.query(sql, (rs,no)->new GSprodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4),rs.getString(5)));
	}
	public List<CUprodEntity> searchList(String word){
		String sql="select * from CU where prodName like '%"+word+"%'";
		return temp.query(sql, (rs,no)->new CUprodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4)));
	}
}
