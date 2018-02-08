package servlets;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class DBmanager {

	private static final Logger logger = LogManager.getLogger(DBmanager.class);

	private static final Connection con = connectToDatabase();

	//TODO - change logger properties for this logger.
	

	private static Connection connectToDatabase() {
		Connection connection = null;
		try {
			Class.forName("org.sqlite.JDBC");
			String url = "jdbc:sqlite:../DB/Data.db";
			connection = DriverManager.getConnection(url);
		}catch(Exception e) {
			e.printStackTrace();
		}
		logger.info((" \"message\": Database has been opened"));
		System.out.println("Database has been opened");
		initalizeDB();
		return connection;
	}
	
	private static void initalizeDB() {
			try (Statement stmt = con.createStatement()) {
				String sql = "CREATE TABLE IF NOT EXISTS database" +
						"(ID   INT PRIMARY KEY NOT NULL," +
						"NAME TEXT 		   NOT NULL," +
						"AGE  INT 			   NOT NULL)";
				stmt.execute(sql);
				stmt.close();
			}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public boolean addToTable() {
		return false;
		//TODO - add code to add data to database
	}
		
	public boolean removeFromTable() {
		return false;
		//TODO - add code to remove data from database
	}
}
