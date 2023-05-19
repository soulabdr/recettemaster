package com.example.examen.login;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class LoginService {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/login";
    private static final String DB_USERNAME = "root";
    private static final String DB_PASSWORD = "";

    public boolean isValidCredentials(String username, String password) {
        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD)) {
            String sql = "SELECT * FROM users WHERE username = ? AND password = ?";
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, username);
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
}