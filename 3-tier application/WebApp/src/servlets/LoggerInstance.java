package servlets;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * 
 * @author Ofir
 * Logger instance
 */

public class LoggerInstance {
	
	private static final Logger logger = LogManager.getLogger(LoggerInstance.class);
	
	public static Logger getInstance()
	{
		return logger;
	}

}
