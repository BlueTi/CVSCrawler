package cvs;

import javax.sql.DataSource;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabase;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseBuilder;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseType;

@SpringBootApplication
public class CvsApplication {
	
	@Bean
	public DataSource dataSource(){
		EmbeddedDatabaseBuilder builder = new EmbeddedDatabaseBuilder();
		builder.setType(EmbeddedDatabaseType.H2);
		builder.addScripts("/DB/start.sql","/DB/CU.sql","/DB/GS.sql","/DB/GS_DUM.sql");
		EmbeddedDatabase db=builder.build();
		return db;
	}

	public static void main(String[] args) {
		SpringApplication.run(CvsApplication.class, args);
	}
}
