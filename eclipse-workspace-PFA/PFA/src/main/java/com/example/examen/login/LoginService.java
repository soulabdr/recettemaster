package com.example.examen.login;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.regex.Pattern;

public class LoginService {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/login";
    private static final String DB_USERNAME = "root";
    private static final String DB_PASSWORD = "";

    public boolean isValidCredentials(String email, String password) {
       
        if (!isValidEmail(email)) {
            return false;
        }

        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD)) {
            String sql = "SELECT * FROM users WHERE email = ? AND password = ?";
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, email);
            statement.setString(2, password);

            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    return true;
                } else {
                    return false;
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return false;
    }

    
    private boolean isValidEmail(String email) {
        
        String emailRegex = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$";
        Pattern pattern = Pattern.compile(emailRegex);

        return pattern.matcher(email).matches();
    }
}