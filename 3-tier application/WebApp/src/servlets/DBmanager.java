package servlets;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class DBmanager {

	static private Connection con = null;
	
	public DBmanager() {
		synchronized (this) {
			if(con == null) {
				connectToDatabase();
				initalizeDB();
			}
		}
	}
	
	private void connectToDatabase() {
		try {
			Class.forName("org.sqlite.JDBC");
			String url = "jdbc:sqlite:../DB/Data.db";
			con = DriverManager.getConnection(url);
		}catch(Exception e) {
			e.printStackTrace();
		}
		System.out.println("Database has been opened");
	}
	
	private void initalizeDB() {
		try {
			Statement stmt = con.createStatement();
			String sql = "CREATE TABLE IF NOT EXISTS database" +
						 "(ID   INT PRIMARY KEY NOT NULL," +
						 "NAME TEXT 		   NOT NULL," +
						 "AGE  INT 			   NOT NULL)";
			stmt.execute(sql);
			stmt.close();
		}catch(Exception e) {
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
